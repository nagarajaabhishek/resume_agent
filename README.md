# 🚀 Resume Agent — Agentic ATS Resume Engineering System

> **Status:** Production-Ready | **Layout:** 1–2 Pages (Charter Serif, Single-Column ATS-Safe)  
> **Pipeline:** Raw Context Artifacts → `master_context.yaml` → `role_*.yaml` → Validation → LaTeX (`.tex`) → PDF

This repository is an **agent-ready resume engineering system** that turns raw career artifacts (old resumes, LinkedIn exports, legal employment records, target JDs, and project links) into validated, ATS-optimized, metrics-driven LaTeX/PDF resumes.

---

## 🛠️ Prerequisites (One-Time Setup)

```bash
# 1. Create virtual environment & install Python dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 2. Install Tectonic for local PDF compilation (macOS)
brew install tectonic
```

> **Note:** `generate_resume.py` automatically detects `.venv/lib/python3.12/site-packages` if present.

---

## 🧭 New Person Onboarding: Step-by-Step Guide (With AI Starter Prompts)

Whether you are building your resume manually or driving an AI coding agent (Antigravity, Claude Code, Cursor, etc.), follow these steps in order. Each step includes a copy-paste **AI Starter Prompt**.

---

### Step 1: Collect Raw Context Artifacts & Align Strategy
Create an intake folder `Resume_Building/<PersonName>/` and drop in your raw context files:

1. **Existing Resume PDF(s):** Baseline experience, metrics, and projects.
2. **LinkedIn Profile PDF (`Profile.pdf`):** Full work timeline, older roles, certifications, and publications.
3. **Official / Legal Chronology Docs (if applicable):** Offer letters, employment verifications, or visa/H-1B filings to reconcile legal employer names, acquisition transitions, and exact start/end months.
4. **Target Positioning & Preferences:**
   - **Target Roles & Companies:** Roles you are targeting (e.g., *AI Engineer, Forward Deployed Engineer, TPM*) and target JDs/domains.
   - **Years of Experience (YOE):** Total experience to highlight in your summary (e.g., `3+ years`).
   - **Section Order & Page Cap:** Desired order (e.g., `experience → projects → education → skills → certifications`) and page limit (`1` or `2` pages).
   - **Formatting & Title Preferences:** E.g., dropping `"Intern"` from titles, hiding project dates (`dates: null`), or spotlighting flagship products/domains.
5. **Verified URLs:** Company websites, live product solution pages, GitHub repositories, LinkedIn, and portfolio/Linktree.

#### 🤖 AI Starter Prompt — Step 1 (Context Intake & Reconciliation)
```text
We are starting a new resume profile for <Person Name>.
First, read `AGENTS.md`, `.agent/skills/resume_generation/SKILL.md`, and all rule files in `.agent/skills/resume_generation/rules/`.
Then review all raw context files inside `Resume_Building/<PersonName>/` (existing resume PDF, LinkedIn `Profile.pdf`, official/legal employment docs, and strategy/JD notes).

Target Preferences:
- Target Roles / Domain: <e.g., AI Engineer, Forward Deployed Engineer — Healthcare AI>
- Years of Experience (YOE): <e.g., 3+ years>
- Section Order & Page Cap: <e.g., experience -> projects -> education -> skills -> certifications, 2 pages max>
- Title / Date / Product Preferences: <e.g., remove "Intern" from titles, hide project dates, spotlight flagship products X & Y>

Before writing any YAML:
1. List all date, title, or employer-name discrepancies across the documents so we can reconcile them.
2. Flag any unsubstantiated metrics or missing company/product/GitHub URLs we should confirm.
3. Recommend our target positioning, summary framing, and which experiences/projects to prioritize.
```

---

### Step 2: Initialize Your Data Directory & Build `master_context.yaml`
Copy the starter template folder to create your isolated profile directory:

```bash
cp -r .agent/data/_template .agent/data/<PersonName>
mkdir -p Resume_Building/<PersonName>/Master
cp resume.cls Resume_Building/<PersonName>/Master/
```

Populate `.agent/data/<PersonName>/master_context.yaml` as your **Single Source of Truth**:
- **No length cap:** Store every role, bullet, product, project, tech stack, and URL here.
- **Reconcile chronologies:** Use verified legal employer names and dates.
- **Attach URLs:** Add `url` fields on `education`, `experience`, `projects`, and `publications`—the template renders them as clickable `\href{url}{name}` links.

