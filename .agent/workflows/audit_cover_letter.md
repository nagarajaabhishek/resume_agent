---
description: A strict protocol for validating Cover Letter formatting, timelessness, and narrative impact.
---

# Cover Letter Audit Protocol

> **Purpose:** Ensure every cover letter is ATS-ready, aesthetically premium, and aligned with the "Builder" narrative before submission.
> **Role:** Quality Assurance (QA).

## Phase 1: Automated Validation (The Script)
**Tool:** `verify_resume.py`

When compiling resumes (e.g., using `python3 scripts/verify_resume.py`), the script automatically flags the following fatal errors in Cover Letters:
- **[FATAL] Date Usage:** The `\today` command is strictly banned. Cover letters must be timeless.
- **[FATAL] Unfilled Placeholders:** Brackets like `(Role)` must be completely resolved. Note: As a rule, we DO NOT include the company name in cover letters, only the targeted Role name.
- **[FATAL] Signature Bloat:** Signature spacing must be exactly `1.2em` (not 2.5em).
- **[FATAL] Line Spacing:** The document must enforce `\setstretch{1.15}` for a premium aesthetic.
- **[FATAL] Header Mismatch:** The header must perfectly echo the resume header (e.g., "Abhishek Nagaraja", "Dallas, Texas").

*Action:* If `verify_resume.py` outputs a warning for a `.tex` file containing "Cover_Letter", you MUST fix the structural error in the LaTeX source before proceeding.

## Phase 2: Narrative Audit (The Intangibles Check)
**Checklist:** The primary goal of the cover letter is to convey what the resume cannot—your work ethic, purpose, culture fit, and leadership philosophy. Review the narrative against these pillars:

### 1. The Hook & Purpose (Paragraph 1)
- [ ] **Purpose-Driven:** Does the opening explain *why* you are drawn to the role or industry on a personal/professional level, beyond just stating the title?
- [ ] **Immediate Value:** Does it clearly articulate your overarching professional philosophy (e.g., bridging engineering with commercial success)?
- [ ] **Company Agnostic:** Does the letter focus purely on the target **Role name** without explicitly mentioning the target Company's name?
- [ ] **No Fluff:** Does it avoid generic openings like "I am writing to apply for..."?

### 2. The Culture & Execution (Paragraph 2 & 3)
- [ ] **Beyond the Bullet Point:** Instead of just repeating resume metrics, does the letter explain *how* you operate (e.g., your work ethic, cross-functional collaboration, or how you tackle ambiguity)?
- [ ] **Team Building & Network:** Do you highlight your ability to build culture, foster communities (like Mavs Entrepreneurs or MavMarket), and align diverse stakeholders (engineering vs. business)?
- [ ] **Technical Empathy:** Does the letter demonstrate your technical literacy (CS background) as a tool for better collaboration and leading teams, rather than just a list of hard skills?

### 3. The Call to Action (Paragraph 4)
- [ ] **The "Builder" Mindset:** Does the closing reiterate a desire for "deep ownership", "team success", and "scaling high-impact products"?
- [ ] **Confident Tone:** Does it end confidently ("I look forward to the possibility...") without sounding desperate or overly deferential?

## Phase 3: Visual & Final Audit
- [ ] **Naming Convention:** The final PDF file MUST be named explicitly using the format: `[FirstName]_[LastName]_[Role]_CL.pdf` (e.g., `Abhishek_Nagaraja_GTM_CL.pdf`).
- [ ] **One Page Rule:** The document must comfortably fit on a single page without crowding the margins.
- [ ] **Premium Typography:** Check that paragraph spacing (`\usepackage[parfill]{parskip}`) is working correctly (no indents, clean breaks between paragraphs).
- [ ] **Proofreading:** Run a final check over the text specifically looking for awkward grammar caused by merging different template parts.
