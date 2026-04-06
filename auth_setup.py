"""
One-time Meta OAuth setup script.

Run this once to get your long-lived Facebook/Instagram access token.
It will:
  1. Open a browser for you to log in to Facebook and grant permissions
  2. Exchange the short-lived code for a long-lived token (~60 days)
  3. Save the token to your .env file automatically

Usage:
  python auth_setup.py

Prerequisites:
  - META_APP_ID and META_APP_SECRET must be set in .env
  - Your Meta App must have redirect URI http://localhost:8888/callback configured
    (Facebook Login → Settings → Valid OAuth Redirect URIs)
"""

import os
import sys
import webbrowser
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
import httpx
from dotenv import load_dotenv, set_key

load_dotenv()

APP_ID = os.environ.get("META_APP_ID", "")
APP_SECRET = os.environ.get("META_APP_SECRET", "")
REDIRECT_URI = "http://localhost:8888/callback"
ENV_FILE = os.path.join(os.path.dirname(__file__), ".env")

SCOPES = [
    "instagram_business_basic",
    "instagram_business_content_publish",
    "pages_manage_posts",
    "pages_read_engagement",
    "pages_show_list",
    "public_profile",
]

_auth_code: str | None = None


class _CallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global _auth_code
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        if "code" in params:
            _auth_code = params["code"][0]
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(
                b"<h2>Auth successful! You can close this tab and return to your terminal.</h2>"
            )
        else:
            error = params.get("error_description", ["Unknown error"])[0]
            self.send_response(400)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(f"<h2>Auth failed: {error}</h2>".encode())

    def log_message(self, *args):
        pass  # suppress request logs


def _exchange_for_short_lived_token(code: str) -> str:
    response = httpx.get(
        "https://graph.facebook.com/v22.0/oauth/access_token",
        params={
            "client_id": APP_ID,
            "redirect_uri": REDIRECT_URI,
            "client_secret": APP_SECRET,
            "code": code,
        },
        timeout=15,
    )
    response.raise_for_status()
    return response.json()["access_token"]


def _exchange_for_long_lived_token(short_token: str) -> str:
    response = httpx.get(
        "https://graph.facebook.com/v22.0/oauth/access_token",
        params={
            "grant_type": "fb_exchange_token",
            "client_id": APP_ID,
            "client_secret": APP_SECRET,
            "fb_exchange_token": short_token,
        },
        timeout=15,
    )
    response.raise_for_status()
    data = response.json()
    token = data["access_token"]
    expires_in = data.get("expires_in", "unknown")
    print(f"Long-lived token obtained. Expires in: {expires_in} seconds (~60 days).")
    return token


def main():
    if not APP_ID or not APP_SECRET:
        print(
            "ERROR: META_APP_ID and META_APP_SECRET must be set in your .env file.\n"
            "Copy .env.example to .env and fill in your Meta App credentials."
        )
        sys.exit(1)

    auth_url = (
        "https://www.facebook.com/dialog/oauth?"
        + urllib.parse.urlencode(
            {
                "client_id": APP_ID,
                "redirect_uri": REDIRECT_URI,
                "scope": ",".join(SCOPES),
                "response_type": "code",
            }
        )
    )

    print("Opening browser for Facebook login...")
    print(f"\nIf the browser doesn't open, visit this URL:\n{auth_url}\n")
    webbrowser.open(auth_url)

    print("Waiting for OAuth callback on http://localhost:8888/callback ...")
    server = HTTPServer(("localhost", 8888), _CallbackHandler)
    server.handle_request()  # handle exactly one request then stop

    if not _auth_code:
        print("ERROR: Did not receive an auth code. Check your Meta App redirect URI settings.")
        sys.exit(1)

    print("Auth code received. Exchanging for access token...")
    short_token = _exchange_for_short_lived_token(_auth_code)
    long_token = _exchange_for_long_lived_token(short_token)

    # Save to .env
    if not os.path.exists(ENV_FILE):
        with open(ENV_FILE, "w") as f:
            f.write(f"META_APP_ID={APP_ID}\n")
            f.write(f"META_APP_SECRET={APP_SECRET}\n")
            f.write(f"META_ACCESS_TOKEN={long_token}\n")
    else:
        set_key(ENV_FILE, "META_ACCESS_TOKEN", long_token)

    print(f"\nSuccess! Token saved to {ENV_FILE}")
    print("\nYou're all set. Run your MCP server:")
    print("  python server.py\n")


if __name__ == "__main__":
    main()
