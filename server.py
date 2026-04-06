"""
HinglishReach MCP Server — Miraya

Exposes tools to Claude for:
- Facebook + Instagram account management and insights (Meta Graph API)
- Web search for competitor research, trend discovery, hashtag research

All brand context is read from CLAUDE.md automatically.
Claude handles Hinglish content generation — no separate AI call needed.

Usage:
  python server.py
  claude mcp add miraya python /path/to/server.py
"""

import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
import meta_client as meta
import web_search as ws

load_dotenv()

mcp = FastMCP(
    "Miraya Social Media Agent",
    instructions=(
        "You are the social media campaign agent for Miraya, a women's ethnic wear "
        "brand in Siliguri, West Bengal. All brand context is in CLAUDE.md — always "
        "read it before generating any content. "
        "\n\nYou have tools to: fetch Meta audience insights, search the web for "
        "competitor content, trending posts, and hashtag research. "
        "\n\nContent rules (from CLAUDE.md):\n"
        "- Write campaigns in Hinglish (natural Hindi-English mix)\n"
        "- CTAs must direct to store visit or Instagram DM — never a website link\n"
        "- Always research hashtags with web_search before finalising a post\n"
        "- Always output as DRAFT — never publish without explicit user confirmation\n"
        "- Never invent prices — only use prices from CLAUDE.md"
    ),
)


# ---------------------------------------------------------------------------
# Meta account tools
# ---------------------------------------------------------------------------

@mcp.tool()
def list_connected_accounts() -> dict:
    """
    List all Facebook Pages and Instagram Business accounts connected to the
    Meta access token. Call this first to confirm account IDs.
    Returns: facebook_page_id, facebook_page_name, instagram_account_id, instagram_username.
    """
    return meta.list_connected_accounts()


@mcp.tool()
def get_facebook_insights(page_id: str) -> dict:
    """
    Fetch audience demographics and weekly engagement for a Facebook Page.
    Use the Facebook Page ID from CLAUDE.md or list_connected_accounts.
    Returns: weekly reach, engagements, followers, gender/age/city/country breakdown.
    Note: demographic data has a 48-hour lag; requires 100+ followers.
    """
    return meta.get_facebook_insights(page_id)


@mcp.tool()
def get_instagram_insights(ig_user_id: str) -> dict:
    """
    Fetch audience demographics and weekly engagement for an Instagram Business account.
    Use the Instagram User ID from CLAUDE.md or list_connected_accounts.
    Returns: weekly reach, impressions, profile views, follower demographics.
    Note: demographic data has a 48-hour lag; requires 100+ followers.
    """
    return meta.get_instagram_insights(ig_user_id)


@mcp.tool()
def publish_to_facebook(page_id: str, message: str, image_url: str = "") -> dict:
    """
    Publish a post to the Miraya Facebook Page Feed.
    Only call this after the user explicitly confirms the draft with 'post it' or 'publish'.
    Args:
        page_id: Facebook Page ID
        message: Full caption in Hinglish with hashtags included
        image_url: Optional public image URL
    """
    return meta.publish_to_facebook(page_id=page_id, message=message, image_url=image_url or None)


@mcp.tool()
def publish_to_instagram(ig_user_id: str, caption: str, image_url: str) -> dict:
    """
    Publish an image post to the Miraya Instagram Feed.
    Only call this after the user explicitly confirms the draft with 'post it' or 'publish'.
    Args:
        ig_user_id: Instagram User ID
        caption: Full caption in Hinglish with hashtags included
        image_url: Publicly accessible image URL (Instagram fetches server-side)
    """
    return meta.publish_to_instagram(ig_user_id=ig_user_id, image_url=image_url, caption=caption)


# ---------------------------------------------------------------------------
# Web search tools
# ---------------------------------------------------------------------------

@mcp.tool()
def web_search(query: str, max_results: int = 6) -> list[dict]:
    """
    Search the web for any query. Use this for:
    - Competitor brand research (search their Instagram handle or brand name)
    - Trending posts and content formats for a keyword
    - Hashtag research (search '[keyword] Instagram hashtags India')
    - Topic/cultural context research (festivals, trends, news)
    Returns list of results with title, url, snippet.
    """
    return ws.search(query, max_results=max_results)


@mcp.tool()
def search_news(query: str, max_results: int = 5) -> list[dict]:
    """
    Search recent news for a query. Use this for:
    - Finding trending topics tied to current events
    - Festival or cultural moment context
    - Understanding what's top-of-mind for Indian audiences right now
    Returns list of news results with title, url, snippet, date, source.
    """
    return ws.search_news(query, max_results=max_results)


if __name__ == "__main__":
    mcp.run()
