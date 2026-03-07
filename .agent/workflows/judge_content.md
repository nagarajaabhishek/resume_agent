---
description: A protocol for evaluating resume content (Experience, Skills, Tools, Methodologies) against the "Hiring Bar".
---

# Content Judge Workflow

> **Purpose:** Critically analyze resume data to ensure strategic alignment and recruiter impact.
> **Role:** Content Strategist / Hiring Bar Advocate.

## Phase 1: Context Gathering
1.  **Read the YAML:** Load the target role data (e.g., `Abhishek/Scrum_Master/role_scrum_master.yaml`).
2.  **Read the Guidelines:** Re-read [Role-Based Guidelines](file:///Users/abhisheknagaraja/Documents/Resume_Agent/.agent/skills/resume_generation/rules/role_guidelines.md) for the specific role.
3.  **Read the Pillars:** Consult [Content Judgment Pillars](file:///Users/abhisheknagaraja/Documents/Resume_Agent/.agent/skills/resume_generation/rules/content_judgment_pillars.md).

## Phase 2: Systematic Evaluation (The Scorecard)
Evaluate the YAML content against the 8 Pillars and assign a rating (Low/Medium/High Impact):

1.  **Strategic Argument:** Is the work history a "slam dunk" for this role?
2.  **Recruiter Empathy:** Does it speak to the recruiter's specific needs?
3.  **Hard Skill Depth:** Are the core technical skills properly showcased?
4.  **Tool & Application Mastery:** Is the professional toolset complete?
5.  **Methodological Rigor:** Are frameworks (Agile, SDLC, etc.) correctly utilized?
6.  **Soft Skill Integration:** Are soft skills proven through action?
7.  **Keyword Naturalism:** Is the JD terminology woven in naturally?
8.  **AI-Forwardness:** Does it demonstrate modern productivity (AI/Automation)?

## Phase 3: Actionable Feedback
For any pillar rated "Low" or "Medium", you MUST provide:
- **The "Why":** Why is this bullet or section weak?
- **The "How":** A specific rewrite or expansion suggestion.

## Phase 4: Verification
1.  **Update the YAML:** After user approval of suggestions, update the source YAML data.
2.  **Regenerate & Audit:** Run `python3 .agent/scripts/generate_resume.py [YAML_PATH]` to generate the new `.tex` file. Then, use the [Resume Audit Protocol](file:///Users/abhisheknagaraja/Documents/Resume_Agent/.agent/workflows/audit_resume.md) to ensure the 2-line visual symmetry rule hasn't been broken.
