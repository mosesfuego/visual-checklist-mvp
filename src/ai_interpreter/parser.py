from .mock_llm import mock_llm
from .prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE
from .schema import VERIFICATION_SCHEMA
import json

def parse_instruction(instruction_text: str):
    response = mock_llm(
        system_prompt=SYSTEM_PROMPT,
        user_prompt=USER_PROMPT_TEMPLATE.format(
            schema=VERIFICATION_SCHEMA,
            instruction=instruction_text
        )
    )

    return json.loads(response)
