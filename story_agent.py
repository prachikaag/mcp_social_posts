"""
Miraya Story Agent — "Woh Har Roz Ki Ladki" Comic Campaign Generator

Generates complete storytelling comic campaigns for Miraya's everyday-woman series.
Reads both CLAUDE.md (brand context) and art_style.md (visual direction) before
generating any content.

Outputs:
- Full 5-panel story arc per post
- Complete image generation prompts (ready for Canva, Midjourney, DALL-E, Firefly)
- Hinglish captions for Instagram carousel and Facebook
- Posting schedule for multi-post series
- All cohesion rules from art_style.md enforced automatically

Usage:
  python story_agent.py "Durga Puja — women who celebrate quietly"
  python story_agent.py "spring summer — everyday moments"
  python story_agent.py  # prompts interactively

The agent asks how many posts (1 or a series of 3–5), then generates everything.
"""

import sys
import os
import json
from pathlib import Path
from dotenv import load_dotenv
import anthropic
import web_search as ws

load_dotenv()

# ---------------------------------------------------------------------------
# Context loaders
# ---------------------------------------------------------------------------

def load_file(filename: str) -> str:
    path = Path(__file__).parent / filename
    if path.exists():
        return path.read_text(encoding="utf-8")
    return f"[{filename} not found]"


def load_context() -> tuple[str, str]:
    return load_file("CLAUDE.md"), load_file("art_style.md")


# ---------------------------------------------------------------------------
# Tools for the story agent
# Only needs web search — no Meta API calls needed for story posts
# ---------------------------------------------------------------------------

TOOLS = [
    {
        "name": "web_search",
        "description": (
            "Search the web. Use for: researching the emotional truth behind a campaign theme, "
            "finding relatable Indian women's stories, researching cultural moments, "
            "finding trending hashtags for the story series. "
            "Returns list of {title, url, snippet}."
        ),
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
        "name": "search_news",
        "description": "Search recent news — useful for cultural moments and timing hooks for Indian women.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "max_results": {"type": "integer", "default": 4},
            },
            "required": ["query"],
        },
    },
]


