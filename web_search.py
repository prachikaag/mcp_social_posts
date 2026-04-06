"""
Web search module using DuckDuckGo (no API key required).
Used by the MCP server and agent.py for competitor research,
trend discovery, hashtag research, and topic research.
"""

from duckduckgo_search import DDGS


def search(query: str, max_results: int = 6) -> list[dict]:
    """
    Run a web search and return results as a list of dicts with
    keys: title, url, snippet.
    """
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append({
                "title": r.get("title", ""),
                "url": r.get("href", ""),
                "snippet": r.get("body", ""),
            })
    return results


def search_news(query: str, max_results: int = 5) -> list[dict]:
    """Search news results — useful for trending topics and recent events."""
    results = []
    with DDGS() as ddgs:
        for r in ddgs.news(query, max_results=max_results):
            results.append({
                "title": r.get("title", ""),
                "url": r.get("url", ""),
                "snippet": r.get("body", ""),
                "date": r.get("date", ""),
                "source": r.get("source", ""),
            })
    return results