#### 🤖 AI Starter Prompt — Step 2 (Generate `master_context.yaml`)
```text
Let's create the Single Source of Truth for <Person Name> following `.agent/workflows/update_master_profile.md`.
1. Copy `.agent/data/_template/` into `.agent/data/<PersonName>/` and initialize `Resume_Building/<PersonName>/Master/`.
2. Populate `.agent/data/<PersonName>/master_context.yaml` using our reconciled facts, verified metrics, and company/product/GitHub URLs (look up official company or product URLs if missing).
3. Include full uncapped history, tags, `products_worked_on`, skills, certifications, and publications without inventing any unverified data.
```

---

### Step 3: Craft `role_master.yaml` (Master Resume)
Derive `.agent/data/<PersonName>/role_master.yaml` from `master_context.yaml` and register it in `.agent/data/<PersonName>/resume_inventory.yaml`. Every bullet and section must pass these strict rules:

| Rule | Requirement |
| :--- | :--- |
| **Google XYZ Formula** | `[Power Verb] + [Result/Impact] + [Metric] + by/utilizing/leveraging [Method/Tools]` |
| **2-Line Bullet Symmetry** | **215–245 characters** per bullet (excluding `\textbf{}` markup) so every bullet fills 2 full lines without orphan words |
| **Zero Forbidden Words** | Never use: *Accomplished, Responsible for, Tasked with, Helped, Managed, Participated, Worked on, Involved in, Assisted* |
| **Full Month Names** | Always write `January`, `February`, `August`, etc. (abbreviations like `Jan` fail validation) |
| **Summary Cap** | **≤ 3 lines** (~290–330 chars), stating years of experience, flagship products, stack, and domain without repeating metrics from bullets |
| **Section & Chronology Order** | Typically `experience` → `projects` → `education` → `skills` → `certifications` in reverse chronological order (`dates: null` to omit project dates) |
| **2-Page Hard Cap** | Prune lower-ROI bullets or older roles in `role_master.yaml` (keeping them safely archived in `master_context.yaml`) |

#### 🤖 AI Starter Prompt — Step 3 (Create `role_master.yaml`)
```text
Now let's build the Master Resume for <Person Name> (not a role-specific variant yet) following `.agent/workflows/create_resume.md` and `.agent/skills/resume_generation/SKILL.md`.
1. Populate `.agent/data/<PersonName>/role_master.yaml` from `master_context.yaml` and register it in `.agent/data/<PersonName>/resume_inventory.yaml`.
2. Set `meta.filename` to `Resume_Building/<PersonName>/Master/<Full_Name>_Master_Resume.tex`.
3. Enforce a <= 3-line summary (no repeated metrics), section order (`experience` -> `projects` -> `education` -> `skills` -> `certifications`), reverse chronological order, full month names, zero forbidden verbs, XYZ structure, and strict 215–245 character bullet lengths.
```

---

### Step 4: Validate, Generate `.tex`, Compile PDF, & Visual QA
Run the deterministic generator, compile the PDF, and verify the 2-page layout:

```bash
# 1. Validate rules & render LaTeX
python3 .agent/scripts/generate_resume.py .agent/data/<PersonName>/role_master.yaml

# 2. Compile PDF with Tectonic (Charter font + hyperref)
tectonic --outdir Resume_Building/<PersonName>/Master Resume_Building/<PersonName>/Master/<Full_Name>_Master_Resume.tex
# Or batch-compile all .tex resumes under your profile:
./scripts/generate_pdfs.sh <PersonName>

# 3. Verify page count (must be <= 2)
pdfinfo Resume_Building/<PersonName>/Master/<Full_Name>_Master_Resume.pdf | grep Pages
```

> **Golden Rule:** **Never edit `.tex` files manually.** Always edit the YAML and re-run `generate_resume.py`.

#### 🤖 AI Starter Prompt — Step 4 (Build, Compile & Visual QA)
```text
Validate `.agent/data/<PersonName>/role_master.yaml` using `python3 .agent/scripts/generate_resume.py`, then compile the PDF using `tectonic --outdir Resume_Building/<PersonName>/Master ...`.
Check `pdfinfo` and visually inspect every page of the rendered PDF:
- Confirm total page count is <= 2 pages and summary is <= 3 lines.
- Check for orphaned section headers, bullets split awkwardly across Page 1 and Page 2, or multi-column overlaps in Certifications.
- Fix any issues only by editing the YAML and regenerating.
```

