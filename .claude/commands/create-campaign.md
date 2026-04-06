# Skill: Create Social Media Campaign

Generate a complete, ready-to-review Hinglish campaign draft for Miraya —
covering Instagram and Facebook — with researched hashtags, a creative prompt,
and a campaign brief.

**This skill ALWAYS outputs a DRAFT. Never publishes automatically.**
Only call `publish_to_instagram` or `publish_to_facebook` when the user says
"post it", "publish", or "go ahead and post".

Reads all brand context from CLAUDE.md. No variables need to be asked.

---

## Steps

1. Read from CLAUDE.md:
   - Brand voice, tone, and Hinglish style guidelines
   - Target audience (women 20–45, Siliguri / North Bengal)
   - Products & Pricing Guide
   - Sales Process (DM / store visit CTAs only — no website links)
   - Festival Calendar (for seasonal relevance)
   - Competitor context (to differentiate)

2. Confirm the campaign keyword/theme from the user's message or from the
   `/run-campaign` orchestration context. If missing, ask for it.

3. **Research hashtags** using `web_search` before writing the caption:
   - `"#[keyword] Instagram India ethnic wear [current year]"` — find active tags
   - `"best hashtags [keyword] Indian fashion Instagram 2025"`
   - `"Siliguri fashion hashtags Instagram"`
   - `"handmade kurta hashtags Instagram India"`
   - Evaluate: high-volume broad tags (reach), mid-volume niche tags (relevance),
     low-volume local tags (community). Mix all three.
   - Always include: `#Miraya` `#MirayaIndia` `#SiliguriShopping` `#SiliguriEthnic`

4. **Write the Instagram caption in Hinglish:**
   - **Hook** (line 1): stop-the-scroll — question, bold claim, or relatable statement.
     Written in Hinglish. Max 10 words.
   - **Body** (2–4 lines): the story, benefit, or reason to care. Brand voice from CLAUDE.md.
     Reference handcraft, fabric quality, or cultural moment where genuine.
   - **CTA**: direct to store visit OR Instagram DM. Never a website link.
     Options: "Planet Mall aa jao", "DM karo to order", "Comment 'yes' to know more"

5. **Write the Facebook caption:**
   - Slightly longer, more conversational than Instagram
   - Same core message but add one more line of context
   - 3–5 hashtags only (not the full Instagram stack)

6. **Write the image/creative prompt** in enough detail to brief a designer
   or use an AI image generation tool.

7. **Compile the full draft** in the output format below.

---

## Output Format

---

## MIRAYA — CAMPAIGN DRAFT

> **Status: DRAFT — Not Posted**
> Review, edit, then say "post it" when ready.

---

### Campaign Overview
| Field | Value |
|---|---|
| **Keyword / Theme** | |
| **Goal** | |
| **Product Featured** | |
| **Audience** | Women 20–45, Siliguri / North Bengal |
| **Tone** | |
| **Date Created** | [today] |

---

### Instagram Post (@miraya_india)

**Caption:**
```
[Hook — Hinglish, scroll-stopping, max 10 words]

[Body — 2–4 lines, brand voice, handcraft/fabric/culture angle]

[CTA — DM / store visit, no website link]
```

**Researched Hashtags:**
```
[Category: Broad reach]
#[tag] #[tag] #[tag] #[tag] #[tag]

[Category: Niche ethnic wear]
#[tag] #[tag] #[tag] #[tag] #[tag]

[Category: Local / Siliguri]
#SiliguriShopping #SiliguriEthnic #[tag]

[Category: Brand]
#Miraya #MirayaIndia

[Category: Trending / seasonal]
#[tag] #[tag] #[tag]
```
*Total: [n] hashtags — researched and active as of [date]*

**Why these hashtags:** [1–2 lines explaining the mix strategy]

---

### Facebook Post

**Caption:**
```
[Slightly longer, more conversational version]

[CTA]
```

**Hashtags (3–5):**
```
#[tag] #[tag] #[tag] #Miraya #SiliguriShopping
```

---

### Image / Creative Prompt

```
Subject: [what to show — product, model, lifestyle]
Mood: [e.g., warm, festive, soft, rich]
Colour palette: [e.g., warm terracotta, ivory, gold accents]
Background: [e.g., minimal white studio / outdoor market / traditional courtyard]
Lighting: [e.g., soft natural light / golden hour / studio soft box]
Styling details: [e.g., dupatta draped over shoulder, minimal gold jewellery]
Text overlay (if any): [quote or price or tagline to overlay]
Style reference: [e.g., editorial lifestyle, product flat lay, real customer feel]
```

---

### Posting Recommendation
- **Instagram:** [e.g., Thursday or Saturday, 7–9 PM IST]
- **Facebook:** [e.g., Wednesday, 12–2 PM IST]

---

### Editor Notes
[Any notes on what to personalise, image sourcing suggestions, or follow-up post ideas]

---

After showing the draft, ask:
> "Kaisa laga? You can ask me to:
> - Edit the caption or change the tone
> - Try a different angle
> - Swap the hashtags
> - Generate an alternative version
> - Post it to Instagram, Facebook, or both"
