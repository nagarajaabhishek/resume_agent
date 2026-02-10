---
name: Resume Generation
description: A skill for generating high-impact, ATS-optimized resumes using the XYZ strategy and LaTeX templates.
---

# Master Resume Instructions & Agent Prompt

## 1. The Strategy: XYZ
To stand out for AI/ML/Software roles, every bullet point must follow the **XYZ Strategy**:
> "Accomplished [X] as measured by [Y], by doing [Z]"

- **X (Result):** What did you achieve? (e.g., "Scaled system", "Reduced latency")
- **Y (Metric):** How do we know it worked? (e.g., "for 100k users", "by 50%")
- **Z (Action):** How did you do it? (e.g., "using Python and Redis", "by implementing A/B testing")

**Example:**
*Before:* Worked on a chatbot.
*After:* Accomplished **20% reduction in support tickets** [X] as measured by **monthly helpdesk reports** [Y], by **engineering a RAG-based chatbot** using **Python and OpenAI API** [Z].

## 2. Core Principles (The Hierarchy of Impact)
1. **ATS First**: Your resume acts as a key. Before it can be read by a human, it must be unlocked by the ATS. Ensure exact keyword matches from the JDs are present in the text *while* drafting.
2. **XYZ Strategy**: Once unlocked, the content must be high-impact. Use the "Accomplished [X] as measured by [Y], by doing [Z]" formula.
3. **Prioritize by Impact**: Arrange bullet points based on the target role. The most impressive/relevant achievement goes first.
4. **Show, Don't Tell**: Don't say "Expert in Java". Show "Built a Java microservice handling 10k RPS".

## 3. File & Folder Organization
Structured organization is critical for managing multiple candidates and versions.

### Directory Structure
```
/Resume_Agent
  /CandidateName (e.g., /Abhishek)
    /Role_or_Purpose (e.g., /Manager)
      - career_profile.md
      - [CandidateName]_[Role]_Resume.tex
      - [JobDescription].txt (Optional)
```

### Naming Conventions
- **Folder:** Use Title Case for names and roles (e.g., `Abhishek/Manager`).
- **Files:** Use the pattern `[CandidateName]_[Role]_Resume.tex` (e.g., `Abhishek_Manager_Resume.tex`).
- **Assets:** Ensure `resume.cls` is present in the specific role folder if you are testing locally, though Overleaf handles this in the cloud.

## 4. Workflow
### Phase 1: Context & Strategy
1. **Analyze Role**: Ingest target Job Descriptions (JDs) to identify key skills and themes.
2. **Context Building**: Create a `career_profile.md` (Profile Context File) to draft content.
   - **Step 1: Keyword Extraction**: Extract high-frequency ATS keywords (skills, tools, methodologies) from the JDs.
   - **Step 2: Gap Analysis**: Compare keywords against the user's profile to find evidence.
3. **Drafting (The Integration)**:
   - Write bullet points in `career_profile.md` using the **XYZ Formula**.
   - **Constraint**: You must Integrate the extracted ATS keywords *naturally* into the "Action" (Z) part of the formula.
4. **Prioritization**:
   - Reorder the drafted bullet points.
   - **Rule**: Place the highest-impact, most relevant achievements for the *specific role* at the top of each section.
5. **User Vetting**: Present `career_profile.md` to the user for review. Do NOT proceed to LaTeX until content is approved.

### Phase 2: LaTeX Execution
1. **Duplicate Template**:
   - Duplicate `.agent/skills/resume_generation/resources/master_resume_template.tex` to a new file (e.g., `/CandidateName/CandidateName_Resume.tex`).
   - **Critical**: Ensure `resume.cls` (from resources) is in the same directory.
2. **Interchange Content**:
   - Replace the placeholders in the *duplicated* file with the approved content from `career_profile.md`.
   - **Constraint**: Do not modify the template structure or style. Only inject content.
3. **Hand-off & Compilation**:
   - Instruct the user to upload the generated `.tex` file (and `resume.cls`) to Overleaf.
   - The user will manually compile the document in Overleaf. (No local compilation).
## 5. Metric Estimation (When Data is Missing)
If the user lacks exact numbers, use these logic paths to derive them:
- **Time Saved:** "Did this save 1 hour/week? That's 52 hours/year."
- **Scale:** "How many users/requests? High traffic system?"
- **Efficiency:** "Did you replace a manual process or reduce steps?"
- **Cost:** "Did this prevent a potential fine or reduce AWS bill?"

## 6. Role-Based Tuning
Adjust the tone based on the target seniority:
- **Intern/Junior:** Focus on **Execution**, Learning, and Tools. show ability to deliver sub-tasks.
- **Senior/Lead:** Focus on **Architecture**, Design Decisions, Trade-offs, and Mentorship.
- **Manager:** Focus on **Delivery**, People, Strategy, and ROI.

## 7. Gap Management Strategy
If the user lacks a required skill from the JD:
1. **Identify the Gap:** Acknowledge it in the `career_profile.md`.
2. **Find Adjacency:** Highlight a transferable skill (e.g., "SQL" for "NoSQL", "Java" for "C#").
3. **Show Learning:** demonstrate ability to learn fast or past instances of picking up new tech.

## 8. Quality Assurance (QA) Rubric
Before finalizing content, verify:
- [ ] **The "So What?" Test:** Does every bullet explain *why* it mattered?
- [ ] **Metric Check:** Is there a number (Y) or qualitative impact?
- [ ] **Tech Stack Audit:** Are the JD tools actually mentioned in the bullet points?
- [ ] **Formatting:** Are bullets under 2 lines?

## 9. Master Agent Prompt
**Copy and paste the text below into an AI agent (like ChatGPT, Claude, or Gemini) to generate new resume content:**

---
**[START PROMPT]**

You are an expert Resume Writer and Career Coach specializing in AI, Machine Learning, and Software Engineering. Your goal is to rewrite my resume bullet points to be high-impact, quantifiable, and ATS-optimized.

**My Background:**
[Paste your raw resume content or experience details here]

**Job Description I am applying for:**
[Paste the Job Description here]

**Instructions:**
1. **Use the XYZ Strategy:** Every bullet point MUST follow the structure: "Accomplished [X] as measured by [Y], by doing [Z]".
2. **Quantify:** Use specific numbers, percentages, and metrics wherever possible. If exact numbers are missing, estimate reasonable metrics based on industry standards (e.g., "improved performance" -> "reduced latency by ~30%").
3. **Keywords:** Integrate keywords from the Job Description naturally into the bullet points.
4. **Action Verbs:** Start every bullet with a strong power verb (e.g., Architected, Engineered, Deployed, Optimized).
5. **Format:** Output the result as LaTeX code compatible with the `resume.cls` format (using `\item`).

**Output the rewritten experience section in this LaTeX format:**
```latex
\begin{rSubsection}
{Job Title, Company - Location}{Dates}{}{}
\begin{itemize}[left=-1.5em, labelsep=.1cm, labelwidth=.2cm, itemsep=0.0em]
\item Accomplished \textbf{[Result]} as measured by \textbf{[Metric]}, by \textbf{[Action]}.
\item ...
\end{itemize}
\end{rSubsection}
```

**[END PROMPT]**
---
