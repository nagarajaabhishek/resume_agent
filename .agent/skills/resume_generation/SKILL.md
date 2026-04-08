---
name: Resume Generation
description: A modular skill for generating high-impact, ATS-optimized resumes using the XYZ strategy and LaTeX templates.
intent: To standardize and automate the creation of 2-page, highly effective ATS resumes from YAML data.
type: generation
best_for: Tailoring, generating, and formatting technical resumes.
scenarios:
  - User wants to apply to a specific job.
  - User finished a new certification and needs to update their resume.
  - User needs to QA an existing resume.
---

# Resume Generation

> **🚨 AGENT PROTOCOL:** This skill is modular. Before any generation or analysis, you MUST consult this Master Index and refer to the specific rule files in the `rules/` directory as needed.

## Purpose
To ensure every generated resume passes automated ATS scanners and human review by enforcing the XYZ Strategy, a strict 2-page limit, and dense, metrics-driven bullet points formatted precisely in LaTeX.

## Key Concepts

### Core Principles (The Hierarchy of Impact)
1. **ATS First**: Ensure exact keyword matches to "unlock" the resume for human review.
2. **XYZ Strategy**: Use the "Accomplished [X] as measured by [Y], by doing [Z]" formula for all achievements.
3. **Double-Line Symmetry**: Target **215-245 characters** per bullet to ensure every achievement occupies exactly two lines for visual densification.
4. **Full Month Names**: **ALWAYS** use full month names (e.g., "January", "August"). Never abbreviate ("Jan", "Aug").
5. **Show, Don't Tell**: Use concrete engineering outcomes instead of generic skill claims.
6. **Standard Formatting**: Single-column, standard headings, and specific font settings.

### Modular Rule Components
Consult these sub-documents for specific implementation details:
- **[LaTeX Formatting](file:///Users/abhisheknagaraja/Documents/Resume_Agent/.agent/skills/resume_generation/rules/latex_formatting.md):** Font (Charter), spacing, bolding syntax (`\textbf{}`), and ATS-safe layout.
- **[Content Strategy (XYZ)](file:///Users/abhisheknagaraja/Documents/Resume_Agent/.agent/skills/resume_generation/rules/content_strategy.md):** XYZ formula, keyword engineering, metric estimation, and anti-patterns.
- **[Line Efficiency](file:///Users/abhisheknagaraja/Documents/Resume_Agent/.agent/skills/resume_generation/rules/line_efficiency.md):** Real estate optimization, 215-245 character rule, and visual symmetry.
- **[Role-Based Guidelines](file:///Users/abhisheknagaraja/Documents/Resume_Agent/.agent/skills/resume_generation/rules/role_guidelines.md):** Tuning vocabulary, focus, and AI Enhancement strategies.
- **[Cover Letter Rules](file:///Users/abhisheknagaraja/Documents/Resume_Agent/.agent/skills/resume_generation/rules/cover_letter_rules.md):** Timelessness, 4-paragraph structure, and branding consistency.

## Application

### The Audit Hierarchy
To ensure high-impact resumes, follow this specific order of operations during analysis and generation:
1.  **Double-Line Visual Symmetry**: Every bullet point point MUST be **215-245 characters**. If too short, **EXPAND**.
2.  **Date Quality**: All dates must use full month names. Zero abbreviations allowed.
3.  **Role Alignment & Vocabulary**: Consult the Role-Based Guidelines. Use role-specific high-value keywords.
4.  **Action & Result (XYZ Logic)**: Mandatory "Verb + [Result] + [Action]". Use Diverse Action Verbs. NEVER start repetitive bullets with "Accomplished".
5.  **Skills Triple-Threat**: Ensure the Skills section includes Methodologies/Strategies + Tools + Hard Concepts.
6.  **Line Efficiency (Formatting)**: Ensure second lines are 80%+ full and no orphaned words exist.
7.  **Comprehensive Experience**: All resumes MUST include every professional experience listed in the Master Profile.
8.  **Project Prioritization**: Projects MUST be ordered by relevance to the target role.

### Execution Workflow
1.  **Check the Inventory**: Consult `.agent/data/[PersonName]/resume_inventory.yaml` to see active resumes.
2.  **Locate Data**: Verify the existing YAML path listed in the inventory.
3.  **Run the Script**: `python3 .agent/scripts/generate_resume.py .agent/data/[PersonName]/[role_file].yaml` is the ONLY way to build the `.tex` file.
4.  **No PDF Generation**: Antigravity is NOT responsible for compiling the `.tex` to PDF. Do not run `pdflatex`.
5.  **Do NOT Edit LaTeX Manually**: The `.tex` files are overwrite targets. Edit the YAML instead.

## Examples
Use the [Master Agent Prompt](file:///Users/abhisheknagaraja/Documents/Resume_Agent/.agent/skills/resume_generation/rules/content_strategy.md#master-agent-prompt) logic when using external AI tools to rewrite content. Ensure you look at `.agent/data/Abhishek/master_context.yaml` as the prime example of data structure.

## Common Pitfalls

### Mandatory Workflows
- **The Source of Truth Protocol**: Follow `update_master_profile.md`. **NEVER** edit a role file directly for biographical updates.
- **Creating New Resumes**: Follow `create_resume.md` or `tailor_resume.md`.
- **Content Strategy**: Follow `judge_content.md`.
- **Quality Assurance**: Follow `audit_resume.md`.

### Single Source of Truth
1.  **Master Context**: `master_context.yaml` is the **DEFINITIVE** source for all biographical data.
2.  **Propagation**: Always update `master_context.yaml` **FIRST**, then propagate changes to specific role files.
3.  **Conflict Resolution**: If a role file contradicts `master_context.yaml`, the master context is correct.

### Inventory Maintenance
- **Mandatory Update**: Whenever you create a NEW role file or change an output path, update `resume_inventory.yaml` immediately.
