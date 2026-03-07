---
description: The Single Source of Truth protocol. ALWAYS start here when updating biographical data (dates, employers, degrees).
---

# Master Profile Update Workflow

> **🚨 CRITICAL:** Do NOT update specific resume files (e.g., `role_tpm.yaml`) with new jobs or degrees until you have updated the Master Context.

## Step 0: Know the Frozen Facts
These biographical fields are **immutable ground truth**. Never change them without explicit user confirmation:
- **School**: `University of Texas at Arlington`
- **Degrees**: `Master of Science in Computer Science`, `Master of Science in Engineering Management`
- **Undergrad**: `Jawaharlal Nehru Technological University` — `Bachelor of Technology in Computer Science and Engineering`
- **School URL**: `https://www.uta.edu/`

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

## Step 4: Integrity Check (Run after every edit)
Run the following to assert frozen facts were not accidentally changed:
```bash
grep -q "University of Texas at Arlington" .agent/data/Abhishek/master_context.yaml || echo "⚠️ School name mismatch!"
```
If the warning fires, **stop and fix `master_context.yaml` before proceeding.**
