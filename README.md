# 🚀 AI Agent for High-Impact Resume Generation
> **Status:** Production-Ready (ATS Score > 90%)
> **Architecture:** YAML Data → Python Logic → LaTeX Output

This repository hosts a sophisticated **Resume Engineering System** designed to automate the creation of high-impact, ATS-optimized resumes. It enforces the "XYZ Strategy" and strict formatting rules to ensure every resume passes both automated parsers and human review.

## 🏆 The "Secret Sauce" (Why >90%?)
1.  **Strict XYZ Pattern**: Every bullet point must follow the formula: *"Accomplished [X] as measured by [Y], by doing [Z]"*. Weak verbs and vague claims are banned.
2.  **Line Efficiency Algorithm**: The system calculates character density to ensure every bullet point maximizes its readable space (approx. 115-120 chars/line).
3.  **Role-Based Tailoring**: Data is separated from formatting, allowing you to "fork" your experience into diverse roles (e.g., TPM vs. Product Manager) without duplicating effort.
4.  **ATS-Safe LaTeX**: The underlying `resume.cls` uses standard fonts, clear headings, and parse-friendly structures to ensure perfect keyword extraction.

## 📂 System Architecture
```
/Resume_Agent
  /.agent
    /data/[PersonName]/        # Single Source of Truth (YAML)
      master_context.yaml      # All your history (DO NOT EDIT RESUMES DIRECTLY)
      role_tpm.yaml            # Tailored data for specific roles
    /skills/resume_generation  # The "Brain" (Rules & Logic)
      SKILL.md                 # The Master Index
    /workflows                 # Process Documentation
    /scripts                   # Python Generation Engine
  /Resume_Building
    /Generated                 # Output PDFs and LaTeX files
```

## 🛠️ Mandatory Workflows
**Protocol**: All resume operations must follow these strict guides to maintain quality.

### 1. [Update Master Profile](.agent/workflows/update_master_profile.md)
**When:** You have a new job, degree, or certification.
**Rule:** Always update `master_context.yaml` first. Never edit a role file directly for biographical data.

### 2. [Create / Tailor Resume](.agent/workflows/create_resume.md) | [Tailoring Guide](.agent/workflows/tailor_resume.md)
**When:** Applying to a specific role.
**Rule:** Fork from the Master, prune irrelevant experience, and tune keywords.

### 3. [Audit & Quality Assurance](.agent/workflows/audit_resume.md)
**When:** Before hitting "Submit".
**Rule:** Run the 4-Phase Protocol: Automated Checks -> Content Audit (XYZ) -> Visual Audit -> Final PDF.

## 🚀 Usage
The entire system is driven by a single Python command.

```bash
# 1. Generate a resume from a specific data file
python3 .agent/scripts/generate_resume.py .agent/data/[PersonName]/[role_file].yaml

# Example:
python3 .agent/scripts/generate_resume.py .agent/data/Abhishek/role_tpm.yaml
```

## 📄 License
MIT License. Built by Antigravity.
