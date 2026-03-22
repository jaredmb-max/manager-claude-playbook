# SETUP.md — Loading the Manager's Claude Playbook into Claude Projects

This turns the prompt library into a set of always-on skills that activate automatically when you describe what you're working on. Instead of copying and pasting a prompt, you just say what you need and the right skill runs.

**Time to set up: 10-15 minutes.**
**What you need: Claude Pro account (claude.ai/pro)**

---

## What a Claude Project is

A Claude Project is a persistent workspace in Claude.ai where you can load custom instructions and knowledge that stay active across every conversation. Once your skills are loaded, Claude behaves like a specialist who already knows your context — your team, your product, your personas, your voice.

The difference between using the prompts in this library and using the skills:

| Prompt library | Skills in a Project |
|---|---|
| Copy the prompt, fill in the blanks, paste into Claude | Describe what you need in plain language |
| Context resets every conversation | Your context is persistent |
| Works on free Claude tier | Requires Claude Pro |
| Good for occasional use | Better for daily use |

---

## Step 1 — Create a new Claude Project

1. Go to [claude.ai](https://claude.ai) and sign in
2. In the left sidebar, click **Projects**
3. Click **New Project**
4. Name it: `Manager Playbook` or whatever makes sense for you
5. Click **Create Project**

---

## Step 2 — Add your context file

Before you load the skills, create a short context file that tells Claude about your specific situation. This is what makes every skill output calibrated to your team instead of a generic manager's team.

Create a file called `my-context.md` and fill it in:

```markdown
# My Manager Context

## Role and team
- Title: [Your title]
- Company: [Company name]
- Industry/vertical: [What you sell into]
- Team: [Number of reps, breakdown by tenure]
- Tools: [Sequencing tool, call tool, CRM]

## My buyers
- Primary persona 1: [Title, company type, top pain]
- Primary persona 2: [Title, company type, top pain]
- Primary persona 3: [Title, company type, top pain]

## My product
- What we sell: [One sentence]
- The value prop that actually lands: [One sentence]
- What we're NOT (common misconceptions to avoid): [One sentence]

## My coaching style
[2-3 sentences on how you run 1:1s, give feedback, and develop reps. 
Not the textbook version — how you actually show up.]

## Team challenges right now
[1-2 sentences on what your team is working through at the moment — 
a new persona, a conversion problem, a ramping rep, whatever is live.]

## What I want to avoid in every output
[E.g. "No corporate language. No feature lists. No em dashes. 
Don't assume my reps are struggling — they're competent people 
dealing with real problems."]
```

Upload this file to your Project by clicking **Add Content** in the Project sidebar.

---

## Step 3 — Load the skill files

Each skill in the `skills/` folder is a SKILL.md file. Load the ones you want.

**To load a skill:**
1. Open the skill file from the `skills/` folder in this repo
2. In your Claude Project, click **Add Content**
3. Paste the contents of the SKILL.md file
4. Save

You can load all 8 at once or start with the ones you'll use most. Recommended starting set:

**Start with these three:**
- `skills/03-one-on-one-prep/SKILL.md` — you'll use this every week
- `skills/06-hard-message-drafter/SKILL.md` — you'll use this when it matters most
- `skills/04-pipeline-reviewer/SKILL.md` — you'll use this every month

**Add these when you're ready:**
- `skills/01-sequence-builder/SKILL.md`
- `skills/02-talk-track-generator/SKILL.md`
- `skills/07-play-launcher/SKILL.md`
- `skills/05-capacity-model-framer/SKILL.md`
- `skills/08-enablement-doc/SKILL.md`

---

## Step 4 — Test it

Start a new conversation in your Project and try one of these:

> "I have six 1:1s tomorrow and I haven't prepped any of them. Help me prep for Marcus — he's made 40 calls this week, booked 1 meeting, and seemed off in our last standup."

> "I need to send something to a rep who's been at 50% of quota for two months. I've mentioned it in 1:1s but never named the severity directly."

> "Give me a pipeline update I can send to my VP. BDR team generated 28 meetings this month against a 36 target. Two senior reps are maxed out, two junior reps are still ramping."

If it works, Claude will run the right skill automatically and produce output calibrated to your context. If something feels off, go back to your `my-context.md` and add more specificity.

---

## Step 5 — Customize as you go

The skills are starting points, not finished products. After your first few uses, you'll notice patterns — places where the output is close but not quite right for how your team talks, or how your VP thinks, or how your reps respond.

Edit your `my-context.md` to add those specifics. The more real your context file gets, the sharper every output becomes.

---

## Troubleshooting

**Claude isn't using the right skill.**
Add more context to your request. E.g. instead of "help me with my pipeline," say "I need a pipeline narrative to share with my VP — here's the data."

**The output sounds generic.**
Your `my-context.md` needs more specificity. Add a real example of your product's value prop, a real persona description, a real thing your team struggles with.

**It's asking too many clarifying questions.**
Add to your context file: "If the request is reasonably clear, skip clarifying questions and produce output I can react to. I'll redirect if it's wrong."

**The tone is off.**
Add voice examples to your context file. Paste in a real email you wrote that landed well. Say "match this tone."

---

## A note on privacy

Your 1:1 notes, rep names, pipeline data, and deal information go into a Claude Project that is private to your account. Claude does not train on your Project data. Use first names only for reps in anything sensitive, and don't paste in information you wouldn't want stored in a cloud document.

---

*Part of [The Manager's Claude Playbook](./README.md) by Jared Langley*
