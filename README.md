# HinglishReach MCP Server

**An MCP (Model Context Protocol) server that lets Claude manage your Facebook and Instagram social media campaigns in Hinglish.**

Instead of a web app, you talk to Claude directly:
> *"Create a campaign for my ethnic wear brand, keyword: Eid sale, target women 25-40 in tier-2 cities"*

Claude fetches your audience insights, writes the Hinglish caption, hashtags, and CTA — then posts to your Facebook Page and Instagram Feed.

---

## What is MCP?

Model Context Protocol (MCP) is an open standard that lets Claude use external tools — like calling APIs, reading databases, or posting to social media — directly from conversation. This server exposes your Meta (Facebook + Instagram) account as tools Claude can use.

No web frontend. No forms. Just conversation.

---

## How It Works

```
You (talking to Claude Code or Claude Desktop)
          │
          ▼
    Claude (AI reasoning + Hinglish content generation)
          │  calls MCP tools
          ▼
  HinglishReach MCP Server (Python)
          │
          ▼
    Meta Graph API
      ├── Facebook Page API  → read insights, publish posts
      └── Instagram Graph API → read insights, publish posts
```

---

## Tools Claude Gets

| Tool | What it does |
|---|---|
| `list_connected_accounts` | Lists your connected Facebook Pages and Instagram Business accounts |
| `get_facebook_insights` | Fetches audience demographics + engagement from your Facebook Page |
| `get_instagram_insights` | Fetches audience demographics + engagement from your Instagram account |
| `publish_to_facebook` | Posts a caption (+ optional image) to your Facebook Page Feed |
| `publish_to_instagram` | Posts a caption + image to your Instagram Feed |

Claude handles everything else — generating Hinglish captions, hashtags, CTAs, and image prompts — using its own intelligence, no extra API calls needed.

---

## Example Conversation

```
You:  Create a festive campaign for my saree brand.
      Keyword: Navratri collection. My audience is women 25-45, Gujarat and Rajasthan.

Claude: Let me pull your audience insights first...
        [calls get_instagram_insights]
        [calls get_facebook_insights]

        Here's your campaign:

        Caption (Hinglish):
        "Ye Navratri, apni favourite saree mein celebrate karo! ✨
        Our new Navratri Collection has arrived — vibrant colours,
        premium silk, perfect for every garba night.
        Limited pieces — order karo aaj hi! 🙏🏽"

        Hashtags: #NavratriCollection #SareeLove #EthnicWear
                  #NavratriSpecial #GarbaLook #IndianFashion

        CTA: "Shop now — link in bio!"

        Image prompt: "Woman in bright red-orange silk saree dancing garba,
        warm festive lighting, traditional jewellery, joyful expression"

        Should I post this to Instagram and Facebook, or do you want to edit first?

You:  Change the CTA to "DM us to order" and post it.

Claude: [calls publish_to_instagram]
        [calls publish_to_facebook]
        Done! Posted to both accounts.
```

---

## What This Can and Cannot Do

| Capability | Status |
|---|---|
| Post images/videos/carousels to Facebook Page Feed | ✅ |
| Post images/videos/carousels to Instagram Feed | ✅ |
| Read audience demographics (age, gender, top cities) | ✅ |
| Read engagement metrics (likes, comments, reach, impressions) | ✅ |
| Generate Hinglish captions, hashtags, CTAs | ✅ (Claude does this) |
| Publish Reels or Stories | ❌ Meta API limitation |
| Real-time demographics | ❌ 48-hour lag (Meta limitation) |
| Accounts with fewer than 100 followers | ❌ No demographic data |
| Granular interest/behavioral targeting data | ❌ Removed by Meta post-2018 |

---

## Setup

### Prerequisites
- Python 3.11+
- Claude Desktop or Claude Code (to use the MCP server)
- A Meta Developer account + Facebook App (see below)

### 1. Clone and install

```bash
git clone https://github.com/prachikaag/mcp_social_posts.git
cd mcp_social_posts
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Set up Meta Developer App (one-time)

You need a Meta App to call the Graph API. Follow these steps:

1. Go to [developers.facebook.com](https://developers.facebook.com) and register
2. Click **My Apps → Create App → Business**
3. Add products: **Facebook Login** + **Instagram Graph API**
4. Under **Facebook Login → Settings**, add redirect URI: `http://localhost:8888/callback`
5. Note your **App ID** and **App Secret** from **App Settings → Basic**

Required OAuth permissions:
```
instagram_business_basic
instagram_business_content_publish
pages_manage_posts
pages_read_engagement
pages_show_list
```

### 3. Get your access token (one-time)

Run the included helper script — it opens a browser, walks you through Meta OAuth, and saves a long-lived token to your `.env` file:

```bash
python auth_setup.py
```

This only needs to be done once. The token lasts ~60 days and can be refreshed.

### 4. Configure environment

Copy `.env.example` to `.env` and fill in your values:

```bash
cp .env.example .env
```

```env
META_APP_ID=your_app_id
META_APP_SECRET=your_app_secret
META_ACCESS_TOKEN=your_long_lived_token   # filled by auth_setup.py
```

### 5. Register with Claude Desktop

Add the server to your Claude Desktop config (`~/Library/Application Support/Claude/claude_desktop_config.json` on Mac):

```json
{
  "mcpServers": {
    "hinglishreach": {
      "command": "python",
      "args": ["/absolute/path/to/mcp_social_posts/server.py"],
      "env": {
        "META_APP_ID": "your_app_id",
        "META_APP_SECRET": "your_app_secret",
        "META_ACCESS_TOKEN": "your_long_lived_token"
      }
    }
  }
}
```

Or if using Claude Code, run:

```bash
claude mcp add hinglishreach python /absolute/path/to/mcp_social_posts/server.py
```

### 6. Start using it

Open Claude Desktop or Claude Code and start talking:

> *"What does my Instagram audience look like this week?"*
> *"Create a Hinglish Diwali campaign for my skincare brand and post it."*

---

## Project Structure

```
mcp_social_posts/
├── server.py          # MCP server — defines all tools Claude can call
├── meta_client.py     # Meta Graph API wrapper (insights + publishing)
├── auth_setup.py      # One-time OAuth helper to get your access token
├── requirements.txt
├── .env.example
└── README.md
```

---

## Roadmap

| Version | Milestone |
|---|---|
| v0.1 | README + project structure |
| v0.2 | Meta OAuth token helper (`auth_setup.py`) |
| v0.3 | Meta Graph API client (insights + publishing) |
| v0.4 | MCP server with all tools |
| v0.5 | Hinglish campaign prompts + Claude integration |
| v1.0 | Multi-account support + campaign history |

---

## License

MIT
