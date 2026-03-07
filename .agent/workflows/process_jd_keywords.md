---
description: Process to evaluate new keywords/skills from a JD and safely inject them into the Master Context and target Role YAMLs.
---

# Process JD Keywords Workflow

**Objective**: Safely evaluate and inject new skills, tools, or keywords from a Job Description (JD) into your resumes without modifying or deleting existing context.

## Step 1: Provide the Keyword Dump
You provide a list of keywords or skills extracted from a JD (e.g., via Gemini) and specify the target role file you're tailoring for.
*Example prompt: "/process_jd_keywords for `role_dubai.yaml`. Here is the list: [AWS, Python, Agile, Scrum, Cloud Migration]"*

## Step 2: Evaluation & Sorting
I will analyze the provided list and categorize them into:
1. **Fits (Career Progression)**: Relevant skills that enhance your profile and match the hiring bar.
2. **Discards**: Irrelevant, basic, or duplicate skills that do not demonstrate progression.

I will present this sorted list to you for final approval.

## Step 3: Injection into Master Context
Once approved, I will strictly **APPEND** the approved keywords to your `.agent/data/[PersonName]/master_context.yaml`.
- Existing XYZ bullet points or summaries will **never** be altered.
- Keywords will be added to the appropriate sections (e.g., lists under `skills`, or as new lines like "Tools/Tech Used" under specific `experience` entries).

## Step 4: Role Sync
After the `master_context.yaml` is updated:
1. I will intelligently copy the new additions to the target role file (e.g., `role_dubai.yaml`), injecting them where they are most relevant for that specific role.

## Step 5: Learning Roadmap Update
Any high-value keywords that were discarded because they do not currently apply to your profile (but represent strong career progression or industry standards) will be appended to `.agent/data/[PersonName]/learning_roadmap.md`.
- This ensures you have a continuous backlog of skills and tools to acquire for future roles.
