---
description: How to create a NEW, targeted resume from the Master Profile using Role Guidelines.
---

# Tailor Resume Workflow (Job-Specific Injection)

> **🚨 CRITICAL ARCHITECTURE RULE:** 
> Do not confuse Resume TAILORING with Resume BUILDING.
> - **Tailor Agent (`tailor.py`)**: Used AUTOMATICALLY in the data pipeline to inject a specific Job Description onto a pre-existing baseline profile (e.g. transforming `role_tpm.yaml` into `JD_123.yaml` mapping to a specific company).
> - **Builder Agent (`builder.py`)**: Used MANUALLY for the *FIRST-TIME CREATION* of a baseline career profile.

> **Goal:** Create a high-impact, targeted resume for a specific Job Description utilizing a pre-built base role.

## Step 1: Analysis & Strategy
1.  **Consult Role Guidelines:**
    - Open `.agent/skills/resume_generation/rules/role_guidelines.md`.
    - Identify the **Key Verbs** and **Focus Areas** for your target role.
    - *Example (TPM):* Focus on "Orchestrated", "Aligned", "Delivered", "Risk Management".
    - *Example (Product):* Focus on "Strategized", "Roadmapped", "User Research", "GTM".

## Step 2: Clone from Base Role (Tailor Action)
1.  **Clone Data File:**
    - The `tailor.py` bridge executes cloning logic on a high-scoring job.
    - **Naming:** `JD_[ID].yaml` (e.g., `JD_1241.yaml`).
    - **Command:** `shutil.copy(.agent/data/[PersonName]/role_[base_role].yaml, .agent/data/[PersonName]/tailored/JD_[ID].yaml)`

## Step 3: Tune the Content (The Tailoring)
1.  **Rewrite Bullets (XYZ):**
    - Modify the bullets to use the **Key Verbs** identified in Step 1.
    - *Example:* Change "Built a dashboard" to "Orchestrated a metric visualization system" (for TPM).
2.  **Reorder Sections:**
    - If Technical: Put Skills/projects higher.
    - If Managerial: Put Experience higher.
3.  **Add AI Enhancement:**
    - Explicitly add a bullet point about how you used AI in this role (if applicable).

## Step 4: Generate & Verify
1.  **Generate:**
    ```bash
    python3 .agent/scripts/generate_resume.py .agent/data/[PersonName]/role_[new_role].yaml
    ```
## Step 5: Registration (Inventory Update & Cleanup)
**Objective:** Track the new niche resume in the master inventory and manage files.

1.  **Open Inventory:** `.agent/data/[PersonName]/resume_inventory.yaml`.
2.  **Append Details:** Add the new role name, its YAML path, and the target TeX output path. 
3.  **Verify:** Check that the `status` is set to `Active`.
4.  **Cleanup:** Move any replaced/outdated `.tex` variants to an `Archive/` folder only after creating a timestamped backup folder and confirming exact target filenames.

## Step 6: Cover Letter Generation (Optional)
**Objective:** Generate a targeted cover letter to accompany the new tailored resume.
1. Use the appropriate prompt to generate a new cover letter targeting the specific `[new_role]`.
2. Ensure the cover letter passes the [Cover Letter Audit Protocol](./audit_cover_letter.md).
