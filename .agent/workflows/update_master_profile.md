---
description: The Single Source of Truth protocol. ALWAYS start here when updating biographical data (dates, employers, degrees).
---

# Master Profile Update Workflow

> **🚨 CRITICAL:** Do NOT update specific resume files (e.g., `role_tpm.yaml`) with new jobs or degrees until you have updated the Master Context.

## Step 1: Update the Master Source
**File:** `.agent/data/[PersonName]/master_context.yaml`

1.  **Open `master_context.yaml`**.
2.  **Add/Edit Data**:
    - **New Job**: Add to `experience` list.
    - **New Project**: Add to `projects` list.
    - **New Certification**: Add to `certifications` list.
    - **Date Change**: Update the specific record.
3.  **Verify**: Ensure the data is complete and accurate. This is your database.

## Step 2: Propagate to Active Roles
**Objective**: Push the new data to the specific resumes you are currently using.

1.  **Identify Active Roles**:
    - E.g., `.agent/data/Abhishek/role_tpm.yaml`
    - E.g., `.agent/data/Abhishek/role_manager.yaml`

2.  **Copy & Paste**:
    - Copy the *exact* new block from `master_context.yaml`.
    - Paste it into the corresponding section of the role file.

3.  **Regenerate**:
    - Run `python3 .agent/scripts/generate_resume.py .agent/data/Abhishek/[role_file].yaml` to generate the updated `.tex` file. Antigravity does **not** generate the final PDF.

## Step 3: Consistency & Length Check
1.  **Diff Check:** Run a diff or visual check to ensure `master_context.yaml` and your key role files match on core facts (dates, titles).
2.  **Cascade Pruning Warning:** If propagating a new job or project pushes the role-specific resume over the strict 1-page limit, you MUST immediately prune or condense older, less relevant entries in that specific role file.