def execute_tool(name: str, inputs: dict) -> str:
    try:
        if name == "web_search":
            result = ws.search(inputs["query"], inputs.get("max_results", 5))
        elif name == "search_news":
            result = ws.search_news(inputs["query"], inputs.get("max_results", 4))
        else:
            result = {"error": f"Unknown tool: {name}"}
    except Exception as e:
        result = {"error": str(e)}
    return json.dumps(result, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------------------
# System prompt
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """You are the Miraya Story Agent — specialised in creating emotionally powerful
storytelling comic campaigns for Miraya, a women's ethnic wear brand in Siliguri, West Bengal.

You create the "Woh Har Roz Ki Ladki" (The Everyday Woman) series — caricature/comic posts
that show real Indian women in their daily lives and how Miraya fits into those lives.

You have TWO source documents to guide every decision:

1. BRAND CONTEXT (CLAUDE.md): Voice, audience, products, CTA rules, brand story
2. ART STYLE GUIDE (art_style.md): Visual style, character archetypes, colour palettes,
   panel structure, base image prompts, cohesion rules

---
BRAND CONTEXT:
{brand_context}

---
ART STYLE GUIDE:
{art_style}

---

YOUR JOB when given a campaign theme:

1. Research the emotional truth behind the theme for Indian women (use web_search)
2. Research relevant hashtags (use web_search)
3. Decide: single post or series? If series, plan 3 posts with different character archetypes
4. For each post:
   a. Map the 5-panel emotional arc (reality → strength → almost forgot herself → Miraya → glow)
   b. Write panel narration text (Hinglish, max 10 words per panel)
   c. Write COMPLETE image generation prompts for each panel — detailed enough to paste
      directly into Canva AI, Midjourney, DALL-E 3, or Adobe Firefly
   d. Write the Instagram carousel caption (Hinglish, emotional, cohesive)
   e. Write the Facebook variant
5. Enforce carousel cohesion: ONE colour palette across ALL slides of a post, consistent
   character design, consistent typography, consistent illustration style
6. Produce a posting schedule if it's a series

CRITICAL RULES:
- Read art_style.md colour palettes — every image prompt must include the exact hex codes
- Use the BASE PROMPT from art_style.md as the foundation for every image prompt
- Each panel prompt must include: style, character, scene, palette hex codes, text overlay, emotion word
- Captions: natural Hinglish — the way real Indian women speak, not translated Hindi
- CTAs: DM @miraya_india or visit Planet Mall, Siliguri — NEVER a website link
- ALWAYS output as DRAFT — never say "this is published" or suggest it's live
- The final panel of every story must show her glowing — she is celebrated, never pitied
"""


# ---------------------------------------------------------------------------
# Agent loop
# ---------------------------------------------------------------------------

def run_story_agent(theme: str, num_posts: int = 0) -> None:
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set in .env")
        sys.exit(1)

    brand_context, art_style = load_context()
    system = SYSTEM_PROMPT.format(brand_context=brand_context, art_style=art_style)

    # Build initial user message
    if num_posts == 0:
        series_instruction = (
            "Decide whether this should be a single post or a 3-post series based on the theme. "
            "If unsure, default to a 3-post series — one character archetype per post."
        )
    elif num_posts == 1:
        series_instruction = "Create a single story post (5-panel carousel)."
    else:
        series_instruction = f"Create a series of {num_posts} story posts, each with a different character archetype."

    user_message = (
        f"Create the Miraya 'Woh Har Roz Ki Ladki' storytelling comic campaign.\n\n"
        f"Campaign theme: **{theme}**\n\n"
        f"{series_instruction}\n\n"
        f"Pipeline:\n"
        f"1. Research the emotional truth behind this theme for Indian women (web_search)\n"
        f"2. Research hashtags for this theme + Miraya's storytelling series (web_search)\n"
        f"3. Plan the character archetypes and story arcs\n"
        f"4. For each post: write 5-panel arc, panel narration, complete image prompts, "
        f"Instagram caption, Facebook caption\n"
        f"5. Enforce full colour palette cohesion across all slides (from art_style.md)\n"
        f"6. Produce posting schedule if series\n\n"
        f"Output the complete DRAFT series in full detail — image prompts should be "
        f"ready to paste directly into Canva AI, Midjourney, or DALL-E 3."
    )

    messages: list[dict] = [{"role": "user", "content": user_message}]

    print(f"\n{'='*60}")
    print(f"  MIRAYA STORY AGENT")
    print(f"  Woh Har Roz Ki Ladki Campaign")
    print(f"  Theme: {theme}")
    print(f"{'='*60}\n")

    client = anthropic.Anthropic(api_key=api_key)

    # Agentic loop
    while True:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=16000,
            system=system,
            tools=TOOLS,
            messages=messages,
        )

        text_blocks = [b for b in response.content if b.type == "text"]
        tool_calls = [b for b in response.content if b.type == "tool_use"]

        if text_blocks:
            for b in text_blocks:
                print(b.text)

        if not tool_calls:
            messages.append({"role": "assistant", "content": response.content})
            break

        tool_results = []
        for tc in tool_calls:
            print(f"\n[Research] {tc.name}: {tc.input.get('query', '')[:80]}...")
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

    # Interactive follow-up
    print(f"\n{'='*60}")
    print("Campaign draft complete. You can now:")
    print("  - Ask to edit any post, panel, caption, or image prompt")
    print("  - Ask to add more posts to the series")
    print("  - Ask to adjust the colour palette")
    print("  - Type 'exit' to end the session")
    print(f"{'='*60}\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ("exit", "quit", "q"):
            print("Story session ended. Drafts saved above.")
            break

        messages.append({"role": "user", "content": user_input})

        while True:
            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=16000,
                system=system,
                tools=TOOLS,
                messages=messages,
            )

            text_blocks = [b for b in response.content if b.type == "text"]
            tool_calls = [b for b in response.content if b.type == "tool_use"]

            if text_blocks:
                print("\nMiraya Story Agent:", "\n".join(b.text for b in text_blocks))

            if not tool_calls:
                messages.append({"role": "assistant", "content": response.content})
                break

            tool_results = []
            for tc in tool_calls:
                print(f"\n[Research] {tc.name}: {tc.input.get('query', '')[:80]}...")
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
                max_tokens=16000,
                system=system,
                tools=TOOLS,
                messages=messages,
            )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    args = sys.argv[1:]

    # Check for --posts flag
    num_posts = 0
    filtered_args = []
    i = 0
    while i < len(args):
        if args[i] == "--posts" and i + 1 < len(args):
            try:
                num_posts = int(args[i + 1])
                i += 2
            except ValueError:
                i += 1
        else:
            filtered_args.append(args[i])
            i += 1

    if filtered_args:
        theme = " ".join(filtered_args)
    else:
        print("Miraya Story Agent — Woh Har Roz Ki Ladki")
        print("─" * 40)
        theme = input("Campaign theme: ").strip()
        if not theme:
            print("No theme provided. Exiting.")
            sys.exit(0)
        if num_posts == 0:
            try:
                num_posts_input = input("Number of posts in series? (1–5, or Enter for auto): ").strip()
                num_posts = int(num_posts_input) if num_posts_input else 0
            except ValueError:
                num_posts = 0

    run_story_agent(theme, num_posts)
