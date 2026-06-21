# Query

Answer the question provided in $ARGUMENTS.

Search procedure:

1. Search `wiki/` first. Read every relevant page and extract claims that bear on the question.
2. If the wiki does not contain enough information, search `raw/` for supporting source material.
3. Synthesise a clear, direct answer in plain English.

Citation rules:

- Cite every factual claim with the wiki page name in brackets, e.g. `[AI Tutoring Bias Study]`.
- If a claim comes from `raw/` rather than a wiki page, cite the source file name instead.
- If no source exists for a claim, do not make it. State that the information is not in the knowledge base.

Format:

- Lead with a direct answer to the question.
- Follow with supporting detail, each claim cited.
- End with a "Sources" list of every page or file cited.
