# Skill 04 — The Pipeline Reviewer

> *"You have the numbers. You just don't have a story yet — and your VP has a call in 20 minutes."*

---

## What this is for

End of week. End of month. Someone up the chain needs a pipeline update and the data is living in three different places — Salesforce has the opps, Outreach has the activity, Slack has the context that explains why the numbers look the way they do.

You're not a data analyst. You're a manager. Your job isn't to report the pipeline — it's to have a point of view on it. What's real, what's at risk, what moved, what didn't, and what you're doing about it.

This prompt takes whatever you have — even rough, copied-from-three-places data — and turns it into a clean pipeline narrative with a recommendation at the end.

---

## The moment this solves

It's Friday afternoon. Your VP wants a pipeline update before the weekend. You open Salesforce, export something, scan your Outreach dashboard, remember two things a rep told you in Slack that explain a lot, and then spend 40 minutes trying to assemble it all.

This prompt does that assembly in under five minutes.

---

## The base prompt

```
I need help turning raw pipeline data into a clear narrative I can share 
with my manager or VP. I don't need a spreadsheet — I need a story with 
a point of view.

Here is my context:

**Time period:** [This week / this month / end of quarter]
**My team structure:** 
[How you think about pipeline — e.g. "I break it down by source: 
marketing-generated, BDR-generated, and sales-generated."]

**The data I have:**
[Paste whatever you have — messy is fine.]

**What I know that the data doesn't show:**
[This is the most important field. Context from rep conversations, 
Slack, or gut instinct that doesn't appear in the numbers.]

**Who I'm reporting to and what they care about:**
[E.g. "My VP of Sales. She cares most about pipeline coverage and 
BDR-to-qualified conversion."]

**What I want them to feel confident about after reading this:**
[The one thing you want them to take away.]

---

Give me:

1. **The headline** — One sentence. The honest summary.

2. **Pipeline by source** — 2-3 sentences per bucket. What moved, what didn't.

3. **What the data doesn't show** — The qualitative context. This is where 
   your credibility lives.

4. **Risk and opportunity** — One of each. Specific.

5. **Your recommendation** — What you're doing about it. Not watching — doing.

Under 300 words. Should paste into Slack, email, or read aloud on a call.
```

---

## The Slack version

```
Same context as above, but give me a Slack-friendly version:
- One opening line: the honest headline
- Three bullet points max
- One closing line on what's being done about it
Under 100 words. No headers. No bold labels.
```

---

## Make it yours

```
I want to build a pipeline review template for my team. Ask me these questions:

1. How do you segment pipeline — by source, by rep, by product line?
2. What does your manager care most about when you send an update?
3. What's the metric you trust most as an indicator of real pipeline health?
4. What gets lost most often when you summarize pipeline for leadership?
5. What's a phrase you've used that landed well with your VP?

After I answer, write me a pipeline context block.
```

---

## Tips from the field

**Paste messy data. Seriously.** Copy the Salesforce export, paste in the Outreach numbers, add two sentences of Slack context. Claude will find the structure.

**"What the data doesn't show" is where your credibility lives.** Anyone can read a report. What your VP can't see is what you know from being close to the team.

**The headline is the hardest part.** Most managers bury the lead. The headline forces the point of view up front. If you hate the first draft: "Make it more honest" or "This is too optimistic."

**Read it back-to-front before you send it.** Recommendation first, then risk/opportunity, then the rest. If the recommendation doesn't connect to the risk, something is off.

---

## What this skill pairs with

- **[Skill 05 — The Capacity Model Framer](../05-capacity-model-framer/)** — When the pipeline update leads to a headcount conversation
- **[Skill 07 — The Play Launcher](../07-play-launcher/)** — When the pipeline review reveals a gap and you need a campaign to close it fast

---

*Part of [The Manager's Claude Playbook](../README.md) by Jared Langley*
