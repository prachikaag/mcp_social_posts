# Skill: Fetch Trending Posts with Target Keyword

Find what content is currently trending around a keyword on Instagram,
Facebook, and broader social/web — so campaigns can ride existing momentum
rather than starting cold.

---

## Inputs Required

- **Keyword or topic** (ask the user if not provided)
- **Platform focus** — Instagram, Facebook, or both (default: both)
- **Niche context** — read from CLAUDE.md (product category, target audience)

If no keyword is provided, ask:
> "What keyword or topic should I search for trending content?
> For example: 'Navratri outfits', 'monsoon skincare', 'affordable ethnic wear'."

---

## Steps

1. **Web search for trending content around the keyword:**
   - `[keyword] trending Instagram [current month year]`
   - `[keyword] viral posts India [current month year]`
   - `[keyword] hashtag trending`
   - `[keyword] most liked posts`

2. **Search for related hashtags:**
   - `#[keyword] Instagram posts`
   - Look for hashtag volume indicators, related tags, niche sub-tags

3. **Search for trending formats:**
   - Is this keyword being used more in Reels, carousels, static images, or text posts?
   - Any meme formats, audio trends, or challenges attached to it?

4. **Look for Indian/regional angle:**
   - `[keyword] India social media trend`
   - `[keyword] Hinglish viral`
   - Any specific cities, festivals, or cultural moments attached to the keyword?

5. **Check recency** — prioritise content from the last 7-14 days.

---

## Output Format

### Trending Posts Report
**Keyword:** [keyword]
**Date:** [today's date]
**Platforms checked:** Instagram, Facebook, Web

---

#### What's Trending Right Now
- **Content format leading the trend:** [e.g., carousel, Reel, static image with text]
- **Tone of trending content:** [e.g., humorous, aspirational, informational, emotional]
- **Language pattern:** [e.g., mostly Hinglish, English captions with Hindi hashtags]

#### Top Trending Hashtags
| Hashtag | Approximate volume | Notes |
|---|---|---|
| #[tag] | [e.g., 2.3M posts] | [e.g., highly competitive] |
| #[tag] | | |
| #[tag] | | [e.g., niche, lower competition — good to own] |

#### What Top Posts Are Doing
1. [e.g., "Strong hook in first line — 'Ye summer mein yahi chahiye tha!'"]
2. [e.g., "Before/after format performing well"]
3. [e.g., "Posts with price callout are getting high saves"]
4. [e.g., "Colour palette — bright pinks and oranges dominating"]

#### Indian/Cultural Angle
<!-- Any festivals, cultural moments, news events tied to this keyword right now -->

#### Relevance to Your Brand
<!-- Claude connects the trend to the brand context in CLAUDE.md -->
- How this keyword maps to your product category:
- Audience overlap (does this trend reach your target audience?):
- Risk / caution (anything off-brand about this trend?):

---

## Notes for Customisation

<!-- Add any default keywords to always monitor -->
**Default keywords to track:**
<!-- e.g., ethnic wear, kurta, festive fashion, Indian fashion -->

<!-- Specific platforms or communities to always check -->
<!-- e.g., "Always check what's trending on ShareChat and Moj for tier-2 audiences" -->
