"""
Meta Graph API client.
Handles Facebook Page and Instagram Business account operations:
- Listing connected accounts
- Fetching audience insights and engagement metrics
- Publishing posts to Facebook Feed and Instagram Feed
"""

import os
import httpx
from typing import Any

GRAPH_API_BASE = "https://graph.facebook.com/v22.0"


def _token() -> str:
    token = os.environ.get("META_ACCESS_TOKEN", "")
    if not token:
        raise RuntimeError(
            "META_ACCESS_TOKEN is not set. Run auth_setup.py to generate your token."
        )
    return token


def _get(path: str, params: dict | None = None) -> dict:
    params = params or {}
    params["access_token"] = _token()
    response = httpx.get(f"{GRAPH_API_BASE}/{path}", params=params, timeout=15)
    response.raise_for_status()
    return response.json()


def _post(path: str, data: dict) -> dict:
    data["access_token"] = _token()
    response = httpx.post(f"{GRAPH_API_BASE}/{path}", data=data, timeout=15)
    response.raise_for_status()
    return response.json()


# ---------------------------------------------------------------------------
# Account discovery
# ---------------------------------------------------------------------------

def list_facebook_pages() -> list[dict]:
    """Return all Facebook Pages the user manages."""
    result = _get("me/accounts", {"fields": "id,name,category,followers_count"})
    return result.get("data", [])


def get_instagram_account(page_id: str) -> dict | None:
    """Return the Instagram Business account linked to a Facebook Page, or None."""
    result = _get(page_id, {"fields": "instagram_business_account{id,name,username,followers_count}"})
    return result.get("instagram_business_account")


def list_connected_accounts() -> dict:
    """
    Return all Facebook Pages and their linked Instagram Business accounts.
    This is the starting point — call this first to get IDs needed for other tools.
    """
    pages = list_facebook_pages()
    accounts: list[dict] = []
    for page in pages:
        ig = get_instagram_account(page["id"])
        accounts.append({
            "facebook_page_id": page["id"],
            "facebook_page_name": page["name"],
            "facebook_followers": page.get("followers_count"),
            "instagram_account_id": ig["id"] if ig else None,
            "instagram_username": ig.get("username") if ig else None,
            "instagram_followers": ig.get("followers_count") if ig else None,
        })
    return {"accounts": accounts}


# ---------------------------------------------------------------------------
# Audience insights
# ---------------------------------------------------------------------------

def get_facebook_insights(page_id: str) -> dict:
    """
    Fetch Facebook Page audience demographics and recent engagement.
    Note: demographic data has a 48-hour lag and requires 100+ followers.
    """
    # Page-level engagement metrics
    metrics = ",".join([
        "page_impressions_unique",
        "page_post_engagements",
        "page_fans",
        "page_fan_adds",
        "page_views_total",
    ])
    insights_result = _get(
        f"{page_id}/insights",
        {"metric": metrics, "period": "week"},
    )

    # Audience demographics
    demographics_result = _get(
        f"{page_id}/insights",
        {"metric": "page_fans_city,page_fans_country,page_fans_gender_age", "period": "lifetime"},
    )

    # Flatten into a readable dict
    engagement: dict[str, Any] = {}
    for item in insights_result.get("data", []):
        name = item["name"]
        values = item.get("values", [])
        engagement[name] = values[-1]["value"] if values else None

    demographics: dict[str, Any] = {}
    for item in demographics_result.get("data", []):
        demographics[item["name"]] = item.get("values", [{}])[-1].get("value")

    return {
        "platform": "facebook",
        "page_id": page_id,
        "weekly_engagement": engagement,
        "audience_demographics": demographics,
        "note": "Demographic data has a 48-hour reporting lag.",
    }


def get_instagram_insights(ig_user_id: str) -> dict:
    """
    Fetch Instagram Business account audience demographics and recent engagement.
    Note: demographic data has a 48-hour lag and requires 100+ followers.
    """
    # Account-level metrics
    metrics = "reach,impressions,profile_views,follower_count"
    insights_result = _get(
        f"{ig_user_id}/insights",
        {"metric": metrics, "period": "week", "metric_type": "total_value"},
    )

    # Audience breakdown
    audience_result = _get(
        f"{ig_user_id}/insights",
        {
            "metric": "follower_demographics",
            "period": "lifetime",
            "metric_type": "total_value",
            "breakdown": "age,city,country,gender",
        },
    )

    engagement: dict[str, Any] = {}
    for item in insights_result.get("data", []):
        engagement[item["name"]] = item.get("total_value", {}).get("value")

    demographics: dict[str, Any] = {}
    for item in audience_result.get("data", []):
        demographics[item["name"]] = item.get("total_value", {}).get("breakdowns", [])

    return {
        "platform": "instagram",
        "ig_user_id": ig_user_id,
        "weekly_engagement": engagement,
        "audience_demographics": demographics,
        "note": "Demographic data has a 48-hour reporting lag.",
    }


# ---------------------------------------------------------------------------
# Publishing
# ---------------------------------------------------------------------------

def publish_to_facebook(page_id: str, message: str, image_url: str | None = None) -> dict:
    """
    Publish a post to a Facebook Page Feed.
    Supports text-only or text + image. Carousels and Reels are not supported via API.
    Returns the created post ID.
    """
    # Get page-specific access token (required for publishing)
    page_info = _get(page_id, {"fields": "access_token"})
    page_token = page_info.get("access_token")
    if not page_token:
        raise RuntimeError(f"Could not retrieve page access token for page {page_id}.")

    if image_url:
        data = {
            "url": image_url,
            "caption": message,
            "access_token": page_token,
        }
        result = httpx.post(f"{GRAPH_API_BASE}/{page_id}/photos", data=data, timeout=15)
    else:
        data = {
            "message": message,
            "access_token": page_token,
        }
        result = httpx.post(f"{GRAPH_API_BASE}/{page_id}/feed", data=data, timeout=15)

    result.raise_for_status()
    return {"platform": "facebook", "page_id": page_id, "post_id": result.json().get("id"), "status": "published"}


def publish_to_instagram(ig_user_id: str, image_url: str, caption: str) -> dict:
    """
    Publish an image post to an Instagram Business account Feed.
    image_url must be a publicly accessible URL (Instagram fetches it server-side).
    Reels and Stories are not supported via the API.
    Returns the created media ID.
    """
    # Step 1: Create media container
    container = _post(
        f"{ig_user_id}/media",
        {"image_url": image_url, "caption": caption},
    )
    container_id = container.get("id")
    if not container_id:
        raise RuntimeError("Failed to create Instagram media container.")

    # Step 2: Publish the container
    publish_result = _post(
        f"{ig_user_id}/media_publish",
        {"creation_id": container_id},
    )
    return {
        "platform": "instagram",
        "ig_user_id": ig_user_id,
        "media_id": publish_result.get("id"),
        "status": "published",
    }
