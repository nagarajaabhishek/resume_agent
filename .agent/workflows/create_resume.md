---
description: The standard, strict workflow for creating or updating any resume. Enforces Markdown-first drafting and mandatory audits.
---

# Resume Creation/Update Workflow (Python-Based)

> **🚨 CRITICAL ARCHITECTURE RULE:** 
> Do not confuse Resume BUILDING with Resume TAILORING.
> - **Builder Agent (`builder.py`)**: Used MANUALLY for the *FIRST-TIME CREATION* of a baseline career profile (e.g. creating `role_tpm.yaml` from `master_context.yaml`).
> - **Tailor Agent (`tailor.py`)**: Used AUTOMATICALLY in the data pipeline to inject a specific Job Description onto a pre-existing baseline profile (e.g. transforming `role_tpm.yaml` into `JD_123.yaml`).

## Step 1: Career Profile Extraction (Builder Agent)
**Objective:** Define the baseline content in structured data.
**File:** `.agent/data/resume_data.yaml`

1.  **Extract Data via Builder:**
    - The Builder Agent (`builder.py`) forks `master_context.yaml` based on a requested track.
    - Alternatively, manually create a new YAML file for the specific role (e.g., `.agent/data/Abhishek/role_tpm.yaml`).
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
- The final output is the generated `.tex` file. Antigravity does **not** generate the final PDF.

## Step 4: Maintenance (Registry Update & Cleanup)
**Objective:** Keep the global list of active resumes up to date and clean up old artifacts.

1. **Update Inventory:** Open `.agent/data/[PersonName]/resume_inventory.yaml`.
2. **Add Entry:** Ensure the new role, its YAML path, and its TeX output path are registered.
3. **Cleanup:** Move any outdated `.tex` files for this role to an `Archive/` or `Old/` folder to prevent version confusion.
