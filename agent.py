"""
Miraya Campaign Agent — Standalone agentic pipeline using the Anthropic SDK.

Runs the full campaign workflow automatically:
  1. Loads brand context from CLAUDE.md
  2. Fetches Meta audience insights
  3. Researches competitors (from CLAUDE.md)
  4. Finds trending posts for the keyword
  5. Researches hashtags
  6. Researches the topic in depth
  7. Generates a Hinglish campaign draft (Instagram + Facebook)
  8. Presents draft and waits for user approval before publishing

Usage:
  python agent.py "cotton kurta"
  python agent.py "Durga Puja collection"
  python agent.py  # will prompt for keyword interactively

Requirements:
  - ANTHROPIC_API_KEY in .env
  - META_ACCESS_TOKEN in .env (run auth_setup.py first)
  - pip install -r requirements.txt
"""

import sys
import os
import json
from pathlib import Path
from dotenv import load_dotenv
import anthropic
import meta_client as meta
import web_search as ws

load_dotenv()

# ---------------------------------------------------------------------------
# Tool definitions (matches server.py tools)
# ---------------------------------------------------------------------------

TOOLS = [
    {
        "name": "list_connected_accounts",
        "description": "List all Facebook Pages and Instagram Business accounts connected to the Meta access token.",
        "input_schema": {"type": "object", "properties": {}, "required": []},
    },
    {
        "name": "get_facebook_insights",
        "description": "Fetch audience demographics and weekly engagement for a Facebook Page.",
        "input_schema": {
            "type": "object",
            "properties": {"page_id": {"type": "string", "description": "Facebook Page ID"}},
            "required": ["page_id"],
        },
    },
    {
        "name": "get_instagram_insights",
        "description": "Fetch audience demographics and weekly engagement for an Instagram Business account.",
        "input_schema": {
            "type": "object",
            "properties": {"ig_user_id": {"type": "string", "description": "Instagram User ID"}},
            "required": ["ig_user_id"],
        },
    },
    {
        "name": "web_search",
        "description": (
            "Search the web. Use for: competitor research, trending posts, "
            "hashtag research, topic/cultural context. "
            "Returns list of {title, url, snippet}."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "max_results": {"type": "integer", "default": 6},
            },
            "required": ["query"],
        },
    },
    {
        "name": "search_news",
        "description": "Search recent news. Use for trending topics, festivals, current events in India.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "max_results": {"type": "integer", "default": 5},
            },
            "required": ["query"],
        },
    },
    {
        "name": "publish_to_facebook",
        "description": (
            "Publish a post to the Miraya Facebook Page. "
            "ONLY call this after the user explicitly says 'post it' or 'publish'."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "page_id": {"type": "string"},
                "message": {"type": "string"},
                "image_url": {"type": "string", "default": ""},
            },
            "required": ["page_id", "message"],
        },
    },
    {
        "name": "publish_to_instagram",
        "description": (
            "Publish an image post to the Miraya Instagram account. "
            "ONLY call this after the user explicitly says 'post it' or 'publish'."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "ig_user_id": {"type": "string"},
                "caption": {"type": "string"},
                "image_url": {"type": "string"},
            },
            "required": ["ig_user_id", "caption", "image_url"],
        },
    },
]


# ---------------------------------------------------------------------------
# Tool executor
# ---------------------------------------------------------------------------

