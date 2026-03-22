# Skill 01 — The Sequence Builder

> *"Cold outbound is the hardest sequence to write because you're asking for attention you haven't earned yet. The goal isn't to sound impressive. It's to sound relevant."*

---

## What this is for

Your team is going cold. No prior contact, no signal, no warm intro. Just an ICP account list and the task of getting someone who didn't ask to hear from you to respond anyway.

The hardest part isn't the product knowledge. It's personalization at scale. When you're sending to hundreds of prospects, every touch wants to feel like it was written for one person. That tension — volume versus humanity — is where most sequences break down.

This prompt solves it by separating the structure from the personalization. You build the architecture once. You define the personalization variables per persona. Claude assembles something that scales without reading like a template.

---

## The moment this solves

Your team has a new vertical to hit, a new persona to crack, or a campaign that needs to go out by Friday. You need a full sequence — subject lines, email bodies, call steps, LinkedIn touches — and you need every touch to build on the last one without repeating itself.

Normally that's a two-hour build. This prompt gets you to a first draft in under ten minutes that your team can actually use.

---

## The base prompt

Copy this. Paste it into Claude. Fill in the brackets with whatever data you have.

```
Build me a cold outbound sequence for my BDR team. We are reaching out to 
prospects with no prior contact — no signal, no event trigger, just ICP targeting.

Here is the context:

**Company and product:**
[Describe what you sell and who you sell to.]

**Target persona:**
[Who is this sequence for? Name, title, and what keeps them up at night.]

**The ICP account profile:**
[What does the ideal account look like?]

**What we're NOT doing:**
[What are the common mistakes or approaches you want to avoid?]

**Tone:**
[How should this sound?]

**Sequence length:** [e.g. 8 touches over 14 days]

**Channels available:** [e.g. Email, phone, LinkedIn]

---

Build the sequence in this format for each touch:

**Touch [#] — Day [X] — Channel**
- Subject line (email) or opening line (call/LinkedIn):
- Body / script:
- Personalization note: [One sentence on where and how to personalize]
- What this touch is trying to do: [One sentence on its job in the sequence]
```

---

## The personalization at scale prompt

Run this separately once you have your sequence built:

```
I have a cold outbound sequence built for [persona] at [account type]. 
The sequence is solid but I need to make it personalize at scale without 
my reps rewriting every email from scratch.

Here is the sequence: [paste your sequence]

For each email touch, give me:

1. **The personalization slot** — the one sentence that should be customized per prospect
2. **The research question** — what should a rep look for to fill that slot in 60 seconds
3. **A fill-in example** — what a personalized version looks like when the research is done
```

---

## Make it yours

```
I want to build a sequence context block for my team. Ask me these questions one at a time:

1. What does your company sell and what's the one-line value prop that actually resonates?
2. Who are your top 2-3 personas by title and what's the pain each one feels most acutely?
3. What's the one thing your BDRs do in their best sequences that you want to make sure shows up?
4. What's the most common mistake you see in sequences built by your team or AI tools?
5. How many touches and over what timeframe does your standard cold sequence run?

After I answer, write me a sequence context block I can paste into any sequence prompt.
```

---

## Tips from the field

**The "what we're NOT doing" field is as important as the brief.**
Telling Claude what you don't want — feature lists, early demo asks, name-in-subject-line tricks — is often more valuable than telling it what you do want. It removes the defaults.

**Touch one earns touch two. That's its only job.**
The most common mistake in cold sequences is trying to close too early. Touch one should make someone curious enough to open touch two.

**The pattern-break touch is worth the investment.**
Every sequence needs one touch that's shorter, different, or unexpected. It's often the touch that gets a reply.

**The close matters as much as the open.**
The final touch is where most sequences get lazy. The prompt is built to produce a genuine close that respects their time and leaves the door open without begging.

**Personalization is a research problem, not a writing problem.**
Your reps don't struggle to write personalized emails. They struggle to find the specific detail that makes personalization real. The personalization at scale prompt solves the research side.

---

## What this skill pairs with

- **[Skill 02 — The Talk Track Generator](../02-talk-track-generator/)** — Build the call script that runs alongside this sequence
- **[Skill 07 — The Play Launcher](../07-play-launcher/)** — When you have a signal and need a sequence built around it fast

---

*Part of [The Manager's Claude Playbook](../README.md) by Jared Langley*
