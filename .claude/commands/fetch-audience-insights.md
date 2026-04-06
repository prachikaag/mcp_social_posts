# Skill: Fetch Audience Insights

Fetch live audience demographics and engagement from Miraya's connected
Facebook Page and Instagram account, then produce a campaign-ready brief.

All account IDs are read from CLAUDE.md — do not ask the user for them.

---

## Steps

1. Read from CLAUDE.md:
   - `Facebook Page ID` (Connected Meta Accounts section)
   - `Instagram User ID` (Connected Meta Accounts section)

2. If IDs are not yet filled in CLAUDE.md, call `list_connected_accounts`
   to retrieve them, then remind the user to save the IDs to CLAUDE.md.

3. Call `get_facebook_insights(page_id)` and `get_instagram_insights(ig_user_id)`
   in parallel.

4. Synthesise results into the output format below, interpreting the numbers
   in the context of Miraya's brand (women's ethnic wear, Siliguri, 20–45 age group).

---

## Output Format

### Miraya — Audience Insights
**Date fetched:** [today's date]
**Note:** Demographic data has a 48-hour reporting lag.

#### Instagram (@miraya_india)
- **Weekly reach:** [n]
- **Weekly impressions:** [n]
- **Profile views this week:** [n]
- **Followers:** [n]
- **Top age groups:** [e.g., 25-34 (41%), 18-24 (29%)]
- **Gender split:** [e.g., Female 89%, Male 11%]
- **Top cities:** [e.g., Siliguri, Jalpaiguri, Kolkata]

#### Facebook Page
- **Weekly reach:** [n]
- **Post engagements this week:** [n]
- **Total followers:** [n]
- **Top age groups:** [breakdown]
- **Gender split:** [breakdown]
- **Top cities:** [breakdown]

#### Campaign Takeaways
<!-- Interpret the data specifically for Miraya's next campaign -->
- [e.g., "Majority audience is women 25-34 in Siliguri — lean into 'local pride' angle"]
- [e.g., "Engagement dipped this week — hook-first content and an offer will help"]
- [e.g., "Strong presence in Jalpaiguri too — consider mentioning 'North Bengal' in copy"]
