import langextract as lx


EXAMPLES = [
    lx.data.ExampleData(
        text="Sofia from Brazil mastered the skill of storytelling through dance.",
        extractions=[
            lx.data.Extraction(
                extraction_class="person_name",
                extraction_text="Sofia",
                attributes={"country": "Brazil"}
            ),
            lx.data.Extraction(
                extraction_class="country",
                extraction_text="Brazil",
                attributes={"person_name": "Sofia"}
            ),
            lx.data.Extraction(
                extraction_class="skill-set",
                extraction_text="storytelling through dance",
                attributes={"person_name": "Sofia"}
            ),
        ]
    )
]