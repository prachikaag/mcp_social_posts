# Skill: Fetch Audience Insights

Fetch live audience demographics and engagement metrics from your connected
Facebook Page and Instagram account, then summarise them in a clear brief
that can be used as context for campaign creation.

---

## Steps

1. Call `list_connected_accounts` to confirm which accounts are connected.
   If no accounts are listed, tell the user to run `python auth_setup.py` first.

2. Call `get_facebook_insights` using the Facebook Page ID from CLAUDE.md
   (or from the list_connected_accounts result).

3. Call `get_instagram_insights` using the Instagram User ID from CLAUDE.md
   (or from the list_connected_accounts result).

4. Summarise the combined insights in this format:

---

## Output Format

### Audience Insights Summary
**Date fetched:** [today's date]
**Note:** Demographic data has a 48-hour reporting lag.

#### Facebook Page
- **Weekly reach:** [number]
- **Weekly post engagements:** [number]
- **Total followers:** [number]
- **Top age groups:** [e.g., 25-34 (42%), 35-44 (28%)]
- **Gender split:** [e.g., Female 68%, Male 32%]
- **Top cities:** [e.g., Mumbai, Delhi, Jaipur]
- **Top countries:** [e.g., India 94%]

#### Instagram
- **Weekly reach:** [number]
- **Weekly impressions:** [number]
- **Profile views this week:** [number]
- **Followers:** [number]
- **Top age groups:** [e.g., 18-24 (35%), 25-34 (40%)]
- **Gender split:** [e.g., Female 72%, Male 28%]
- **Top cities:** [e.g., Delhi, Bangalore, Pune]

#### Key Takeaways for Campaigns
<!-- Claude should write 3-5 bullet points interpreting the data in the context
     of the brand information in CLAUDE.md -->
- [e.g., "Majority audience is women 25-34 — use aspirational, relatable copy"]
- [e.g., "Strong presence in Delhi and Mumbai — reference metro lifestyle"]
- [e.g., "Low engagement this week — consider a stronger hook or offer-led post"]

---

## Notes for Customisation

<!-- Fill in any account-specific quirks or preferences below -->
<!-- Example: "Always compare this week's reach to the previous week if possible" -->
<!-- Example: "Focus on Instagram insights — Facebook Page is less active" -->
