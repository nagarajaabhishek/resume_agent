# 🚀 AI Agent for High-Impact Resume Generation
> **Status:** Production-Ready (ATS Score > 90%) | **Resumes:** ≤ 2 Pages Enforced
> **Architecture:** YAML Data → Python Logic → LaTeX Output → PDF

This repository hosts a sophisticated **Resume Engineering System** designed to automate the creation of high-impact, ATS-optimized resumes. It enforces the **XYZ Strategy** and strict formatting rules to ensure every resume passes both automated scanners and human review.

---

## 📣 Updates & Announcements
* **Mar 2026:** Added Dubai Market specific role templates and optimizations.
* **Feb 2026:** Gemini JD Validation prompt implemented for tighter application targeting.

---

## ⚡ Start in 60 Seconds
Generate a resume instantly from an existing role profile.

```bash
# Generate a resume for a specific role
python3 .agent/scripts/generate_resume.py .agent/data/Abhishek/<role_file>.yaml

# Examples:
python3 .agent/scripts/generate_resume.py .agent/data/Abhishek/role_tpm.yaml
```

Output `.tex` files land in `Resume_Building/Abhishek/<RoleName>/` when `meta.filename` includes that path; bare filenames go to `Resume_Building/Abhishek/Generated/`. **PDFs are always written next to the `.tex`** (`pdflatex -output-directory` / `tectonic --outdir` under the person folder).

---

## 🌟 What Makes This Different (The "Secret Sauce")

* ✅ **Strict XYZ Pattern:** Every bullet follows: *"Accomplished [X] as measured by [Y], by doing [Z]"*. Weak verbs and vague claims are banned.
* ✅ **2-Page Hard Limit:** Role YAMLs are pruned to maximize impact within a strict 2-page boundary. Low-ROI bullets are cut, not softened.
* ✅ **Line Efficiency Algorithm:** Calculates character density to maximize readable space (~115–120 chars/line) with no orphan lines.
* ✅ **Role-Based Tailoring:** Experience data is stored once in `master_context.yaml` and forked into role-specific YAMLs (TPM, PO, GTM, etc.) without duplication.
* ✅ **ATS-Safe LaTeX Templates:** A custom `resume.cls` class enforces rigid structure, margins, and hierarchy. You write data (YAML), LaTeX renders the pixel-perfect PDF.

---

## 💼 Real-World Use Cases

* **"I need to apply to a specific job posting."**
  → Run the **[Tailor Resume](.agent/workflows/tailor_resume.md)** workflow + **[JD Validation](Resume_Building/gemini_JD_Validation.md)** prompt.
* **"I just finished a new certification or job."**
  → Run the **[Update Master Profile](.agent/workflows/update_master_profile.md)** workflow to update the Single Source of Truth.
* **"I need to check if my formatting will pass ATS."**
  → Run the **[Audit & QA](.agent/workflows/audit_resume.md)** workflow.
* **"I found skill gaps in a JD and want to learn them."**
  → Run the **[Process JD Keywords](.agent/workflows/process_jd_keywords.md)** workflow to update your learning roadmap.

---

## 🤖 Agent Routing Instructions
This repository is an **agent-ready environment**. If you are an AI reading this source code:
1. **Never scan folders blindly**: Go straight to `.agent/catalog/skills-by-type.md` or `.agent/catalog/commands-index.yaml` to discover capabilities in O(1) time.
2. **Context Isolation**: Each item in `.agent/skills/` is isolated. Navigate to its `SKILL.md` to parse its strict schema and YAML frontmatter.
3. **Execution Safety**: Code strictly meant for execution (and not prompt logic) lives in `.agent/scripts/` or `/scripts/`. Do not attempt to parse them for contextual logic.

---

## 📂 System Architecture

```text
/Resume_Agent
  /.agent
    /catalog/                   # Generative routing indexes (O(1) lookup tables)
    /data/Abhishek/             # Single Source of Truth (YAML)
      master_context.yaml       # All biographical history
      ...                       # role_*.yaml files
    /skills/                    # Core isolated agent skills (One per folder)
    /workflows                  # Orchestration commands & Process docs
    /templates                  # Jinja2 → LaTeX template
  /scripts                      # Auxiliary management/execution scripts
  /docs                         # Non-executable documentation/blogs
  /Resume_Building              # Generated outputs and JD Validation
```

---

## 🛠️ Mandatory Workflows

**Protocol:** All resume operations must follow these strict guides to maintain quality and avoid data drift.

1. **[Update Master Profile](.agent/workflows/update_master_profile.md):** Always update `master_context.yaml` first. Never edit a role YAML directly for biographical data.
2. **[Create / Tailor Resume](.agent/workflows/create_resume.md) · [Tailoring Guide](.agent/workflows/tailor_resume.md):** Fork from the Master, prune low-impact bullets, tune keywords to the JD.
3. **[Process JD Keywords](.agent/workflows/process_jd_keywords.md):** Inject "Fits" into the YAMLs. Append "Discards" to learning roadmap.
4. **[Audit & QA](.agent/workflows/audit_resume.md) · [Audit Cover Letter](.agent/workflows/audit_cover_letter.md):** Run the 4-Phase Protocol.
5. **[JD Validation](Resume_Building/gemini_JD_Validation.md):** Use the Gemini prompt to analyze job listings.

---

## 📋 Current Resume Inventory (Abhishek)

<details>
<summary>Click to view all tailored resumes</summary>

| Role | YAML | Resume | Cover Letter |
|---|---|---|---|
| Technical Program Manager | `role_tpm.yaml` | `Abhishek_Nagaraja_TPM_Resume.tex` | ✅ |
| Product Owner | `role_po.yaml` | `Abhishek_Nagaraja_PO_Resume.tex` | ✅ |
| GTM / Solutions Engineer | `role_gtm.yaml` | `Abhishek_Nagaraja_GTM_Resume.tex` | ✅ |
| Business Analyst | `role_ba.yaml` | `Abhishek_Nagaraja_BA_Resume.tex` | ✅ |
| Delivery Manager | `role_manager.yaml` | `Abhishek_Nagaraja_Manager_Resume.tex` | ✅ |
| Scrum Master | `role_sm.yaml` | `Abhishek_Nagaraja_SM_Resume.tex` | ✅ |
| Dubai Market | `role_dubai.yaml` | `Abhishek_Nagaraja_Dubai_Resume.tex` | ✅ |

</details>

---

## 📄 License
MIT License. Built by Antigravity.
