# Miraya Social Media Agent

**An MCP server + agentic pipeline that runs Miraya's entire social media operation from conversation.**

Miraya is a women's ethnic wear brand in Siliguri, West Bengal. This system lets Claude:
- Research your audience, competitors, and trends
- Generate Hinglish campaigns and storytelling comic posts
- Create Canva-ready design visuals
- Publish directly to Facebook and Instagram — always as a draft first, never auto-posted

No forms. No dashboards. Just talk to Claude.

---

## How It Works

```
You (Claude Code or Claude Desktop)
          │
          ▼
    Claude — reads CLAUDE.md + art_style.md for brand context
          │  invokes skills and agents
          ▼
  Miraya MCP Server (server.py)
    ├── Meta Graph API     → audience insights + publishing
    └── Web Search (DDG)   → competitor research, trends, hashtags
          │
          ▼
    Campaign Draft → you review → "post it" → published
```

---

## Two Campaign Modes

### 1. Product Campaigns (`/run-campaign`)
Keyword-driven. Researches trends, writes Hinglish caption + hashtags + image prompt.

```
/run-campaign cotton kurta
/run-campaign Durga Puja collection
/run-campaign spring summer vibrant Indian textiles
```

### 2. Story Campaigns (`/create-story-post`, `/create-comic-campaign`)
Caricature comic posts — the *"Woh Har Roz Ki Ladki"* series. Shows everyday Indian women
(the Young Mother, the Working Woman, the Elder Sister, the Woman of the House) in their
real daily lives, and how Miraya fits into those moments. Deeply emotional, highly shareable.

```
/create-story-post morning routine
/create-comic-campaign Durga Puja — women who celebrate quietly
/create-comic-campaign spring summer — everyday moments --posts 3
```

---

## Available Skills

### Research
| Command | What it does |
|---|---|
| `/fetch-audience-insights` | Live Instagram + Facebook demographics and engagement |
| `/fetch-competitor-insights` | Researches @alamode_slg and @trendxmastani — gaps and opportunities |
| `/fetch-trending-posts [keyword]` | Trending content for a keyword on Instagram India |
| `/understand-trending` | Why something is trending — emotion, lifecycle, brand angle |
| `/research-topic` | Deep topic brief before writing any campaign content |

### Campaign Creation
| Command | What it does |
|---|---|
| `/create-campaign` | Hinglish product campaign — caption, researched hashtags, image prompt |
| `/create-story-post` | Single 5-panel "Woh Har Roz Ki Ladki" comic carousel |
| `/create-comic-campaign` | Full 3–5 post story series, different archetypes, cohesive palette |

### Orchestration
| Command | What it does |
|---|---|
| `/run-campaign [keyword]` | Full pipeline: insights → competitors → trends → research → draft |

---

## Standalone Python Agents

Run outside Claude Code — useful for batch generation or automation:

```bash
# Product campaign agent
python agent.py "cotton kurta"
python agent.py "Durga Puja collection"

# Story / comic campaign agent
python story_agent.py "spring summer — everyday moments"
python story_agent.py "Durga Puja — women who celebrate quietly" --posts 3
```

---

## Visual Design System

All image generation is governed by `art_style.md` — read before any design task.

**Primary style:** *Desi Glow* — warm watercolour caricature, Amul-inspired bold outlines,
expressive faces, real Indian women (diverse body types, skin tones, ages 20–45).

**4 approved colour palettes** — one locked per carousel, never mixed:

| Palette | Use for | Primary colour |
|---|---|---|
| Coral Dawn | Spring / summer / new arrivals | `#E8603C` coral |
| Teal Heritage | Handcraft / artisan stories | `#2EC4B6` turquoise |
| Bengali Gold | Durga Puja / festive | `#E9C46A` marigold |
| Monsoon Soft | Everyday / emotional storytelling | `#386641` forest green |

**4 story character archetypes** (defined in `art_style.md`):
- The Young Mother — messy bun, toddler at her feet, warm smile
- The Working Woman — dupatta half-tucked, rushing between two worlds
- The Elder Sister — quiet strength, responsible beyond her years
- The Woman of the House — the one everyone depends on, always last to eat

**Emotional arc** (same in every story post):
> Reality → she carries so much → barely time for herself → Miraya → she glows

Image prompts from `art_style.md` are ready to paste into **Canva AI, Midjourney, DALL-E 3, or Adobe Firefly**.

---

## What This Can and Cannot Do

| Capability | Status |
|---|---|
| Publish image/video/carousel posts to Facebook Page Feed | ✅ |
| Publish image/video/carousel posts to Instagram Feed | ✅ |
| Read audience demographics (age, gender, top cities) | ✅ |
| Read engagement metrics (reach, impressions, likes, comments) | ✅ |
| Generate Hinglish captions, hashtags, CTAs | ✅ Claude does this |
| Research competitors and trending content | ✅ Via DuckDuckGo search |
| Generate Canva / Midjourney image prompts | ✅ Via art_style.md |
| Always output as draft first | ✅ Hard rule — never auto-publishes |
| Publish Reels or Stories | ❌ Meta API limitation |
| Real-time demographic data | ❌ 48-hour lag (Meta limitation) |
| Accounts under 100 followers | ❌ No demographic data |
| Granular interest/behavioral targeting | ❌ Removed by Meta post-2018 |

