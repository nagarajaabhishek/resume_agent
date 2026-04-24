---
description: A strict protocol for Verifying Resume Quality (Content & Code).
---

# Resume Audit Protocol

> **Purpose:** Ensure every resume meets the "High-Impact" standard before export.
> **Role:** Quality Assurance (QA).

## Phase 1: Automated Validation (The Gatekeeper)
**Tool:** `generate_resume.py`

1.  **Run the Script:**
    ```bash
    python3 .agent/scripts/generate_resume.py .agent/data/[Person]/[Role].yaml
    ```
2.  **Verify Output:**
    - **Pass:** Script completes with "✅ Resume Generation COMPLETE."
    - **Fail:** Script throws strict errors (e.g., "Bullet too short", "Forbidden word found").
    - *Action:* You MUST fix these errors in the YAML data. Do not override the script.

## Phase 2: Content Audit (The XYZ Test)
**Manual Checklist:** Review the YAML content.

### 1. The Structure Test (XYZ)
- [ ] **Every Bullet** follows the pattern: "Accomplished [X] as measured by [Y], by doing [Z]".
- [ ] **No Weak Verbs:** "Responsible for", "Tasked with", "Helped", "Worked on" are **BANNED**.
- [ ] **Action-First:** Bullets start with a strong power verb (e.g., "Orchestrated", "Engineered", "Spearheaded").

### 2. The Impact Test (Quantification)
- [ ] **Numbers:** Does the bullet contain a metric? ($, %, Time Saved, Users Gained).
- [ ] **Context:** Is the metric meaningful? (e.g., "Reduced latency by 50ms" vs "Reduced latency").

### 3. The Role Test (Alignment)
- [ ] **Keywords:** Does the resume contain the specific keywords from `role_guidelines.md` for this target role?
- [ ] **Relevance:** detailed engineering projects should be brief for a "Product Manager" role, and vice versa.

## Phase 3: Visual & Formatting Audit (The Polish)
**Manual Checklist:** Review the generated `.tex` code or the rendered PDF (if compiled externally).

### 1. Line Efficiency
- [ ] **The 2-Line Rule:** Are most bullets 215-245 characters to ensure they occupy 2 full lines?
- [ ] **The 80% Rule:** If a bullet wraps to a second line, does it fill at least 80% of that line visually?
- [ ] **No Orphans:** Are there single words on a line? (Rewrite to fix).

### 2. Formatting & Links
- [ ] **Hyperlinks:** Click every link (GitHub, LinkedIn, Projects). Do they work?
- [ ] **Dates:** Are dates consistent and correct?
- [ ] **Spacing:** Is there awkward white space? (Adjust content to fill).

## Phase 4: Final Approval
- If all checks pass, the resume is ready for submission.
