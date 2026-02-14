---
name: Resume Generation
description: A skill for generating high-impact, ATS-optimized resumes using the XYZ strategy and LaTeX templates.
---

# Master Resume Instructions & Agent Prompt

> **🚨 AGENT PROTOCOL:** Before analyzing any resume or generating content, you **MUST** read and process **EVERY** section of this document (Sections 1 through 14) sequentially. Do not skip any section. Each section contains critical constraints for compliance.


## 1. Core Principles (The Hierarchy of Impact)
1. **ATS First**: Your resume acts as a key. Before it can be read by a human, it must be unlocked by the ATS. Ensure exact keyword matches from the JDs are present in the text *while* drafting.
2. **XYZ Strategy**: Once unlocked, the content must be high-impact. Use the "Accomplished [X] as measured by [Y], by doing [Z]" formula.
3. **Prioritize by Impact**: Arrange bullet points based on the target role. The most impressive/relevant achievement goes first.
4. **Show, Don't Tell**: Don't say "Expert in Java". Show "Built a Java microservice handling 10k RPS".
5. **Standard Headings**: Use standard section titles ("Work Experience", "Education", "Skills", "Certifications").
6. **Profile/Summary**: Do NOT use a section header for the summary (e.g., "Profile" or "Summary"). Place the text directly below the contact information.
7. **Section Order**:
   - **Universal Rule**: Education *always* follows Summary (for students/recent grads).
   - **Scenario A: Experience-First (Default for PO, PM, GTM, Manager)**
     - Summary (No Header)
     - Education
     - **Work Experience**
     - **Projects**
     - Skills
     - Certifications
   - **Scenario B: Technical-First (Option for TPM, R&D, Dev)**
     - Summary (No Header)
     - Education
     - **Projects** (If highly innovative/relevant)
     - **Work Experience**
     - Skills
     - Certifications

## 2. File & Folder Organization
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
- **Files:** Use the pattern `FirstName_LastName_Role_Resume.tex` (e.g., `Abhishek_Nagaraja_Manager_Resume.tex`).
- **Assets:** Ensure `resume.cls` is present in the specific role folder if you are testing locally, though Overleaf handles this in the cloud.

## 3. The Strategy: XYZ
To stand out for AI/ML/Software roles, every bullet point must follow the **XYZ Strategy**:
> "Accomplished [X] as measured by [Y], by doing [Z]"

- **X (Result):** What did you achieve? (e.g., "Scaled system", "Reduced latency")
- **Y (Metric):** How do we know it worked? (e.g., "for 100k users", "by 50%")
- **Z (Action):** How did you do it? (e.g., "using Python and Redis", "by implementing A/B testing")

**Example:**
*Before:* Worked on a chatbot.
*After:* Accomplished **20% reduction in support tickets** [X] as measured by **monthly helpdesk reports** [Y], by **engineering a RAG-based chatbot** using **Python and OpenAI API** [Z].

## 4. Keyword Engineering & Optimization
1. **Acronyms & Full Forms**: Always spell out the first instance of an acronym: "Search Engine Optimization (SEO)". This covers both keyword variations for the parser.
2. **Contextual Integration**: Do not "stuff" keywords. "Python" should not just be in a list; it should be in a sentence: "...built backend using **Python**...".
3. **Frequency Check**: High-priority keywords from the JD should appear more than once (e.g., in Skills AND Work Experience).

## 5. Role-Based Tuning & Vocabulary
Adjust the tone and verbs based on the target role to align with recruiter expectations:

- **GTM / PMM / Growth:**
    - *Keywords:* Launch, Orchestrate, Go-to-Market, Revenue, User Acquisition, Funnel, Campaign, Positioning, Win Rate.
    - *Focus:* **Commercial Outcome** & **Market Adoption**.
- **Engineering / AI:**
    - *Keywords:* Architect, Engineer, Deploy, Optimize, Scale, Latency, Throughput, System Design.
    - *Focus:* **Technical Complexity** & **Reliability**.
- **Product Management (Core):**
    - *Keywords:* Roadmap, Prioritize, Stakeholder, MVP, Discovery, User Research, Strategy.
    - *Focus:* **User Value** & **Business Viability**.

