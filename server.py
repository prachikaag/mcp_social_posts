"""
HinglishReach MCP Server

Exposes Facebook and Instagram tools to Claude so it can:
- List your connected Meta accounts
- Fetch audience insights (demographics, engagement)
- Publish posts to Facebook Page Feed and Instagram Feed

Claude handles Hinglish content generation itself — no extra API needed.

Usage:
  python server.py                  # run directly
  claude mcp add hinglishreach python /path/to/server.py
"""

import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
import meta_client as meta

load_dotenv()

mcp = FastMCP(
    "HinglishReach",
    instructions=(
        "You are a social media campaign assistant for Indian e-commerce brands. "
        "Use these tools to fetch audience data from Facebook and Instagram, then "
        "generate brand-specific campaigns in Hinglish (Hindi-English mix). "
        "Always fetch audience insights before generating campaign content so you "
        "can tailor the language, tone, and references to the actual audience. "
        "When generating captions: write naturally in Hinglish — mix Hindi and English "
        "the way real Indians speak. Include relevant hashtags (mix of Hindi and English). "
        "Keep CTAs direct and conversational."
    ),
)


@mcp.tool()
def list_connected_accounts() -> dict:
    """
    List all Facebook Pages and Instagram Business accounts connected to your Meta access token.
    Call this first to get the page_id and ig_user_id values needed for other tools.
    """
    return meta.list_connected_accounts()


@mcp.tool()
def get_facebook_insights(page_id: str) -> dict:
    """
    Get audience demographics and weekly engagement metrics for a Facebook Page.

    Args:
        page_id: The Facebook Page ID (get this from list_connected_accounts)

    Returns audience breakdown by gender, age, city, country plus engagement metrics
    like reach, impressions, page likes, and weekly post engagements.

    Note: Demographic data has a 48-hour reporting lag. Requires 100+ page followers.
    """
    return meta.get_facebook_insights(page_id)


@mcp.tool()
def get_instagram_insights(ig_user_id: str) -> dict:
    """
    Get audience demographics and weekly engagement metrics for an Instagram Business account.

    Args:
        ig_user_id: The Instagram user ID (get this from list_connected_accounts)

    Returns follower breakdown by age, gender, city, country plus weekly reach,
    impressions, and profile views.

    Note: Demographic data has a 48-hour reporting lag. Requires 100+ followers.
    """
    return meta.get_instagram_insights(ig_user_id)


@mcp.tool()
def publish_to_facebook(page_id: str, message: str, image_url: str = "") -> dict:
    """
    Publish a post to a Facebook Page Feed.

    Args:
        page_id:   Facebook Page ID (from list_connected_accounts)
        message:   The post caption — write in Hinglish with hashtags included
        image_url: Optional. A publicly accessible image URL to attach to the post.
                   Leave empty for a text-only post.

    Returns the published post ID on success.

    Limitation: Reels and Stories cannot be published via the Meta API.
    """
    return meta.publish_to_facebook(
        page_id=page_id,
        message=message,
        image_url=image_url or None,
    )


@mcp.tool()
def publish_to_instagram(ig_user_id: str, caption: str, image_url: str) -> dict:
    """
    Publish an image post to an Instagram Business account Feed.

    Args:
        ig_user_id: Instagram user ID (from list_connected_accounts)
        caption:    Post caption — write in Hinglish with hashtags included
        image_url:  A publicly accessible image URL. Instagram fetches this server-side,
                    so the URL must be reachable from the internet (not localhost).

    Returns the published media ID on success.

    Limitation: Reels and Stories cannot be published via the Meta API.
    """
    return meta.publish_to_instagram(
        ig_user_id=ig_user_id,
        image_url=image_url,
        caption=caption,
    )


if __name__ == "__main__":
    mcp.run()
