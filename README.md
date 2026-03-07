# 🚀 AI Agent for High-Impact Resume Generation
> **Status:** Production-Ready (ATS Score > 90%) | **Resumes:** ≤ 2 Pages Enforced
> **Architecture:** YAML Data → Python Logic → LaTeX Output → PDF

This repository hosts a sophisticated **Resume Engineering System** designed to automate the creation of high-impact, ATS-optimized resumes. It enforces the **XYZ Strategy** and strict formatting rules to ensure every resume passes both automated scanners and human review.

---

## 🏆 The "Secret Sauce" (Why >90%?)

1. **Strict XYZ Pattern** — Every bullet follows: *"Accomplished [X] as measured by [Y], by doing [Z]"*. Weak verbs and vague claims are banned.
2. **2-Page Hard Limit** — Role YAMLs are pruned to maximize impact within a strict 2-page boundary. Low-ROI bullets are cut, not softened.
3. **Line Efficiency Algorithm** — The generator calculates character density to maximize readable space (~115–120 chars/line) with no orphan lines.
4. **Role-Based Tailoring** — Experience data is stored once in `master_context.yaml` and forked into role-specific YAMLs (TPM, PO, GTM, BA, Manager, Dubai, Scrum Master) without duplication.
5. **ATS-Safe LaTeX Templates** — A custom `resume.cls` class enforces rigid structure, margins, and hierarchy. You write data (YAML), LaTeX renders the pixel-perfect PDF.

---

## 📂 System Architecture

```
/Resume_Agent
  /.agent
    /data/Abhishek/             # Single Source of Truth (YAML)
      master_context.yaml       # All biographical history (DO NOT EDIT RESUMES DIRECTLY)
      role_tpm.yaml             # TPM-tailored data
      role_po.yaml              # Product Owner-tailored data
      role_gtm.yaml             # GTM / Solutions Engineer-tailored data
      role_ba.yaml              # Business Analyst-tailored data
      role_manager.yaml         # Engineering / Delivery Manager
      role_sm.yaml              # Scrum Master
      role_dubai.yaml           # Dubai market optimized
    /skills/resume_generation   # The "Brain" (Rules & Logic)
      SKILL.md                  # Master index — all formatting rules
    /workflows                  # Process documentation (tailoring, auditing, cover letters)
    /templates
      resume_template.tex.j2    # Jinja2 → LaTeX template
  /scripts                      # Auxiliary management & audit scripts
  /docs                         # Marketing and public content
  /Resume_Building/Abhishek     # Generated .tex and compiled .pdf outputs
    /Business_Analyst/
    /Dubai/
    /GTM/
    /Manager/
    /Product/                   # TPM role
    /Product_Owner/
    /Scrum_Master/
```

---

## 🛠️ Mandatory Workflows

**Protocol:** All resume operations must follow these strict guides to maintain quality and avoid data drift.

### 1. [Update Master Profile](.agent/workflows/update_master_profile.md)
**When:** New job, degree, certification, or project.
**Rule:** Always update `master_context.yaml` first. Never edit a role YAML directly for biographical data.

### 2. [Create / Tailor Resume](.agent/workflows/create_resume.md) · [Tailoring Guide](.agent/workflows/tailor_resume.md)
**When:** Applying to a specific role or company.
**Rule:** Fork from the Master, prune low-impact bullets, tune keywords to the JD.

### 3. [Process JD Keywords](.agent/workflows/process_jd_keywords.md)
**When:** After extracting keyword gaps from a Job Description.
**Rule:** Inject "Fits" into the Master Context / Role YAML. Append "Discards" to `learning_roadmap.md` for future skill acquisition.

### 4. [Audit & QA](.agent/workflows/audit_resume.md) · [Audit Cover Letter](.agent/workflows/audit_cover_letter.md)
**When:** Before submitting any application.
**Rule:** Run the 4-Phase Protocol: Automated Checks → Content Audit (XYZ) → Visual Audit of `.tex` → Final Output.

> **🚨 Compilation Note:** The agent handles YAML-to-LaTeX templating. It does **not** compile the final PDF. Compile `.tex` files locally using `tectonic` or `pdflatex`.

---

## 🚀 Usage

```bash
# Generate a resume for a specific role
python3 .agent/scripts/generate_resume.py .agent/data/Abhishek/<role_file>.yaml

# Examples:
python3 .agent/scripts/generate_resume.py .agent/data/Abhishek/role_tpm.yaml
python3 .agent/scripts/generate_resume.py .agent/data/Abhishek/role_ba.yaml
python3 .agent/scripts/generate_resume.py .agent/data/Abhishek/role_gtm.yaml
```

Output `.tex` files land in `Resume_Building/Abhishek/<RoleName>/`.

---

## 📋 Current Resume Inventory (Abhishek)

| Role | YAML | Resume | Cover Letter |
|---|---|---|---|
| Technical Program Manager | `role_tpm.yaml` | `Abhishek_Nagaraja_TPM_Resume.tex` | ✅ |
| Product Owner | `role_po.yaml` | `Abhishek_Nagaraja_PO_Resume.tex` | ✅ |
| GTM / Solutions Engineer | `role_gtm.yaml` | `Abhishek_Nagaraja_GTM_Resume.tex` | ✅ |
| Business Analyst | `role_ba.yaml` | `Abhishek_Nagaraja_BA_Resume.tex` | ✅ |
| Delivery Manager | `role_manager.yaml` | `Abhishek_Nagaraja_Manager_Resume.tex` | ✅ |
| Scrum Master | `role_sm.yaml` | `Abhishek_Nagaraja_SM_Resume.tex` | ✅ |
| Dubai Market | `role_dubai.yaml` | `Abhishek_Nagaraja_Dubai_Resume.tex` | ✅ |

---

## 📄 License
MIT License. Built by Antigravity.
