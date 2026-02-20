# The Resume Agent: Hacking the Hiring Algorithm

"When the system filters you out, build a new system." — Me.

Navigating through the job market, I realized the hunt is... well, *different*. It’s an ecosystem of its own. It doesn't matter where you are—the rules are obscure, and the gatekeepers are invisible. I realized I needed to figure out the "system" behind hiring.

The ecosystem I built around me at MavMarket was thriving, but the resume ecosystem felt like a black hole.

I realized I needed to treat my job hunt like I treated my products: as a **System**.

So, being me, I decided to engineer a solution. If they use a machine to filter me, I’ll use a machine to write for them. But not just any machine—an **Agent**.

## Part 1: From Prompt to Protocol

TBH, I started with Gemini. It was cool. I’d paste my resume, paste a JD, and iterate. But I had to do it one experience at a time because of the context window. Copy, paste, prompt, repeat. It was a band-aid, not a solution.

Then I found **Antigravity**. It allows me to define a **Skill**—a repeatable Agent workflow—that I can run over and over for different roles (Product Manager, Engineer, Founder) without starting from scratch.

I built a `SKILL.md` file. This is my Standard Operating Procedure (SOP). It’s not just a prompt; it’s a **14-point Protocol** that enforces quality control before a single line of code is written.

### The Protocol
My agent doesn't "hallucinate" generic buzzwords. It follows strict rules:
1.  **The Hierarchy of Impact:** Results first, skills second.
2.  **Role-Based Tuning:** If I'm applying for a **GTM role**, it focuses on "Revenue," "Funnel," and "Adoption." If it's an **Engineering role**, it pivots to "Latency," "Throughput," and "Scalability."
3.  **Gap Management:** If I lack a specific skill, the agent identifies adjacent technologies I *do* know, rather than making things up.

## Part 2: The XYZ of Impact

I didn't want generic fluff. I wanted data. I hard-coded the **XYZ Strategy** used by top tech recruiters:

> **"Accomplished [X] as measured by [Y], by doing [Z]"**

It changes everything.

*   **Before:** "Managed the MavMarket online store." (Boring. Next.)
*   **After:** "Accomplished **successful product launch** [X] as measured by **scaling to 5,000+ users and $120,000 in revenue** [Y], by **acting as Product Owner** to manage the full product lifecycle [Z]."

The agent now stops me if I try to feed it a weak bullet point. It demands the "Y"—the metric. It forces me to think about my impact, not just my tasks.

## Part 3: The Architecture

We've all been there. You spend 4 hours in **Word** or **Google Docs**, fighting with the margins. One bullet point is slightly off, and suddenly your entire document explodes.

The solution? **LaTeX** and **Overleaf**.

I automate the content generation, but the final rendering happens in Overleaf. Why? Because on a resume, **space is real estate**.

### Single-File Turnkey Design
I deprecated the old complex folder structures. Now, everything lives in a **Single-File Architecture**.
-   **No Dependency Hell:** The `resume.cls` logic is embedded directly into the `.tex` file.
-   **Portable:** I can send this one file to anyone, and it compiles perfectly.
-   **ATS Optimized:** 
    -   **No Columns/Tables:** Layout parsing is the #1 failure point for ATS. My template uses a clean, single-column design.
    -   **Standard Fonts:** Logic ensures no weird glyphs confuse the scanner.
    -   **Hidden Optimization:** The code structure itself is designed to be machine-readable first, human-readable second.

## Part 4: The Workflow (Human-in-the-Loop)

Automation is great, but trust is better. That’s why I built a **Staging Area**.

1.  **Context Ingestion:** The agent reads my `career_profile.md` (my "Master Profile" with every win I've ever had) and the Job Description.
2.  **Gap Analysis & Mapping:** It maps my wins to their requirements.
3.  **The Checkpoint:** Before generating the final PDF code, the agent pauses. It presents a draft.
    -   *Agent:* "I've drafted the content. Please review the bullet points and metrics. Shall I proceed?"
    -   *Me:* "Modify bullet 3. The revenue was actually $150k."
4.  **Generation:** Only *after* I approve does it generate the production-ready LaTeX code. 


## Part 5: The Proof (Results)

Talk is cheap. Results are what matter.

I ran my old resume through standard ATS scanners. It scored **40%**. It was getting filtered out before a human ever saw it.

After running it through the **Resume Agent**, using the Single-File architecture and XYZ strategy:

**ATS Score: >90%**

![ATS Score Result - Overall](path/to/ats_score_image_1.png)

![ATS Score Result - Detailed Breakdown](path/to/ats_score_image_2.png)

The system works. It doesn't just "look" better; it performs better.

## Why This Matters

This isn't just about getting a job. It’s about **mindset**. It’s about taking a system that feels broken and finding a way to make it work for you. "When life doesn't give you lemons, Go Find them, make lemonade, and sell it."

This agent matches my lemons to their lemonade stand. Perfectly.

## Open Source for the Community

In the spirit of the ecosystem—from T-Hub to 1 Million Cups—I’ve decided to open source it. You can grab the code here:

[**<GitHub Icon> Resume Agent Repository**](https://github.com/nagarajaabhishek/resume_agent)

It includes the Logic (`SKILL.md`), the Template, and the Strategy. TBH, it’s a game changer.