## 6. Metric Estimation (When Data is Missing)
If the user lacks exact numbers, use these logic paths to derive them:
- **Time Saved:** "Did this save 1 hour/week? That's 52 hours/year."
- **Scale:** "How many users/requests? High traffic system?"
- **Efficiency:** "Did you replace a manual process or reduce steps?"
- **Cost:** "Did this prevent a potential fine or reduce AWS bill?"

## 7. Gap Management Strategy
If the user lacks a required skill from the JD:
1. **Identify the Gap:** Acknowledge it in the `career_profile.md`.
2. **Find Adjacency:** Highlight a transferable skill (e.g., "SQL" for "NoSQL", "Java" for "C#").
3. **Show Learning:** demonstrate ability to learn fast or past instances of picking up new tech.

## 8. Content Anti-Patterns (Do NOT Do This)
1.  **Double Dipping (Duplication):** NEVER repeat the same specific metric or achievement in both the Summary and Work Experience.
    - *Bad:* Summary says "Managed $120k revenue", Experience says "Managed $120k revenue".
    - *Good:* Summary says "Proven track record of revenue generation", Experience says "Managed $120k revenue".
2.  **Context Mixing:** Do not use Engineering verbs for GTM bullets (e.g., don't say "Built a marketing plan", say "Designed/Executed a marketing plan").

## 9. Workflow
### Phase 1: Context & Strategy (The "Human-in-the-Loop" Layer)
1. **Analyze Role**: Ingest target Job Descriptions (JDs) to identify key skills and themes.
2. **Context File Creation (`career_profile.md`)**:
   - **Action**: Create or update `career_profile.md` for the specific role.
   - **Content**: Draft the *exact* bullet points, summary, and skills you intend to use.
   - **Why**: This text file serves as the "Staging Area" for content. It is easier to read/edit than LaTeX.
3. **Optimized Mapping**:
   - Map JD keywords to specific bullet points in `career_profile.md`.
   - Ensure the "XYZ" formula is applied strictly.
4. **MANDATORY USER VALIDATION**:
   - **Protocol**: You MUST stop and ask the user to review `career_profile.md`.
   - **Prompt**: "I have drafted the content in `career_profile.md`. Please review the bullet points and metrics. Shall I proceed to generate the resume?"
   - **Constraint**: Do NOT generate the `.tex` file until the user explicitly approves this context file.

### Phase 2: LaTeX Execution
1. **Duplicate Template**:
   - Duplicate `.agent/skills/resume_generation/resources/single_file_resume_template.tex` to a new file (e.g., `/CandidateName/CandidateName_Resume.tex`).
   - **Note**: This template is self-contained. You do NOT need a separate `resume.cls` file.
2. **Interchange Content**:
   - Replace the placeholders in the *duplicated* file with the approved content from `career_profile.md`.
   - **Constraint**: Do not modify the embedded class definitions at the top of the file. Only inject content into the body.
3. **Hand-off & Compilation**:
   - Instruct the user to upload the generated `.tex` file (and `resume.cls`) to Overleaf.
   - The user will manually compile the document in Overleaf. (No local compilation).

## 10. ATS Mastery & Formatting (>90% Score Factors)
To achieve a >90% ATS score, strict adherence to these research-backed factors is non-negotiable:

### A. Formatting (The Parse Layer)
1. **No Columns or Tables**: Layout parsing is the #1 failure point. Use a single-column layout only.
2. **No Graphics/Images**: Icons, logos, and photos are unreadable to many parsers.
3. **Standard Fonts**: Arial, Helvetica, Times New Roman, or LaTeX defaults.
4. **Contact Info in Body**: Ensure contact details are in the main document body, not hidden in the header/footer.
5. **Cleanliness**: Avoid text boxes, background shading, or decorative lines.

### B. Content Optimization (The Rank Layer)
6. **Exact Keyword Matching**: If JD says "ML", use "Machine Learning (ML)". If JD says "Python", use "Python".
7. **Frequency Strategy**: High-value keywords should appear 2-3 times (e.g., in Skills AND Work Experience).
8. **Acronym Rule**: Always use "Full Term (Acronym)" on first use (e.g., "Standard Operating Procedure (SOP)").
9. **Quantifiable Metrics**: ATS algorithms score "Managed team" lower than "Managed team of 10". Usage of numbers indicates authority.

### C. LaTeX Technical Rules
10. **LaTeX Syntax**: **ALWAYS** use `\textbf{text}` for bolding. **NEVER** use markdown `**text**`.
11. **Spacing Consistency**: Do **NOT** use manual `\vspace{}` adjustments in titles.
12. **Standardized Margins**: Use `0.5in` margins for maximum real estate.
13. **Hyperlinks**: Use `\href{url}{display_text}`.
14. **Header Consistency**: `Name, (Certs)` format.

## 11. Line Efficiency (Real Estate Optimization)
Resume real estate is precious. Avoid "orphaned" words on a new line or lines that are less than 75% full.
- **Rule of Thumb:** A standard resume line holds approximately **115-120 characters**.
- **Constraint:** If a bullet point spills over to a second line by only 1-5 words, either:
    1. **Cut:** Condense the text to fit on a single line.
    2. **Expand:** Add more detail (metrics/tech stack) to fill the second line to at least 80%.

## 12. Quality Assurance (QA) Rubric
Before finalizing content, verify:
- [ ] **The "So What?" Test:** Does every bullet explain *why* it mattered?
- [ ] **Metric Check:** Is there a number (Y) or qualitative impact?
- [ ] **Tech Stack Audit:** Are the JD tools actually mentioned in the bullet points?
- [ ] **Formatting:** Are bullets under 2 lines?
- [ ] **Syntax Check:** Verify NO markdown bolding (`**`) exists in the LaTeX code. Search for `**` and replace with `\textbf{}` if found.

## 13. Master Agent Prompt
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
2. **Quantify:** Use specific numbers, percentages, and metrics wherever possible. If exact numbers are missing, estimate reasonable metrics based on industry standards.
3. **Keywords & Acronyms:** Integrate keywords naturally. **ALWAYS** use the format "Full Term (Acronym)" for the first mention (e.g., "Large Language Models (LLMs)").
4. **Dates:** Ensure any dates you generate follow the standard "MM/YYYY" or "Month Year" format.
5. **Action Verbs:** Start every bullet with a strong power verb (e.g., Architected, Engineered, Deployed, Optimized).
6. **Bolding:** You **MUST** use `\textbf{text}` for bolding. Do **NOT** use markdown `**text**` syntax.
7. **Format:** Output the result as LaTeX code compatible with the `resume.cls` format (using `\item`). Do not use tables or columns.

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

## 14. Cover Letter Strategy (The "Bridge" Narrative)
For Technical Product Management (TPM) roles, the cover letter must bridge the gap between "Builder" and "Strategist".

### Core Rules (Non-Negotiable):
1.  **Format**: Generic Markdown. **Do NOT use placeholders** like `[Company Name]`. Use universal terms like "your team", "the organization", or "this opportunity".
2.  **Date**: **Do NOT include a date.** The letter must be timeless.
3.  **Layout**:
    -   **Header**: Contact info must be on **separate lines**.
    -   **URLs**: Must be clickable link format `[url](url)`.
    -   **Signature**: "Sincerely," and Name must be separated by a newline.
4.  **Narrative Focus**: Prioritize **Work Ethic, Culture, and Mindset** (e.g., "Act like an Owner", "Builder Mindset") over just listing skills.

### Key Components (The 4-Paragraph Structure):
1.  **The Hook (The "Why You"):** State your specific value proposition immediately (e.g., "Merging engineering depth with product strategy...").
2.  **The "Bridge" (Technical Literacy):** proactively demonstrate you speak the language of engineering. Mention specific stacks (e.g., "Having architected LangGraph agents...").
3.  **The Evidence (Builder Outcomes):** Pick ONE hero project. Go deep. Use the **STAR** method (Situation, Task, Action, Result) but keep it punchy.
4.  **The Close (Call to Action):** Reiterate enthusiasm and invite the conversation.

### Success Factors:
-   **Show, Don't Tell:** Instead of saying "I am technical", say "I built a multi-agent system using FastAPI".
-   **Narrative Consistency:** Ensure the "Builder" persona in the resume matches the voice in the cover letter.
-   **Brevity:** Max 300-350 words.