---

## Setup

### Prerequisites
- Python 3.11+
- Claude Desktop or Claude Code
- A Meta Developer App (one-time setup — see below)
- Anthropic API key (for standalone agents)

### 1. Clone and install

```bash
git clone https://github.com/prachikaag/mcp_social_posts.git
cd mcp_social_posts
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Set up Meta Developer App (one-time)

1. Go to [developers.facebook.com](https://developers.facebook.com) → **My Apps → Create App → Business**
2. Add products: **Facebook Login** + **Instagram Graph API**
3. Under **Facebook Login → Settings**, add redirect URI: `http://localhost:8888/callback`
4. Note your **App ID** and **App Secret** from **App Settings → Basic**

Required OAuth permissions:
```
instagram_business_basic
instagram_business_content_publish
pages_manage_posts
pages_read_engagement
pages_show_list
```

### 3. Get your access token (one-time)

```bash
python auth_setup.py
```

Opens a browser, walks you through Meta OAuth, and saves a long-lived token (~60 days) to `.env` automatically.

### 4. Configure environment

```bash
cp .env.example .env
```

```env
META_APP_ID=your_app_id
META_APP_SECRET=your_app_secret
META_ACCESS_TOKEN=your_long_lived_token   # auto-filled by auth_setup.py
ANTHROPIC_API_KEY=your_anthropic_api_key  # needed for standalone agents
```

After setup, add your Facebook Page ID and Instagram User ID to `CLAUDE.md` (Connected Meta Accounts section).

### 5. Register with Claude Desktop

**Mac** — edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "miraya": {
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

**Claude Code:**

```bash
claude mcp add miraya python /absolute/path/to/mcp_social_posts/server.py
```

### 6. Fill in your brand details

Open `CLAUDE.md` and complete:
- Products & Pricing Guide (add price ranges)
- Connected Meta Accounts (Page ID + IG User ID from `auth_setup.py`)
- Inspiration Brands (3–5 handles of brands whose style you admire)

Open `art_style.md` if you want to adjust character archetypes or colour palettes.

---

## Project Structure

```
mcp_social_posts/
│
├── CLAUDE.md                     # Brand context — read by every agent and skill
├── art_style.md                  # Visual style guide — read before any image task
│
├── server.py                     # MCP server (Meta API + web search tools)
├── meta_client.py                # Meta Graph API v22.0 wrapper
├── web_search.py                 # DuckDuckGo search wrapper (no API key needed)
├── auth_setup.py                 # One-time OAuth helper → saves token to .env
│
├── agent.py                      # Standalone product campaign agent (Anthropic SDK)
├── story_agent.py                # Standalone story/comic campaign agent
│
├── requirements.txt              # mcp, httpx, anthropic, duckduckgo-search, python-dotenv
├── .env.example                  # Environment variable template
│
└── .claude/
    └── commands/                 # Slash command skills
        ├── run-campaign.md           # /run-campaign — full automated pipeline
        ├── create-campaign.md        # /create-campaign — product campaign draft
        ├── create-story-post.md      # /create-story-post — single comic story post
        ├── create-comic-campaign.md  # /create-comic-campaign — full story series
        ├── fetch-audience-insights.md
        ├── fetch-competitor-insights.md
        ├── fetch-trending-posts.md
        ├── understand-trending.md
        └── research-topic.md
```

---

## Campaign Rules (Always Applied)

These are enforced by every skill, agent, and the MCP server:

1. **Always DRAFT first.** Never publishes without `"post it"` / `"publish"` / `"go ahead"` from you.
2. **Always Hinglish.** Natural Hindi-English mix — not translated, genuinely spoken.
3. **Always research hashtags.** Web search before every post. No guessing.
4. **CTAs = DM or store visit only.** Miraya has no website. Never use "shop now" with a link.
5. **Always include an image prompt.** Product posts use `art_style.md` palette. Story posts use the base caricature prompt.
6. **Never invent prices.** Only prices from `CLAUDE.md` Products & Pricing Guide.
7. **One palette per carousel.** Enforced by `art_style.md` cohesion rules.

---

## Roadmap

| Version | Milestone | Status |
|---|---|---|
| v0.1 | Project structure + README | ✅ Done |
| v0.2 | Meta OAuth token helper | ✅ Done |
| v0.3 | Meta Graph API client | ✅ Done |
| v0.4 | MCP server with Meta + web search tools | ✅ Done |
| v0.5 | Product campaign agent + 9 skills | ✅ Done |
| v0.6 | Story/comic campaign system + art_style.md | ✅ Done |
| v1.0 | Campaign scheduler + post history | Planned |
| v1.1 | Multi-account support | Planned |

---

## License

MIT
