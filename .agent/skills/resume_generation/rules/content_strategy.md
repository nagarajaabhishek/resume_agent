## 1. The XYZ Strategy (Action-First)
Every achievement bullet point MUST follow the "Accomplished [X] as measured by [Y], by doing [Z]" logic, but **NEVER** start every line with the word "Accomplished". 

### Verb usage:
- **Rule**: Start bullets with strong, diverse action verbs (e.g., *Architected*, *Spearheaded*, *Engineered*, *Optimized*).
- **Template Logic**:
    - [X] (Result/Verb) + [Y] (Metric) + [Z] (Method).
    - Or: [Verb] + [Details] + [Result/Metric].
- **Anti-Pattern**: Starting multiple consecutive bullets with the same word (especially "Accomplished", "Managed", or "Worked on").

**Example (XYZ Logic, Diverse Verbs):**
- **Spearheaded** a **20% reduction in support tickets** as measured by monthly helpdesk reports, by **engineering a RAG-based chatbot** using Python and OpenAI API.
- **Optimized** system latency by **35%**, by refactoring the core caching layer in Redis.

## 2. Keyword Engineering
1. **Exact Match**: Use the exact terminology from the Job Description (e.g., "ML" vs "Machine Learning").
2. **Acronym Rule**: Use "Full Term (Acronym)" on the first mention: "Standard Operating Procedure (SOP)".
3. **Contextual Integration**: Weave keywords into action bullets rather than just listing them in a skills section.
4. **Frequency**: High-priority keywords should appear 2-3 times across the document.

## 3. Strict Anti-Hallucination Guardrails
**CRITICAL PROTOCOL: YOU MUST NEVER INVENT, INFLATE, OR FABRICATE DATA.**
- **No New Experiences:** You cannot write bullets for jobs or projects that do not exist in the source YAML.
- **No Fake Metrics:** If the source data says "$120,000", you MUST use $120,000. You cannot change it to "$1M" to sound better. You cannot invent percentages or user counts.
- **No Fake Skills:** You can rephrase "Built an API" to "Architected an API" to match a JD, but you CANNOT say "Architected an API using Kubernetes" if Kubernetes is not listed in the candidate's core profile. 
- **Verbs Only:** You are authorized to strategically swap power verbs (e.g., swapping "Led" to "Orchestrated") to match JD vocabulary, but all nouns, proper nouns, and quantitative data must remain physically anchored to the source truth.

## 4. Content Anti-Patterns
1.  **Double Dipping:** Do NOT repeat the exact same metric in the Summary and Experience sections.
2.  **Generic Verbs:** Avoid "Assisted", "Helped", "Worked on". Use "Architected", "Engineered", "Orchestrated".
3.  **Context Mixing:** Do not use purely technical verbs for GTM/strategy roles (e.g., use "Executed" instead of "Built" for a marketing plan).
