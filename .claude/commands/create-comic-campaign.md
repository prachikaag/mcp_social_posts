# Skill: Create Comic Campaign (Full Story Series)

Create a complete multi-post storytelling comic campaign for Miraya.
Produces a series of 3–5 story posts — each a different everyday woman, a different
chapter of her life — united by one campaign theme and one cohesive art direction.

**Always reads `art_style.md` and `CLAUDE.md` before generating anything.**
**Always outputs as DRAFT. Never publishes without explicit user confirmation.**

---

## When to Use This Skill

Use when you want a full campaign series — not a single post.
For a single story post, use `/create-story-post` instead.

Example triggers:
- `/create-comic-campaign Durga Puja — women who celebrate quietly`
- `/create-comic-campaign summer collection — everyday women, real moments`
- `/create-comic-campaign Women's Day — for every woman who carries the world`

---

## Inputs

- **Campaign theme** — the unifying emotional thread across all posts
- **Number of posts in series** — default: 3 posts (can be 3–5)
- **Colour palette** — read from `art_style.md`; same palette used across ALL posts in series
- **Character archetypes** — each post features a different archetype (A, B, C, D)
  so the series feels like a universe of real women, not one woman repeated

---

## Full Pipeline

### Step 0 — Load Art Direction
Read `art_style.md` fully. Note:
- Carousel cohesion rules (ONE palette for the whole series)
- Emotional arc structure
- Character archetypes
- Base image generation prompt
- Approved taglines

Read `CLAUDE.md` fully. Note:
- Products to feature
- CTA rules (DM/store only)
- Brand voice and Hinglish guidelines

### Step 1 — Research the Campaign Theme
Run `web_search`:
- `"[campaign theme] Indian women relatable content 2025"`
- `"[campaign theme] women emotional storytelling Instagram India"`
- `search_news` for any cultural moment or timing hook

Identify:
- The emotional truth at the core of this theme for Indian women
- Any cultural reference, phrase, or moment that makes it instantly recognisable
- Why NOW is the right time for this campaign

### Step 2 — Research Hashtags
Run `web_search`:
- `"[campaign theme] Indian women Instagram hashtags 2025"`
- `"womenofinstagram ethnic wear storytelling hashtags"`
- Standard Miraya hashtag base from `CLAUDE.md`

Build the cohesive hashtag set for the series (same base set across all 3 posts,
with 2–3 post-specific tags per post).

### Step 3 — Design the Series Structure

Map out the 3-post series:

| Post | Character | Story Title | Core Emotion | Panel Count |
|---|---|---|---|---|
| Post 1 | Archetype [A/B/C/D] | [title] | [emotion] | 5 |
| Post 2 | Archetype [A/B/C/D] | [title] | [emotion] | 5 |
| Post 3 | Archetype [A/B/C/D] | [title] | [emotion] | 5 |

Each post must feel complete alone, but together they build a universe.

**Palette lock:** Confirm ONE palette from `art_style.md` for the whole series
and state it clearly before generating any prompts.

### Step 4 — Generate Each Post

For each post in the series, follow the full `/create-story-post` pipeline:
- Write the 5-panel story arc
- Write panel narration text (Hinglish, max 10 words per panel)
- Generate all 5 image prompts (using base prompt from `art_style.md`)
- Write the Instagram carousel caption
- Write the Facebook caption variant

### Step 5 — Series Overview & Posting Schedule

After all 3 posts, produce a series summary:
- Campaign name
- The emotional thread connecting all 3 posts
- Recommended posting schedule (1 post every 2–3 days for maximum impact)
- Series hashtag (e.g., `#WohHarRozKiLadki`) to use across all posts
- Suggested Stories or Reels concept to amplify the series

---

## Output Format

---

## MIRAYA COMIC CAMPAIGN — DRAFT SERIES

> **Status: DRAFT — Not Posted**
> **Campaign Theme:** [theme]
> **Series Length:** [n] posts
> **Art Style:** Woh Har Roz Ki Ladki — Warm Caricature Comic
> **Colour Palette (ALL posts):** [Palette Name] — [hex codes]
> **Series Hashtag:** #[CampaignHashtag]

---

### Campaign Insight
*[2–3 lines on the emotional truth driving this campaign — why it will resonate
with Miraya's audience of women 20–45 in Siliguri / North Bengal]*

---

### POST 1 OF [N]

**Character:** [Archetype — brief description]
**Story Title:** "[title]"
**Core Emotion:** [word]

#### Panel Breakdown
[5 panels as per /create-story-post format]

#### Image Generation Prompts
[All 5 panel prompts — complete, ready to paste into Canva/Midjourney/DALL-E]

#### Instagram Carousel Caption
[Full caption with hashtags]

#### Facebook Caption
[Variant]

---

### POST 2 OF [N]
[Same structure]

---

### POST 3 OF [N]
[Same structure]

---

### Series Posting Schedule

| Date | Post | Character | Best Time |
|---|---|---|---|
| Day 1 | Post 1 | [archetype] | [time] IST |
| Day 3 | Post 2 | [archetype] | [time] IST |
| Day 6 | Post 3 | [archetype] | [time] IST |

**Recommendation:** Space posts 2–3 days apart. Use Stories between posts to tease
the next character — "Kal miloge isse?" (Meet her tomorrow?)

### Series Amplification Ideas
- Ask followers to tag a woman who fits each archetype ("Tag karein apni woh friend!")
- Create a "Which woman are you?" poll in Stories
- Behind-the-scenes of the illustration process (if applicable)
- User-generated: ask followers to share their own "5am moment"

---

After showing the full draft, ask:
> "Poori series kaisi lagi? 💛
> Main kar sakta hoon:
> - Koi bhi post ka panel ya caption edit karna
> - Ek naya character add karna (4th post)
> - Posting schedule adjust karna
> - Ek ek karke post karna jab aap ready ho"

**Do NOT publish any post until explicitly confirmed for that specific post.**
