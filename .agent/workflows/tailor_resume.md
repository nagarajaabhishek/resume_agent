---
description: How to create a NEW, targeted resume from the Master Profile using Role Guidelines.
---

# Tailor Resume Workflow (Role-Specific)

> **Goal:** Create a high-impact, targeted resume for a specific job family (e.g., "AI Product Manager" vs "Technical Program Manager").

## Step 1: Analysis & Strategy
1.  **Consult Role Guidelines:**
    - Open `.agent/skills/resume_generation/rules/role_guidelines.md`.
    - Identify the **Key Verbs** and **Focus Areas** for your target role.
    - *Example (TPM):* Focus on "Orchestrated", "Aligned", "Delivered", "Risk Management".
    - *Example (Product):* Focus on "Strategized", "Roadmapped", "User Research", "GTM".

## Step 2: Fork from Master
1.  **Create New File:**
    - **Naming:** `role_[target_role].yaml` (e.g., `role_ai_engineer.yaml`).
    - **Command:** `cp .agent/data/[PersonName]/master_context.yaml .agent/data/[PersonName]/role_[new_role].yaml`
2.  **Prune Content:**
    - Remove projects/experience that are *irrelevant* to this specific role.
    - *Rule:* Keep it to 1 page (approx. 3-4 roles, 3-4 projects).

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
2.  **Review:**
    - Check the PDF. Does it "read" like the target role?
