---
description: The standard, strict workflow for creating or updating any resume. Enforces Markdown-first drafting and mandatory audits.
---

# Resume Creation/Update Workflow (Python-Based)

> **🚨 CRITICAL:** We no longer write LaTeX manually. We edit Data (YAML) and Generate Code (Python).

## Step 1: Career Profile (The Source of Truth)
**Objective:** Define the content in structured data.
**File:** `.agent/data/resume_data.yaml`

1.  **Select/Create Data File:**
    - Create a new YAML file for the specific role (e.g., `.agent/data/Abhishek/role_tpm.yaml`).
    - **Naming Convention:** `role_[job_title_snake_case].yaml` (e.g., `role_product_manager.yaml`).
    - **Location:** MUST be in `.agent/data/[PersonName]/`.
    - Copy structure from `master_context.yaml` or existing role file.
    
2.  **Edit Content:**
    - Fill in the YAML fields.
    - **Rules Enforced by Code:**
      - Bullets must be > 100 chars.
      - No forbidden words ("Accomplished", "Responsible for").

## Step 2: Auto-Verification & Generation
**Objective:** Run the Python Engine to validate and build.

1.  **Execute Script:**
    ```bash
    python3 .agent/scripts/generate_resume.py .agent/data/Abhishek/role_tpm.yaml
    ```
    
2.  **Outcome:**
    - **Success:** A perfect `.tex` file is created in `Resume_Building/Generated/`.
    - **Failure:** The script dumps errors (e.g., "Bullet 2 too short"). **Fix the YAML and re-run.**

## Step 3: Final Output
- Present the generated PDF/LaTeX file.
