# Brand Context — Miraya

This file is the single source of truth for all campaign generation, research,
and social media tasks. Every skill and agent reads from here automatically.
Do not ask the user for information that is already defined in this file.

**Also read before any visual or design task:** `art_style.md`

---

## Brand Identity

**Brand Name:** Miraya
**Category:** Women's ethnic wear
**Location:** Planet Mall, B-35, 734001, Siliguri, West Bengal, India
**Instagram Handle:** @miraya_india
**Sales Channels:** Physical store only + Instagram DMs / Instagram payments (no e-commerce website)

**What we sell:**
- Traditional kurtas with pure handwork, hand embroidery, and premium fabric
- Cotton tunics
- All categories of women's ethnic wear

**USP:** Authentic handcrafted ethnic wear — real handwork, real fabric, real craftsmanship.
Not mass-produced. Each piece reflects traditional artistry.

**Brand Story:**
Miraya is a women's ethnic wear store in Siliguri, West Bengal, rooted in the love for
traditional Indian handcraft. We believe in clothing that carries a story — pure fabrics,
hand embroidery, and artisan craftsmanship that fast fashion cannot replicate.
Our customers are women who value quality, heritage, and looking effortlessly ethnic.

---

## Brand Voice & Tone

**Language:** Hinglish (natural Hindi-English mix the way urban Indian women actually speak)
**Overall tone:** Warm, aspirational, feminine, culturally rooted — never salesy or pushy
**Formality:** Semi-casual — like a knowledgeable friend who understands fashion
**Emoji usage:** Moderate — use to add warmth, not clutter
**Key themes to weave in:** Handcraft, purity, heritage, effortless elegance, "made with love"

**Words/phrases we love:**
- "Haath ka kaam" (handwork), "pure fabric", "handcrafted with love"
- "Apni favourite ethnic look", "traditional with a modern feel"
- "Sirf Miraya mein milega" (only at Miraya)

