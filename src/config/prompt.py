import textwrap


PROMPT = textwrap.dedent("""\
    Extract person_name, country, and skill-set in order of appearance.
    Use exact text for extractions. Do not paraphrase or overlap entities.
    Provide meaningful attributes for each entity to add context.""")