# Skill: Fetch Trending Posts with Target Keyword

Find what content is currently trending around a keyword on Instagram and
the broader Indian social media ecosystem — so Miraya campaigns ride momentum.

Reads brand context from CLAUDE.md. Keyword is the only input needed from the user.

---

## Input

**Keyword:** Read from the user's message or the `/run-campaign` call.
If not provided, ask: *"What keyword or theme should I search? e.g. 'cotton kurta', 'festive ethnic wear', 'Durga Puja outfit'"*

---

## Steps

1. Run these `web_search` calls:
   - `"[keyword] Instagram trending India [current month year]"`
   - `"[keyword] viral post Indian women fashion"`
   - `"[keyword] ethnic wear content ideas India"`
   - `"[keyword] Instagram hashtags India [current year]"`

2. Run `search_news`:
   - `"[keyword] India fashion trend [current month year]"`

3. Look for:
   - What **content formats** are leading (carousel, Reel, static, quote card)
   - What **emotions** are being triggered (nostalgia, aspiration, humour, pride)
   - What **language patterns** are popular (Hinglish phrases, Bengali references)
   - Which hashtags appear repeatedly across multiple sources

4. Filter for **Indian / North Bengal relevance** — prioritise content resonating
   with women in Siliguri and broader North Bengal / West Bengal.

5. Check recency — favour the last 14 days.

---

## Output Format

### Trending Posts Report — "[keyword]"
**Date:** [today's date]

#### What's Trending Right Now
- **Dominant content format:** [e.g., carousel "5 ways to style a cotton kurta"]
- **Tone of trending content:** [e.g., aspirational + relatable]
- **Language pattern:** [e.g., Hinglish captions, Bengali hashtags mixed in]

#### Top Hashtags Found
| Hashtag | Notes |
|---|---|
| #[tag] | [e.g., high volume, competitive] |
| #[tag] | [e.g., niche, good for local reach] |
| #[tag] | [e.g., trending this week] |

#### What Top Posts Are Doing
1. [e.g., "Strong first line hooks — 'Ye kurta dekh ke mom ne bhi order kar liya!'"]
2. [e.g., "Before/after styling posts getting high saves"]
3. [e.g., "Price mention in caption is driving DM enquiries"]

#### Relevance to Miraya
- **How this maps to our products:** [from CLAUDE.md product list]
- **Audience overlap:** [does this trend reach Miraya's 20-45 women in Siliguri?]
- **Cultural/local angle:** [any West Bengal or North Bengal hook?]
- **Risk:** [anything off-brand?]
