# Skill: Understand Why It's Trending

Analyse the deeper reason a keyword or content trend is gaining traction —
the emotion, cultural trigger, and lifecycle stage — so Miraya's campaign
takes the right angle rather than just copying surface-level trend aesthetics.

Reads all brand context from CLAUDE.md. Run after `/fetch-trending-posts`.

---

## Steps

1. Read from CLAUDE.md:
   - Brand voice, target audience, product focus, location (Siliguri / North Bengal)
   - Key festivals calendar

2. Take the keyword and trending post data from the previous `/fetch-trending-posts` output.

3. Run `web_search` to go deeper:
   - `"why is [keyword] trending India [current month]"`
   - `"[keyword] cultural significance India women"`
   - `"[keyword] Bengal / North Bengal relevance"`
   - `"[keyword] festival season ethnic wear 2025"`

4. Run `search_news`:
   - `"[keyword] India [current month year]"` — any news event triggering this?

5. Determine:
   - **Trigger:** What started or amplified this trend?
   - **Core emotion:** What feeling drives engagement? (pride, nostalgia, aspiration, humour, FOMO, belonging)
   - **Who is leading it:** UGC, influencers, big brands — is there room for a small local brand?
   - **Lifecycle stage:** Rising / Peak / Declining — and recommendation
   - **Brand-fit angle:** Given Miraya's products and voice, what specific angle fits authentically?

---

## Output Format

### Trend Analysis: "[keyword]"
**Date:** [today's date]

#### What Triggered This Trend
[2–3 sentences on origin/trigger]

#### Core Emotion Driving It
**Primary emotion:** [e.g., Cultural pride]
**Why it resonates with Miraya's audience (women 20–45, Siliguri):**
[Specific insight connecting emotion to this audience]

#### Who Is Leading It
[Creators, community type, or brands amplifying it]

#### Lifecycle Stage
- [ ] Rising — get in now
- [ ] Peak — only join with a very unique angle
- [ ] Declining — avoid or subvert

#### The Real Reason It Works
[The deeper cultural or psychological insight — the most important part.
e.g., "This trend works because it validates that traditional handcraft is
worth more than fast fashion. Women who buy 'real' kurtas want to be seen
as discerning. Miraya's handwork story is the perfect fit."]

#### Best Angle for Miraya
[Specific, actionable angle connecting the trend to Miraya's brand, products,
location, and audience. e.g., "Lead with the handcraft story — 'Haath ka kaam
jo machine kabhi nahi kar sakti.' This is Miraya's authentic differentiator."]

#### What to Avoid
[What would feel forced, inauthentic, or off-brand for Miraya]
