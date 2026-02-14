
# The Resume Agent

"When the system filters you out, build a new system." — Me.

But as I navigating through the job market, I realized the hunt is... well, *different*. It’s an ecosystem of its own. It doesn't matter where you are—the rules are obscure, and the gatekeepers are invisible. I realized I needed to figure out the "system" behind hiring.

It felt... Different. The ecosystem I built around me was thriving, but the resume ecosystem felt like a black hole.

I realized I needed to treat my job hunt like I treated MavMarket: as a **System**.

So, being me, I decided to engineer a solution. If they use a machine to filter me, I’ll use a machine to write for them. But not just any machine—an Agent.

TBH, I started with Gemini. It was cool. I’d paste my resume, paste a JD, and iterate. But I had to do it one experience at a time because of the context window. Copy, paste, prompt, repeat. It was a band-aid, not a solution.

Then I found **Antigravity**.

Before this, I used **Gemini**. It was great for generating points, but I had to do it one experience at a time because of the context window. Copy-paste. Prompt. Copy-paste again. It wasn't a system; it was a band-aid.

**Antigravity is different.** It can create `.md` files. It can read my entire history. It allows me to define a **Skill**—a repeatable Agent workflow—that I can run over and over for different roles (Product Manager, Engineer, Founder) without starting from scratch.

I built a `SKILL.md` file. This wasn't just a prompt; it was my Standard Operating Procedure.

## Part 2: XYZ of Impact

I didn't want generic fluff. I wanted data. I found the logic Google recruiters use: the **XYZ Strategy**.

> **"Accomplished [X] as measured by [Y], by doing [Z]"**

It changes everything.
*   **Before:** "I managed a club." (Boring. Next.)
*   **After:** "Scaled community to **100+ active members** [X] as measured by **event attendance** [Y], by **directing a cross-functional 10-member executive board** [Z]."

I hard-coded this formula into the agent. Now, if I try to feed it a weak bullet point, it stops me. It demands the "Y"—the metric. It forces me to think about my impact, not just my tasks.

## Connecting the Dots: Logic & Structure

I realized `Context` is key.

I created a `career_profile.md`—my "Master Profile." It has everything: every MavMarket win, every e-DAM workshop, every project.

When I see a Job Description (JD), the agent does a gap analysis. It scans the JD, looks at my Master Profile, and pulls the *exact* experience that fits. It’s like having a personalized career coach who remembers everything I’ve ever done.


## The Formatting Nightmare

We've all been there. You spend 4 hours in **Word** or **Google Docs**, fighting with the margins. One bullet point is slightly off, and suddenly your entire document explodes. Or you try **Canva** because it looks pretty, but then you realize the ATS can't parse the text because it's rendering as an image or a weird PDF structure.

The solution? **LaTeX** and **Overleaf**.

I automate the content generation, but the final rendering happens in Overleaf. Why? Because on a resume, **space is real estate**. You can't afford to waste it.

With Overleaf, I have access to **each and every line and space**. If I need to tighten a margin by 0.1cm to fit that crucial metric, I can. It’s precision engineering for your career history. No more fighting with invisible formatting ghosts in Word.

I automated the design. The agent takes the content and injects it into a `resume.cls` template. No more drag-and-drop. No more broken layouts. Just a clean, crisp PDF that the ATS loves.

I built this for myself, but I know I’m not the only one struggling with the black hole.

In the spirit of the ecosystem—from T-Hub to 1 Million Cups—I’ve decided to open source it. You can grab the code here:

[**<GitHub Icon> Resume Agent Repository**](https://github.com/abhisheknagaraja/resume-agent)

It includes the Logic (`SKILL.md`), the Layout (`resume.cls`), and the Template. TBH, it’s a game changer.

## Why This Matters

This isn't just about getting a job. It’s about **mindset**. It’s about taking a system that feels broken and finding a way to make it work for you. "When life doesn't give you lemons, Go Find them, make lemonade, and sell it."

This agent matches my lemons to their lemonade stand. Perfectly.
