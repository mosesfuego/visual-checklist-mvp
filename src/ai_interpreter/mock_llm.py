import json

def mock_llm(system_prompt: str, user_prompt: str) -> str:
    """
    Fake LLM response based on keyword matching.
    Returns a JSON string.
    """

    if "O-ring" in user_prompt or "O-ring" in user_prompt.lower():
        return json.dumps({
            "step_id": "step_001",
            "raw_instruction": "Ensure the O-ring is present and seated correctly.",
            "objects": [
                {
                    "name": "O-ring",
                    "expected_count": 1,
                    "attributes": ["presence", "placement"]
                }
            ],
            "verification_type": ["presence", "placement"],
            "confidence_requirement": 0.75,
            "notes": "Check correct seating in groove"
        })

    if "screw" in user_prompt.lower():
        return json.dumps({
            "step_id": "step_002",
            "raw_instruction": "Verify that four screws secure the motor housing.",
            "objects": [
                {
                    "name": "screw",
                    "expected_count": 4,
                    "attributes": ["presence"]
                }
            ],
            "verification_type": ["presence", "count"],
            "confidence_requirement": 0.7,
            "notes": "Fastener presence check"
        })

    return json.dumps({
        "step_id": "unknown",
        "raw_instruction": "Unknown instruction",
        "objects": [],
        "verification_type": ["visual_inspection"],
        "confidence_requirement": 0.5,
        "notes": "Fallback response"
    })
