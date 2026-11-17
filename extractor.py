
import ollama
from pydantic import ValidationError
from schemas import ProductInfo

MODEL_NAME = "qwen3.5:2b"


def extract_product_information(text: str):

    if not text.strip():
        raise ValueError("Please enter product information.")

    prompt = f"""
    Extract product information from the following description.

    Return only the requested structured JSON.

    Rules:
    - Do not invent missing information.
    - Use an empty string for missing text fields.
    - Use 0 for an unknown price.
    - Price must be a non-negative number.
    - Follow the supplied JSON schema.

    Description:
    {text}
    """

    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            format=ProductInfo.model_json_schema(),
            think=False,
            stream=False,
            options={
                "temperature": 0,
                "num_ctx": 2048,
                "num_predict": 512
            }
        )

        json_output = response.message.content

        # Check for empty model response
        if not json_output or not json_output.strip():
            raise RuntimeError(
                "Qwen returned an empty response. "
                "Check Ollama version and model output."
            )

        # Validate JSON using Pydantic
        product = ProductInfo.model_validate_json(json_output)

        return product

    except ValidationError as error:
        raise ValueError(
            f"JSON schema validation failed: {error}"
        ) from error

    except ollama.ResponseError as error:
        raise RuntimeError(
            f"Ollama error: {error}"
        ) from error
