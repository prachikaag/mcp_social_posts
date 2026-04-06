# Skill: Research the Topic

Do a thorough research pass on the campaign topic before writing any content.
Produces a campaign brief grounded in real audience context, cultural timing,
and Miraya's product range.

Reads all variables from CLAUDE.md. Run after `/understand-trending`.

---

## Steps

1. Read from CLAUDE.md:
   - Products & Pricing Guide (which products fit this topic)
   - Target Audience (what this audience feels about this topic)
   - Festival Calendar (is there a seasonal hook?)
   - Brand Voice & Tone
   - Sales Process (DM / store visit CTAs only)

2. Define the campaign scope:
   - What exactly is this about? (product launch, festival, everyday wear, awareness, UGC prompt)
   - Is it a single post or a series?

3. Run `web_search` for cultural/seasonal context:
   - `"[topic] West Bengal / Siliguri [current month year]"`
   - `"[topic] Indian women fashion [current month year]"`
   - `"[topic] ethnic wear significance India"`

4. Run `web_search` for content angles:
   - `"[topic] Instagram content ideas ethnic wear brand India"`
   - `"[topic] unique campaign angle women fashion"`

5. Run `web_search` for supporting data:
   - Any facts, quotes, or cultural references that make the post more credible
   - Any relevant Hindi/Bengali/Urdu phrases or sayings that fit
   - Any trending audio or format that works for this topic

6. Identify the best-fit Miraya product(s) from CLAUDE.md for this campaign.

7. Identify the objection this audience might have — and how to pre-empt it in copy.

---

## Output Format

### Topic Research Brief: "[topic]"
**Date:** [today's date]
**Campaign type:** [single post / series / seasonal]

#### Cultural & Seasonal Context
[What's happening in India / West Bengal around this topic right now]

#### Best-Fit Miraya Product(s)
[From CLAUDE.md — which products to feature and why]

#### Key Benefit to Highlight
[The single most compelling reason this audience should care, in Miraya's voice]

#### Audience Insight
- **What this audience feels about this topic:**
- **References that will land (Bollywood, Bengali culture, local):**
- **Likely objection and how to address it:**

#### Fresh Angles (Not Overdone)
1.
2.
3.

#### Supporting Data / Cultural References
- [fact or stat]
- [Hinglish / Bengali phrase that fits]
- [cultural moment or reference]

#### Recommended Content Format
- [ ] Single product image
- [ ] Carousel (educational / styling guide / story)
- [ ] Video / Reel concept
- [ ] Quote / text card
- [ ] Before/After or Styled look

#### Ready for Campaign Creation ✓
Pass this brief to `/create-campaign`.
