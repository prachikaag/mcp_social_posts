# HinglishReach

**AI-powered Hinglish social media campaign generator for Indian e-commerce brands**

Enter a keyword → get a ready-to-post Facebook and Instagram campaign in Hindi-English (Hinglish), tailored to your brand, audience, and products.

---

## Overview

HinglishReach is a Python/FastAPI web app that connects to your Facebook Page and Instagram Business account, reads your audience insights, and uses Claude AI to generate brand-specific social media campaigns in Hinglish — the natural mix of Hindi and English spoken by hundreds of millions of Indian consumers.

**Who it's for:** Indian e-commerce brands, D2C sellers, and online stores targeting Hindi-speaking audiences on Instagram and Facebook.

**How it works:**
1. You connect your Facebook Page and Instagram Business account via OAuth
2. You enter a keyword (e.g. "summer sale", "new collection", "festive offer")
3. You describe your brand, products, and target audience
4. Claude AI generates Hinglish captions, hashtags, and a call-to-action
5. Preview and publish directly to your social accounts — or copy and post manually

---

## Features

- **Keyword-based campaign generation** — one keyword produces a full campaign brief
- **Hinglish content** — Claude AI writes in natural Hindi-English mix, tuned for Indian audiences
- **Meta account integration** — connect your Facebook Page and Instagram Business account via Meta OAuth 2.0
- **Audience insights** — pulls basic demographics (age, gender, top cities) and engagement metrics from your connected accounts
- **Brand customisation** — set your brand name, product category, niche, tone, and target audience description
- **Campaign preview** — review the generated content before publishing
- **One-click publishing** — post directly to Facebook Page Feed and Instagram Feed
- **Suggested image prompts** — get an AI-generated prompt to create visuals for each post

> **Note on API limitations:**
> - Reels and Stories **cannot** be published via the Meta API — feed posts only
> - Audience demographic data has a **48-hour reporting lag**
> - Demographic insights require **100+ followers** on the connected account
> - Granular behavioral/interest targeting data is not available (Meta restriction post-2018)

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.11+ + FastAPI |
| AI Engine | Claude API (`claude-sonnet-4-6`) via Anthropic SDK |
| Social Media API | Meta Graph API v22.0 (Facebook + Instagram) |
| Frontend | React (production) / Jinja2 templates (MVP) |
| Auth | Meta OAuth 2.0 |
| Database | SQLite (development) / PostgreSQL (production) |

---

## Architecture

```
User Browser
     │
     ▼
FastAPI Backend
     ├──► Claude API (Anthropic)       ← generates Hinglish campaign content
     └──► Meta Graph API               ← reads audience data, publishes posts
               ├── Facebook Page API
               └── Instagram Graph API
```

---

## What This App Can and Cannot Do

| Capability | Status |
|---|---|
| Publish image/video/carousel posts to Facebook Page Feed | ✅ Supported |
| Publish image/video/carousel posts to Instagram Feed | ✅ Supported |
| Read audience demographics (age, gender, location, top cities) | ✅ Supported |
| Read engagement metrics (likes, comments, reach, impressions) | ✅ Supported |
| Publish Reels | ❌ Not supported by Meta API |
| Publish Stories | ❌ Not supported by Meta API |
| Real-time demographic data | ❌ 48-hour lag |
| Accounts with fewer than 100 followers | ❌ No demographic data available |
| Granular behavioral/interest audience data | ❌ Removed by Meta post-Cambridge Analytica (2018) |

---

## Meta Developer Setup

You need a Meta Developer account and a Facebook App before running this project. Follow these steps:

### 1. Create a Meta Developer Account
- Go to [developers.facebook.com](https://developers.facebook.com)
- Log in with your Facebook account and register as a developer

### 2. Create a New App
- Click **My Apps → Create App**
- Select **Business** as the app type
- Fill in your app name and contact email

### 3. Add Required Products
In your app dashboard, add the following products:
- **Facebook Login** — for OAuth user authentication
- **Instagram Graph API** — for Instagram Business account access

### 4. Configure OAuth Redirect URI
- Go to **Facebook Login → Settings**
- Add your redirect URI (e.g. `http://localhost:8000/auth/callback` for local dev)

### 5. Required OAuth Scopes / Permissions
Your app will request the following permissions from users:

```
instagram_business_basic
instagram_business_content_publish
pages_manage_posts
pages_read_engagement
pages_show_list
```

### 6. Switch to Live Mode
- The app starts in **Development mode** (only accessible to app admins/testers)
- To let real users connect their accounts, submit for **Meta App Review** and switch to **Live mode**
- Meta will review your use of each permission — prepare a screencast demo of your app

### 7. Get Your App Credentials
From **App Settings → Basic**, note your:
- `App ID` → `META_APP_ID`
- `App Secret` → `META_APP_SECRET`

---

## User Flow

```
1. Connect Account
   └── User logs in via Meta OAuth → grants permissions for Facebook Page + Instagram

2. Audience Insights (auto-fetched)
   └── App reads: top age groups, gender split, top cities, recent engagement metrics

3. Campaign Input
   └── User enters:
         • Keyword (e.g. "Eid sale", "monsoon collection")
         • Brand name
         • Product category (e.g. ethnic wear, skincare, electronics)
         • Target audience description (e.g. "women 25-40, tier-2 cities, budget-conscious")
         • Tone preference (e.g. festive, urgent, warm, playful)

4. AI Generation (Claude API)
   └── Generates:
         • Hinglish caption (2-3 paragraphs)
         • Hashtags (mix of Hindi and English tags)
         • Call-to-action line
         • Suggested image/creative prompt

5. Preview & Publish
   └── User reviews content → publishes to Facebook and/or Instagram, or copies manually
```

---

## Local Setup

### Prerequisites
- Python 3.11+
- A Meta Developer App (see setup above)
- An Anthropic API key ([console.anthropic.com](https://console.anthropic.com))

### Installation

```bash
git clone https://github.com/prachikaag/mcp_social_posts.git
cd mcp_social_posts
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root:

```env
ANTHROPIC_API_KEY=your_anthropic_api_key
META_APP_ID=your_meta_app_id
META_APP_SECRET=your_meta_app_secret
META_REDIRECT_URI=http://localhost:8000/auth/callback
```

### Run the App

```bash
uvicorn main:app --reload
```

Open [http://localhost:8000](http://localhost:8000) in your browser.

---

## Roadmap

| Version | Milestone |
|---|---|
| v0.1 | README + project structure |
| v0.2 | Meta OAuth integration (Facebook + Instagram login) |
| v0.3 | Audience insights dashboard |
| v0.4 | Claude API Hinglish content generation |
| v0.5 | Campaign preview UI |
| v0.6 | One-click publishing to Facebook and Instagram Feed |
| v1.0 | Campaign scheduler + post history |

---

## Contributing

This project is in early planning. Contributions, feedback, and ideas are welcome — open an issue or pull request.

---

## License

MIT
