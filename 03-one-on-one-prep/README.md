# Skill 03 — The 1:1 Prep Brief

> *"You have the data. You just don't have time to think about it before you walk in."*

---

## What this is for

You have six 1:1s this week. Maybe more. Each rep deserves your full attention. But between pipeline calls, Slack, and everything else that happened before noon, you're walking into half of them without a real agenda.

It shows. Reps feel it. Unfocused 1:1s drift into status updates. Status updates feel like surveillance. Surveillance erodes trust.

This prompt takes the raw data you already have — activity numbers, pipeline, recent call notes, whatever you can paste in — and turns it into a focused brief in under three minutes. Not a script. A structure. So you walk in knowing three things:

1. What the data actually says (not just what it shows)
2. Where to coach versus where to push
3. The one question worth asking at the end

---

## The moment this solves

It's 9:47am. Your first 1:1 is at 10. You pull up the rep's Salesforce, skim their activity, feel vaguely aware that something's off but can't name it. You open the meeting with "so how are you feeling about the week?" and spend 30 minutes in no particular direction.

This prompt replaces that.

---

## The base prompt

```
You are helping me prepare for a 1:1 with one of my BDR reps. I want to walk 
in with a clear agenda, not a blank slate.

Here is the context:

**Rep name:** [First name only or a placeholder]
**Role:** [BDR / SDR / AE]
**Time period:** [This week / last two weeks / this month]

**Activity data:**
[Paste whatever you have — calls made, emails sent, meetings booked, 
pipeline generated. Raw numbers are fine.]

**Anything notable I already know:**
[Optional — a recent win, a rough patch, a deal that stalled, a pattern 
you've noticed.]

**My coaching style:**
[Optional — e.g. "I lead with data and close with coaching."]

---

Based on this, give me:

1. **The data read** — In 3-4 sentences, what does the data actually suggest?

2. **The agenda** — 3 agenda items, in order. Each with a one-line framing question.

3. **The coaching angle** — What's the human problem underneath the numbers?

4. **The closing question** — Default: "What do you need from me this week 
that you haven't asked for?"

Keep it tight. I need to be able to read this in 90 seconds before I walk in.
```

---

## Example output

**Input:** Marcus. BDR. Last two weeks. 62 dials, 8 connects, 1 meeting. Strong last month. Seemed distracted in standup.

**Output:**

> **The data read:** Marcus is putting in the activity but losing something between the connect and the ask. 8 connects with 1 meeting suggests the conversation is happening but the transition to booking isn't landing. The distraction signal is worth treating as related — when reps go quiet internally, it usually means something is unresolved.
>
> **Agenda:**
> 1. *Connect-to-meeting conversion* — "Walk me through what typically happens after you get someone on the phone right now."
> 2. *Headspace* — "Last month was strong. What feels different right now, if anything?"
> 3. *Pipeline health* — "Which of your open opps are you most confident about and why?"
>
> **The coaching angle:** The activity is there, which means this isn't a motivation issue. The conversion gap and the distraction signal both point toward something internal — maybe a confidence wobble after a few tough connects.
>
> **The closing question:** "What do you need from me this week that you haven't asked for?"

---

## Make it yours

```
I want to create a personal context block for my 1:1 prep prompts. 
Ask me these questions one at a time:

1. How many reps do you manage and what are their general experience levels?
2. What tools do you use to track activity and pipeline?
3. How would you describe your coaching philosophy in 2-3 sentences?
4. What's a pattern you tend to over-focus on in 1:1s that you want to avoid?
5. What does a great 1:1 look like when it works?

After I answer, write me a manager context block.
```

---

## Tips from the field

**Paste messy data. It still works.** You don't need a clean spreadsheet. "She made roughly 50 calls, booked 3 meetings, has one deal she's excited about" is enough.

**The coaching angle is the part worth slowing down on.** The agenda and data read are setup. The coaching angle is the thing you'd have taken 20 minutes to arrive at on your own — or missed entirely.

**Run it the night before, not five minutes before.** The brief is most useful when you've had time to let it sit.

**The closing question is yours.** "What do you need from me this week that you haven't asked for?" works across almost every rep and situation. Make it a ritual.

---

## What this skill pairs with

- **[Skill 06 — The Hard Message Drafter](../06-hard-message-drafter/)** — When the 1:1 surfaces something that needs a follow-up in writing
- **[Skill 08 — The Enablement Doc](../08-enablement-doc/)** — When something from the 1:1 is worth packaging for the whole team

---

*Part of [The Manager's Claude Playbook](../README.md) by Jared Langley*