def execute_tool(name: str, inputs: dict) -> str:
    try:
        if name == "list_connected_accounts":
            result = meta.list_connected_accounts()
        elif name == "get_facebook_insights":
            result = meta.get_facebook_insights(inputs["page_id"])
        elif name == "get_instagram_insights":
            result = meta.get_instagram_insights(inputs["ig_user_id"])
        elif name == "web_search":
            result = ws.search(inputs["query"], inputs.get("max_results", 6))
        elif name == "search_news":
            result = ws.search_news(inputs["query"], inputs.get("max_results", 5))
        elif name == "publish_to_facebook":
            result = meta.publish_to_facebook(
                page_id=inputs["page_id"],
                message=inputs["message"],
                image_url=inputs.get("image_url") or None,
            )
        elif name == "publish_to_instagram":
            result = meta.publish_to_instagram(
                ig_user_id=inputs["ig_user_id"],
                image_url=inputs["image_url"],
                caption=inputs["caption"],
            )
        else:
            result = {"error": f"Unknown tool: {name}"}
    except Exception as e:
        result = {"error": str(e)}

    return json.dumps(result, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------------------
# Brand context loader
# ---------------------------------------------------------------------------

def load_brand_context() -> str:
    claude_md = Path(__file__).parent / "CLAUDE.md"
    if claude_md.exists():
        return claude_md.read_text(encoding="utf-8")
    return "No CLAUDE.md found. Use generic Miraya brand context."


# ---------------------------------------------------------------------------
# Agent loop
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """You are the Miraya Social Media Campaign Agent — a fully autonomous
social media campaign creator for Miraya, a women's ethnic wear brand in Siliguri, West Bengal.

The complete brand context is provided below. Read it carefully before taking any action.

Your job when given a keyword:
1. Fetch Miraya's Instagram and Facebook audience insights (use the account IDs from brand context, or call list_connected_accounts if missing)
2. Research competitor brands from the brand context using web_search
3. Find trending posts and content for the keyword using web_search
4. Research relevant hashtags using web_search — build a strategic mix of broad, niche, local, brand, and trending tags
5. Research the topic in cultural/seasonal depth using web_search and search_news
6. Generate a complete Hinglish campaign draft with:
   - Instagram caption (hook + body + CTA directing to DM or store — no website links)
   - Researched hashtags (18–22 for Instagram, 3–5 for Facebook) with explanation of the strategy
   - Facebook caption (slightly longer, conversational)
   - Detailed image/creative prompt for a designer or AI tool
   - Posting time recommendation

IMPORTANT RULES:
- Write in natural Hinglish (Hindi-English mix the way urban Indian women speak)
- CTAs must be DM-based or store-visit based — Miraya has no online store
- Always research hashtags — never guess them
- Always present as DRAFT — never publish without explicit user confirmation
- Never invent prices — only use prices from brand context

After presenting the draft, ask if the user wants edits or to post it.

---
BRAND CONTEXT:
{brand_context}
"""


def run_agent(keyword: str) -> None:
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY is not set in .env")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    brand_context = load_brand_context()

    system = SYSTEM_PROMPT.format(brand_context=brand_context)
    messages: list[dict] = [
        {
            "role": "user",
            "content": (
                f"Run the full campaign pipeline for the keyword: **{keyword}**\n\n"
                "Go through all steps automatically — audience insights, competitor research, "
                "trending analysis, hashtag research, topic research — then generate the "
                "complete Hinglish campaign draft for Instagram and Facebook."
            ),
        }
    ]

    print(f"\n{'='*60}")
    print(f"  MIRAYA CAMPAIGN AGENT")
    print(f"  Keyword: {keyword}")
    print(f"{'='*60}\n")

    # Agentic loop
    while True:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=8096,
            system=system,
            tools=TOOLS,
            messages=messages,
        )

        # Collect all text and tool use blocks
        text_blocks = []
        tool_calls = []

        for block in response.content:
            if block.type == "text":
                text_blocks.append(block.text)
            elif block.type == "tool_use":
                tool_calls.append(block)

        # Print any text output
        if text_blocks:
            print("\n".join(text_blocks))

        # If no tool calls, the agent is done
        if not tool_calls:
            break

        # Execute all tool calls and collect results
        tool_results = []
        for tc in tool_calls:
            print(f"\n[Tool] {tc.name}({json.dumps(tc.input, ensure_ascii=False)[:120]}...)")
            result_str = execute_tool(tc.name, tc.input)
            tool_results.append({
                "type": "tool_result",
                "tool_use_id": tc.id,
                "content": result_str,
            })

        # Add assistant response and tool results to message history
        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_results})

        # If agent signalled end of turn, stop the loop
        if response.stop_reason == "end_turn":
            break

    # Interactive follow-up
    print(f"\n{'='*60}")
    while True:
        user_input = input("\nYou: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ("exit", "quit", "q"):
            print("Campaign session ended.")
            break

        messages.append({"role": "user", "content": user_input})

        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=8096,
            system=system,
            tools=TOOLS,
            messages=messages,
        )

        while True:
            text_blocks = []
            tool_calls = []

            for block in response.content:
                if block.type == "text":
                    text_blocks.append(block.text)
                elif block.type == "tool_use":
                    tool_calls.append(block)

            if text_blocks:
                print("\nMiraya Agent:", "\n".join(text_blocks))

            if not tool_calls:
                messages.append({"role": "assistant", "content": response.content})
                break

            tool_results = []
            for tc in tool_calls:
                print(f"\n[Tool] {tc.name}({json.dumps(tc.input, ensure_ascii=False)[:120]}...)")
                result_str = execute_tool(tc.name, tc.input)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": tc.id,
                    "content": result_str,
                })

            messages.append({"role": "assistant", "content": response.content})
            messages.append({"role": "user", "content": tool_results})

            if response.stop_reason == "end_turn":
                break

            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=8096,
                system=system,
                tools=TOOLS,
                messages=messages,
            )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    if len(sys.argv) > 1:
        keyword = " ".join(sys.argv[1:])
    else:
        keyword = input("Enter campaign keyword or theme: ").strip()
        if not keyword:
            print("No keyword provided. Exiting.")
            sys.exit(0)

    run_agent(keyword)
