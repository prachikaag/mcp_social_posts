# Skill: Create Social Media Campaign

Create a complete, ready-to-review social media campaign brief for Instagram
and Facebook — grounded in audience insights, topic research, and brand context.

**This skill ALWAYS outputs a DRAFT. It never publishes automatically.**
Publishing only happens when the user explicitly says "post it", "publish", or "go ahead".

---

## Inputs Required

Before running, confirm the following context is available (run the relevant
skills first if not):

- [ ] Brand context loaded (CLAUDE.md)
- [ ] Audience insights fetched (`/fetch-audience-insights`) — strongly recommended
- [ ] Topic research done (`/research-topic`) — strongly recommended
- [ ] Trend context available (`/fetch-trending-posts` + `/understand-trending`) — optional but valuable
- [ ] Keyword or campaign theme (ask user if not provided)

If context is missing, ask:
> "Should I run audience insights and topic research first, or do you want to
> create the campaign with the brand context in CLAUDE.md only?"

---

## Campaign Generation Steps

1. **Confirm campaign parameters** with the user (or use what's been provided):
   - Keyword / theme
   - Product(s) to feature
   - Campaign goal (awareness / sales / engagement / UGC)
   - Tone for this specific post (can differ from default — e.g., urgent for a sale)
   - Any constraint (e.g., "mention the 20% discount", "don't use emoji")

2. **Generate the Hinglish caption** — write naturally in the brand voice from CLAUDE.md:
   - Hook (first line must stop the scroll — a question, bold claim, or relatable statement)
   - Body (the story, benefit, or reason to care — 2-4 lines)
   - CTA (clear, direct, Hinglish — e.g., "Abhi shop karo", "DM us to order", "Link in bio hai!")
   - Mix Hindi and English fluidly — not translated, genuinely Hinglish

3. **Generate hashtags:**
   - Instagram: 15-25 hashtags (mix of brand, category, niche, trending, location)
   - Facebook: 3-5 hashtags only (Facebook doesn't benefit from hashtag stacking)

4. **Generate image/creative prompt:**
   - Describe the ideal visual for this post in enough detail to brief a designer
     or generate with an AI image tool
   - Include: subject, mood, colour palette, background, any text overlay suggestion

5. **Create Facebook variant:**
   - Facebook audiences respond to slightly longer, more conversational copy
   - Fewer hashtags, slightly more context in the caption body
   - Same core message, different delivery

6. **Generate campaign brief summary** for record-keeping.

---

## Output Format

---

## CAMPAIGN DRAFT

> **Status: DRAFT — Not Posted**
> Review and edit before publishing. Tell me "post it" when ready.

---

### Campaign Overview
| Field | Details |
|---|---|
| **Theme / Keyword** | |
| **Campaign Goal** | |
| **Products Featured** | |
| **Target Audience** | |
| **Tone** | |
| **Created** | [today's date] |

---

### Instagram Post

**Caption:**
```
[Hook line — in Hinglish, scroll-stopping]

[Body — 2-4 lines, brand voice from CLAUDE.md]

[CTA — direct and Hinglish]
```

**Hashtags:**
```
#[tag] #[tag] #[tag] ... (15-25 total)
```

**Image / Creative Prompt:**
```
[Detailed visual brief for designer or AI image generation]
Subject: 
Mood/vibe: 
Colours: 
Background: 
Text overlay (if any): 
Style reference: 
```

---

### Facebook Post

**Caption:**
```
[Slightly longer, more conversational version of the same campaign]

[CTA]
```

**Hashtags:**
```
#[tag] #[tag] #[tag] (3-5 only)
```

---

### Suggested Posting Time
- **Instagram:** [e.g., Tuesday or Thursday, 7–9 PM IST — when Indian audiences are most active]
- **Facebook:** [e.g., Wednesday, 12–2 PM IST]

---

### Editor Notes
<!-- Any notes about what can be personalised, image sourcing, or follow-up posts -->

---

## After Showing the Draft

Ask:
> "How does this look? You can ask me to:
> - Edit the caption or tone
> - Try a different angle
> - Generate an alternative version
> - Post it to Instagram, Facebook, or both"

Only call `publish_to_instagram` or `publish_to_facebook` after explicit user confirmation.

---

## Notes for Customisation

<!-- Add any campaign templates or recurring formats your brand uses -->
<!-- Example: "For sale campaigns, always lead with the discount percentage in the hook" -->
<!-- Example: "For new arrivals, always end with 'limited pieces — jaldi karo!'" -->
<!-- Example: "For UGC prompts, always include a branded hashtag challenge" -->

<!-- Default posting schedule -->
**Our usual posting days:** <!-- e.g., Tuesday, Thursday, Saturday -->
**Our usual posting time:** <!-- e.g., 7 PM IST -->
