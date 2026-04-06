# Skill: Run Full Campaign Agent

**Master orchestration skill.** Runs the complete campaign pipeline automatically —
from audience insights to competitor research to trending analysis to campaign draft —
with a single keyword input. No manual step-by-step needed.

All brand context is read from CLAUDE.md. The only input required is a keyword or theme.

---

## How to Invoke

```
/run-campaign [keyword or theme]
```

Examples:
- `/run-campaign cotton kurta`
- `/run-campaign Durga Puja collection`
- `/run-campaign summer ethnic wear`
- `/run-campaign handembroidered kurta`

---

## Full Agent Pipeline

Execute these steps **in order**, automatically, without stopping to ask the user
between steps (unless a critical decision point is reached). Show a brief status
line before each step so the user knows what's happening.

---

### Step 0 — Load Brand Context
Read CLAUDE.md fully. Note:
- Brand: Miraya, women's ethnic wear, Siliguri
- Instagram: @miraya_india
- Competitors: @alamode_slg, @trendxmastani
- Sales channel: store + DM only
- Target: women 20–45, Siliguri / North Bengal

---

### Step 1 — Fetch Audience Insights
*"Fetching Miraya's audience insights from Instagram and Facebook..."*

Call `get_instagram_insights` and `get_facebook_insights` using the IDs in CLAUDE.md.
If IDs are missing, call `list_connected_accounts` and note the IDs for the user to save.
Summarise the key audience signals in 3–4 bullet points (top age group, top cities, gender, engagement trend).

---

### Step 2 — Fetch Competitor Insights
*"Researching competitor brands @alamode_slg and @trendxmastani..."*

Run `web_search` for each competitor from the CLAUDE.md Competitor Brands section:
- `"@alamode_slg Instagram content ethnic wear Siliguri"`
- `"@trendxmastani Instagram fashion posts"`

Identify in 2–3 bullet points per competitor: what they're posting, their tone,
and the biggest gap Miraya can exploit for this keyword.

---

### Step 3 — Fetch Trending Posts
*"Finding what's trending for '[keyword]' on Instagram India..."*

Run `web_search`:
- `"[keyword] trending Instagram India [current month year]"`
- `"[keyword] viral posts Indian women fashion"`
- `"[keyword] Instagram hashtags India 2025"`

Run `search_news`:
- `"[keyword] India [current month year]"`

Summarise: dominant content format, top trending hashtags found, emotional tone of trending content.

---

### Step 4 — Understand Why It's Trending
*"Analysing the trend signal behind '[keyword]'..."*

Based on Step 3 results, identify:
- The trigger (festival, season, cultural moment, algorithm push)
- The core emotion (aspiration, pride, nostalgia, FOMO, belonging)
- Lifecycle stage (rising / peak / declining)
- The best angle for Miraya specifically

---

### Step 5 — Research the Topic
*"Researching the campaign topic in depth..."*

Run `web_search`:
- `"[keyword] women ethnic wear content ideas India"`
- `"[keyword] West Bengal / Siliguri culture or season relevance"`
- `"best Instagram captions [keyword] Indian fashion brand"`

Identify:
- Best-fit Miraya product(s) for this keyword (from CLAUDE.md)
- Fresh content angle not already saturated
- A cultural reference or Hinglish phrase that fits
- The key objection and how to pre-empt it

---

### Step 6 — Research Hashtags
*"Researching active hashtags for '[keyword]'..."*

Run `web_search`:
- `"best hashtags [keyword] Indian ethnic wear Instagram 2025"`
- `"Siliguri shopping fashion Instagram hashtags"`
- `"handmade kurta embroidery Instagram hashtags India"`

Build the hashtag set:
- 5–6 broad reach tags (#EthnicWear, #KurtaLove, #IndianFashion)
- 5–6 niche tags (#HandmadeKurta, #ChikankariFashion, #CottonKurta)
- 3–4 local tags (#SiliguriShopping, #SiliguriEthnic, #NorthBengalFashion)
- 2 brand tags (#Miraya, #MirayaIndia)
- 3–4 trending or seasonal tags (from Step 3 research)
- Total: 18–22 Instagram hashtags; pick 3–5 for Facebook

---

### Step 7 — Generate Campaign Draft
*"Creating the Hinglish campaign draft..."*

Using all context gathered in Steps 1–6, write:

**Instagram Caption** (Hinglish):
- Hook: scroll-stopping first line
- Body: 2–4 lines in Miraya's voice (handcraft, fabric, cultural pride)
- CTA: DM or store visit only (no website links)

**Facebook Caption** (slightly longer, 3–5 hashtags)

**Image / Creative Prompt** (detailed enough to brief a designer or AI tool)

**Posting time recommendation**

---

### Output

Present the full campaign draft using the CAMPAIGN DRAFT format from `/create-campaign`.

After the draft, ask:
> "Kaisa laga? Kuch edit karein, ya post kar dein? 😊
> I can: edit the caption, try a different angle, swap hashtags, or post to Instagram/Facebook."

**Do NOT publish until user explicitly confirms.**

---

## What's Automated vs What Needs You

| Step | Automated |
|---|---|
| Reading brand context | ✅ From CLAUDE.md |
| Fetching audience insights | ✅ Via Meta API tools |
| Competitor research | ✅ Via web search |
| Trending post research | ✅ Via web search |
| Hashtag research | ✅ Via web search |
| Topic research | ✅ Via web search |
| Campaign generation | ✅ Claude writes it |
| Publishing | ❌ User must confirm |
| Filling in prices | ❌ User must update CLAUDE.md |
| Inspiration brands | ❌ User must fill CLAUDE.md |
