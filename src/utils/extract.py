import langextract as lx
import os


def extract_result(input_text, prompt, examples):
    """
        Extracts results from text based on prompt and examples.
    """

    result = lx.extract(
        text_or_documents=input_text,
        prompt_description=prompt,
        examples=examples,
        model_id="gpt-4o",
        api_key=os.environ.get('OPENAI_API_KEY'),
        fence_output=True,
        use_schema_constraints=False
    )

    return result