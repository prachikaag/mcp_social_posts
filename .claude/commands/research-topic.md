# Skill: Research the Topic

Do a thorough research pass on a campaign topic before writing any content.
This ensures campaigns are grounded in real context — not generic copy.

---

## When to Use This Skill

Run this before `/create-campaign` when you want the campaign to feel informed
and specific rather than surface-level. Good research is what separates a
post that gets saved from one that gets scrolled past.

---

## Inputs Required

- **Topic or keyword** (the campaign subject)
- **Brand context** — read from CLAUDE.md
- **Audience insights** (run `/fetch-audience-insights` first if not done recently)
- **Trend context** (run `/fetch-trending-posts` and `/understand-trending` for richer output)

---

## Steps

1. **Define the topic scope**
   - What exactly is this campaign about? (product launch, sale, festival, awareness, UGC prompt?)
   - What time window does it cover? (one post, a week-long series, a full seasonal push?)

2. **Research the cultural/seasonal context**
   Search: `[topic] India [current month/season]`
   Search: `[topic] significance Indian culture`
   - Is there a festival, awareness day, or cultural moment attached?
   - What are people in India feeling/thinking about this topic right now?
   - Any regional significance? (specific states, cities, communities)

3. **Research the product angle**
   Based on CLAUDE.md Products & Pricing Guide:
   - Which product(s) are most relevant to this topic?
   - What is the strongest benefit to highlight for this audience?
   - Any current offer or promotion to weave in?

4. **Research the audience angle**
   Based on CLAUDE.md Target Audience + most recent insights:
   - What does this audience already believe or feel about this topic?
   - What language and references will land with them (Bollywood, regional, etc.)?
   - What objection might they have? (too expensive, seen this before, not for me)

5. **Research content angles**
   Search: `[topic] content ideas India small business`
   Search: `[topic] Instagram caption ideas`
   - What angles have NOT been done to death?
   - What would genuinely surprise or delight this audience?

6. **Gather reference data**
   - Any statistics or facts that make the post more credible or shareable?
   - Any quotes, sayings (Hindi/Urdu/regional) that fit the theme?
   - Any trending audio or format that fits this topic?

---

## Output Format

### Topic Research Brief: [Topic]
**Date:** [today's date]
**Campaign window:** [e.g., Oct 10-15 / one-time post / ongoing]

#### Cultural & Seasonal Context
[What's happening in India around this topic right now]

#### Product Fit
- **Best product(s) to feature:** [from CLAUDE.md]
- **Key benefit to highlight:** [for this specific topic/moment]
- **Offer to mention (if any):** [from CLAUDE.md current offers]

#### Audience Insight
- **What this audience feels about this topic:**
- **Language/references that will land:**
- **Potential objection to address:**

#### Fresh Angles (Not Overdone)
1. [unique angle idea]
2. [unique angle idea]
3. [unique angle idea]

#### Supporting Data / References
- [fact, stat, or cultural reference that adds credibility]
- [Hinglish phrase or regional saying that fits]

#### Recommended Content Format
- [ ] Single image
- [ ] Carousel (educational / how-to / listicle)
- [ ] Video / Reel concept
- [ ] Text-heavy / quote post

#### Ready for Campaign Creation
This brief is ready to pass to `/create-campaign`.

---

## Notes for Customisation

<!-- Add recurring topics your brand always covers so Claude pre-knows the context -->
<!-- Example: "We always do a Navratri campaign — context: Gujarat garba season, our audience
     celebrates in Ahmedabad and Surat, our hero product is the chaniya choli co-ord set" -->

<!-- Example: "For sale campaigns, always research what competitors are pricing at
     so our offer positioning is sharp" -->
