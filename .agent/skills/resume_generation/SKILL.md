---
name: Resume Generation
description: A modular skill for generating high-impact, ATS-optimized resumes using the XYZ strategy and LaTeX templates.
---

# Master Resume Instructions (Master Index)

> **🚨 AGENT PROTOCOL:** This skill is modular. Before any generation or analysis, you MUST consult this Master Index and refer to the specific rule files in the `rules/` directory as needed.

## 1. Core Principles (The Hierarchy of Impact)
1. **ATS First**: Ensure exact keyword matches to "unlock" the resume for human review.
2. **XYZ Strategy**: Use the "Accomplished [X] as measured by [Y], by doing [Z]" formula for all achievements.
3. **Prioritize by Impact**: Most impressive/relevant achievement goes first.
4. **Show, Don't Tell**: Use concrete engineering outcomes instead of generic skill claims.
5. **Standard Formatting**: Single-column, standard headings, and specific font settings.

## 2. Modular Rule Components
Consult these sub-documents for specific implementation details:

- ### [LaTeX Formatting](file:///Users/abhisheknagaraja/Documents/Resume_Agent/.agent/skills/resume_generation/rules/latex_formatting.md)
  *Font (Charter), spacing, bolding syntax (`\textbf{}`), and ATS-safe layout.*
- ### [Content Strategy (XYZ)](file:///Users/abhisheknagaraja/Documents/Resume_Agent/.agent/skills/resume_generation/rules/content_strategy.md)
  *XYZ formula, keyword engineering, metric estimation, and anti-patterns.*
- ### [Line Efficiency](file:///Users/abhisheknagaraja/Documents/Resume_Agent/.agent/skills/resume_generation/rules/line_efficiency.md)
  *Real estate optimization, 115-120 character rule, and orphan management.*
- ### [Role-Based Guidelines](file:///Users/abhisheknagaraja/Documents/Resume_Agent/.agent/skills/resume_generation/rules/role_guidelines.md)
  *Tuning vocabulary, focus, and **AI Enhancement** strategies (Ops/DevEx/Discovery) for GTM, Engineering, PM, and Operations roles.*
- ### [Cover Letter Rules](file:///Users/abhisheknagaraja/Documents/Resume_Agent/.agent/skills/resume_generation/rules/cover_letter_rules.md)
  *Timelessness, 4-paragraph structure, and branding consistency.*

## 3. Core Principles (The Audit Hierarchy)
To ensure high-impact resumes, follow this specific order of operations during analysis and generation:

1.  **Substantial Depth (The 2-Line Rule)**: **NEVER** condense content to fit space. If a bullet is too short, **EXPAND** with technical implementation details, specific tools, or sub-processes. Every bullet point should ideally be **two full lines**.
2.  **Role Alignment & Vocabulary**: Consult the [Role-Based Guidelines](file:///Users/abhisheknagaraja/Documents/Resume_Agent/.agent/skills/resume_generation/rules/role_guidelines.md) first. Use role-specific high-value keywords.
3.  **Action & Result (XYZ Logic)**: Mandatory "Verb + [Result] + [Action]". Use **Diverse Action Verbs** (see Content Strategy). **NEVER** start repetitive bullets with "Accomplished".
4.  **AI Enhancement**: Explicitly show how Generative AI or Agentic Workflows were used as force multipliers for that specific role.
5.  **Skills Triple-Threat**: Ensure the Skills section includes **Methodologies/Strategies** + **Tools** + **Hard Concepts**.
6.  **Line Efficiency (Formatting)**: Only after the content is rich, adjust for [Line Efficiency](file:///Users/abhisheknagaraja/Documents/Resume_Agent/.agent/skills/resume_generation/rules/line_efficiency.md). Ensure second lines are **80%+ full** and no orphaned words exist.
7.  **Comprehensive Experience**: All resumes MUST include **every** professional experience listed in the Master Profile. Prioritize their order based on relevance to the specific role, but never omit valid work history.
8.  **Project Prioritization**: Resumes should list a comprehensive set of projects (6+). Projects MUST be ordered by relevance to the target role. **Content Tailoring**: Primarily achieve this through ordering. If a role requires a completely different angle, **create a new project entry** in the Master Profile rather than editing an existing one in place.

## 4. Master Agent Prompt (For External Interaction)
Use the [Master Agent Prompt](file:///Users/abhisheknagaraja/Documents/Resume_Agent/.agent/skills/resume_generation/rules/content_strategy.md#master-agent-prompt) logic when using external AI tools to rewrite content.

## 5. Critical Error Prevention (Recurring Mistakes to Avoid)

### 📋 MANDATORY WORKFLOWS (Process Engineering)

**1. The Source of Truth Protocol**:
- Follow [Update Master Profile](file:///Users/abhisheknagaraja/Documents/Resume_Agent/.agent/workflows/update_master_profile.md) when adding new jobs, degrees, or certifications.
- **NEVER** edit a role file directly for biographical updates.

**2. Creating New Resumes**:
- Follow [Create Resume](file:///Users/abhisheknagaraja/Documents/Resume_Agent/.agent/workflows/create_resume.md) for standard generation.
- Follow [Tailor Resume](file:///Users/abhisheknagaraja/Documents/Resume_Agent/.agent/workflows/tailor_resume.md) when splitting a new niche resume from the Master.
    
**3. Quality Assurance**:
- Follow [Resume Audit Protocol](file:///Users/abhisheknagaraja/Documents/Resume_Agent/.agent/workflows/audit_resume.md) for mandatory QC before any submission.

### 🚨 BEFORE Starting Any Resume Work:
1.  **Locate Data**: Check `.agent/data/[PersonName]/` for existing YAML files (e.g., `.agent/data/Abhishek/role_tpm.yaml`).
2.  **Run the Script**: `python3 .agent/scripts/generate_resume.py .agent/data/[PersonName]/[role_file].yaml` is the ONLY way to build.
3.  **Do NOT Edit LaTeX Manually**: The `.tex` files in `Resume_Building/Generated/` (or custom output paths) are overwrite targets. Edit the YAML instead.
### 🚨 SINGLE SOURCE OF TRUTH (DATA HIERARCHY)
1.  **Master Context**: `master_context.yaml` is the **DEFINITIVE** source for all biographical data.
2.  **Organization Standards**:
    - **Directory**: `.agent/data/[PersonName]/` (e.g., `Abhishek/`).
    - **Role Files**: `role_[job_title].yaml` (snake_case).
    - **Resume Output**: `Resume_Building/[PersonName]/[Domain]/[Name]_[Role]_Resume.tex`.
3.  **Propagation**: Always update `master_context.yaml` **FIRST**, then propagate changes to specific role files.
3.  **Conflict Resolution**: If a role file contradicts `master_context.yaml`, the master context is correct (unless it's a specific tailoring choice).

---

---
*Created by Antigravity - Optimized for High-Impact Technical Branding.*