---

### Step 5: Fork Role-Tailored Resumes or Target a Job Posting (Optional)
Once your Master Resume is locked, fork targeted variants (e.g., *Core AI Engineer* vs. *Forward Deployed Engineer*) or tailor directly to a specific Job Description without mutating `master_context.yaml`.

#### 🤖 AI Starter Prompt — Step 5 (Tailor to a Role or JD)
```text
Let's tailor a resume for <Person Name> targeting this role/JD: <paste JD or target role>.
Follow `.agent/workflows/tailor_resume.md`, `.agent/workflows/process_jd_keywords.md`, and `.agent/workflows/judge_content.md`.
1. Create `.agent/data/<PersonName>/role_<target_role>.yaml` by pulling verified experiences, projects, and skills from `master_context.yaml` (do not invent skills or metrics).
2. Reorder bullets and tune the <= 3-line summary and skills section to match exact JD terminology while keeping all bullets 215–245 chars.
3. Update `resume_inventory.yaml`, generate `.tex`, compile the 2-page PDF with `tectonic`, and run `.agent/workflows/audit_resume.md`.
```

---

## 📂 Repository Architecture

```text
/resume_agent
  ├── AGENTS.md                       # Global LaTeX Charter typography & compiler rules
  ├── requirements.txt                # Python dependencies (pyyaml, jinja2)
  ├── resume.cls                      # Shared LaTeX class definition
  ├── .agent/
  │   ├── catalog/                    # O(1) lookup indexes for agents (skills & workflows)
  │   ├── checklist/                  # Verification checklists
  │   ├── data/
  │   │   ├── _template/              # Starter YAMLs for new candidates
  │   │   └── Abhishek/               # Master context, role YAMLs, inventory, roadmap
  │   ├── scripts/                    # Core generator, role filter, URL propagator, watcher
  │   ├── skills/resume_generation/   # Modular SKILL.md + rules/ (XYZ, LaTeX, line efficiency)
  │   ├── templates/                  # Jinja2 → LaTeX templates (resume & cover letter)
  │   └── workflows/                  # Step-by-step agent protocols (create, tailor, audit, judge)
  ├── .agents/rules/                  # IDE/compiler rule definitions
  ├── docs/                           # Architecture analysis & documentation
  ├── scripts/                        # Batch PDF compiler, line-length & LaTeX auditors
  └── Resume_Building/                # Generated .tex/.pdf outputs & JD validation prompt
```

---

## 🛠️ Mandatory Workflows & Agent Routing

If you are an AI agent operating in this repository:
1. **O(1) Discovery:** Read [`.agent/catalog/skills-by-type.md`](.agent/catalog/skills-by-type.md) and [`.agent/catalog/commands-index.yaml`](.agent/catalog/commands-index.yaml) first.
2. **Follow Core Rules:** Read [`AGENTS.md`](AGENTS.md) and [`.agent/skills/resume_generation/SKILL.md`](.agent/skills/resume_generation/SKILL.md) before modifying any YAML or generating resumes.
3. **Core Workflows:**
   - **[Update Master Profile](.agent/workflows/update_master_profile.md)** — Always update `master_context.yaml` first.
   - **[Create Resume](.agent/workflows/create_resume.md)** · **[Tailor Resume](.agent/workflows/tailor_resume.md)** — Build Master or JD-tailored role YAMLs.
   - **[Judge Content](.agent/workflows/judge_content.md)** · **[Process JD Keywords](.agent/workflows/process_jd_keywords.md)** — Evaluate hiring-bar alignment and keyword fit.
   - **[Audit Resume](.agent/workflows/audit_resume.md)** · **[Audit Cover Letter](.agent/workflows/audit_cover_letter.md)** — Run final QA before export.
   - **[JD Validation Prompt](Resume_Building/gemini_JD_Validation.md)** — Analyze target job postings.

---

## 📋 Active Resume Inventory (Abhishek)

| Role | YAML Source | Output Directory | Status |
|---|---|---|---|
| Master Resume | `.agent/data/Abhishek/role_master.yaml` | `Resume_Building/Abhishek/Master/` | Active |
| Master One-Page Resume | — | `Resume_Building/Abhishek/Master_OnePage/` | Active |

---

## 📄 License
MIT License. Built with Antigravity.