**Words/phrases to avoid:**
- "Cheap", "discount dhamaka", "sale sale sale" (avoid aggressive sale language)
- Do not over-promise delivery or shipping (we don't deliver online — store + DM only)

**Brand tagline (working):** *"Woh ethnic feel, woh authentic touch."*

---

## Target Audience

**Primary audience:**
- **Who:** Women in and around Siliguri, West Bengal
- **Age range:** 20–45
- **Interests:** Ethnic fashion, traditional wear, handcrafted clothing, festivals, weddings
- **Income:** Mid to upper-mid (willing to pay for quality over quantity)
- **Shopping behaviour:** Visits malls, browses Instagram for style inspiration, DMs brands to enquire
- **Pain points:** Hard to find genuine handwork at fair prices; most stores sell machine-made
- **Aspirations:** Looking elegant and culturally connected without compromising on fabric quality
- **Language:** Hinglish, Bengali-Hindi mix, understands English

**Secondary audience:**
- Women in nearby areas (Jalpaiguri, Darjeeling, North Bengal region)
- Bengali diaspora following ethnic fashion on Instagram

---

## Products & Pricing Guide

> Update prices when they change. The agent will only mention prices listed here.

| Product | Description | Price Range |
|---|---|---|
| Traditional Kurtas | Pure fabric, hand embroidery, handwork | ₹ [add price range] |
| Cotton Tunics | Breathable cotton, everyday wear | ₹ [add price range] |
| Ethnic Co-ords / Sets | [add if applicable] | ₹ [add price range] |
| Dupattas | [add if applicable] | ₹ [add price range] |

**Hero / Bestsellers:**
<!-- List your top-selling or most photographed pieces here -->
<!-- Example: "Chikankari cotton kurta — bestseller, ₹899" -->

**Current Promotions:**
<!-- Update before each campaign season -->
<!-- Example: "Durga Puja collection launch — 10% off on first visit, mention Instagram" -->

**Pricing Philosophy:** Mid-premium. Emphasise value of handcraft over price.
Never position as "budget". Position as "worth it".

---

## Sales Process (Important for CTAs)

Since we sell via **store visits and Instagram DMs only**:
- Every CTA must direct to one of: "Visit us at Planet Mall" / "DM to enquire" / "DM to order"
- Never use "Shop now" with a link — we have no online store
- For Instagram: "Link in bio" is not relevant — use "DM us" or "Comment below"
- Include store address in campaigns targeting local discovery:
  **Planet Mall, B-35, Siliguri – 734001**

---

## Connected Meta Accounts

<!-- Fill in after running auth_setup.py -->
**Facebook Page ID:** [add after setup]
**Facebook Page Name:** [add after setup]
**Instagram User ID:** [add after setup]
**Instagram Username:** @miraya_india

---

## Competitor Brands

These brands operate in the same market and should be monitored regularly.
The `/fetch-competitor-insights` skill reads this list automatically.

| Handle | Notes |
|---|---|
| @alamode_slg | Local Siliguri fashion brand — monitor content style and offers |
| @trendxmastani | Local competitor — monitor for tone, hashtags, campaign themes |

---

## Inspiration Brands

> **TO FILL IN:** Add 3–5 Instagram handles of brands whose content style,
> aesthetic, or campaign themes you admire. These will be used to shape
> the visual and copy direction of your campaigns.

| Handle | What you like about them |
|---|---|
| @[handle] | [e.g., "Love their carousel storytelling"] |
| @[handle] | [e.g., "Their Hinglish captions feel very natural"] |
| @[handle] | [e.g., "Great use of festival themes"] |

---

## Visual Direction

**For all image generation and carousel design tasks, read `art_style.md` first.**

Key visual rules (full detail in `art_style.md`):
- **Story posts:** Warm caricature illustration — Desi Glow style (Amul-inspired, watercolour wash)
- **Carousel cohesion:** ONE colour palette per carousel. Never mix palettes across slides.
- **Characters:** Real Indian women, diverse body types and skin tones, 4 archetypes defined in `art_style.md`
- **Emotional arc:** Reality → she carries so much → barely time for herself → Miraya → she glows
- **Image prompts:** Always use the base prompt from `art_style.md` before adding scene detail

**Approved colour palettes** (hex codes in `art_style.md`):
- Palette 1: Coral Dawn — spring/summer/new arrivals
- Palette 2: Teal Heritage — handcraft/artisan stories
- Palette 3: Bengali Gold — Durga Puja/festive
- Palette 4: Monsoon Soft — everyday/emotional storytelling

---

## Campaign Rules (Always Follow — No Exceptions)

1. **Always output as DRAFT.** Never call `publish_to_facebook` or `publish_to_instagram`
   without the user explicitly typing "post it", "publish", or "go ahead and post".

2. **Always write in Hinglish.** Natural Hindi-English mix. Not translated — genuinely spoken.

3. **Always research hashtags** before finalising a post. Do not guess hashtags.
   Use `web_search` to find which hashtags are active and relevant for the topic + niche.

4. **CTAs must match our sales channel.** Always direct to store visit or Instagram DM.
   Never use "shop now" with a link. Never mention online delivery.

5. **Always include an image/creative prompt** with every campaign draft.
   For story/comic posts: follow `art_style.md` base prompt. For product posts: describe
   subject, mood, colour palette, background, lighting, text overlay.

6. **Read audience insights** if available in the session before generating campaigns.

7. **Never invent prices.** Only mention prices from the Products & Pricing Guide above.

8. **Location matters.** Siliguri is in North Bengal — reference local festivals
   (Durga Puja, Eid, Diwali, Teej, Bengali New Year / Poila Boishakh) and
   local culture where relevant.

9. **Carousel cohesion.** Every slide in a carousel must share the same colour palette,
   character design, typography, and illustration style. Read `art_style.md` before
   generating any multi-slide content.

---

## Available Skills (Slash Commands)

Invoke these in Claude Code or Claude Desktop by typing the command:

### Research Skills
| Command | What it does |
|---|---|
| `/fetch-audience-insights` | Pulls live Instagram + Facebook audience demographics and engagement |
| `/fetch-competitor-insights` | Researches @alamode_slg and @trendxmastani — content gaps and opportunities |
| `/fetch-trending-posts [keyword]` | Finds trending content for a keyword on Instagram India |
| `/understand-trending` | Analyses *why* something is trending — emotion, lifecycle, brand angle |
| `/research-topic` | Deep topic research brief before writing campaign content |

### Campaign Creation Skills
| Command | What it does |
|---|---|
| `/create-campaign` | Standard product campaign — Hinglish caption + researched hashtags + image prompt |
| `/create-story-post` | Single "Woh Har Roz Ki Ladki" comic post — 5-panel emotional story arc |
| `/create-comic-campaign` | Full 3–5 post story series with different character archetypes |

### Orchestration
| Command | What it does |
|---|---|
| `/run-campaign [keyword]` | Full automated pipeline: insights → competitors → trends → research → draft |

---

## Standalone Agents (Python CLI)

For running outside Claude Code:

```bash
# Full campaign agent (keyword → Hinglish campaign draft)
python agent.py "cotton kurta"
python agent.py "Durga Puja collection"

# Story / comic campaign agent (everyday woman storytelling)
python story_agent.py "spring summer — everyday moments"
python story_agent.py "Durga Puja — women who celebrate quietly" --posts 3
```

---

## Key Festivals & Campaign Calendar

| Festival / Moment | Approximate Timing | Notes |
|---|---|---|
| Poila Boishakh (Bengali New Year) | Mid-April | Very important for Bengali audience |
| Eid | Varies | Large Muslim audience in North Bengal |
| Durga Puja | Oct | Biggest festival for Bengali women's ethnic wear |
| Navratri / Dussehra | Oct | Important for kurta/ethnic wear sales |
| Diwali | Oct–Nov | |
| Christmas / New Year | Dec | Mall foot traffic peaks |
| Wedding Season | Nov–Feb | Bridal party / guest wear — high demand |
| Mother's Day | May | Gift angle |

---

## Session Notes

<!-- Temporary context for current campaign. Clear after each campaign. -->
<!-- Example: "Running Durga Puja campaign. Focus: new handembroidered kurta collection." -->
