import json


def mock_llm(system_prompt: str, user_prompt: str) -> str:
    """
    Deterministic mock LLM.
    Returns a VerificationContract JSON string that conforms
    to the locked schema.
    """

    instruction = user_prompt.lower()

    # ---- O-RING CASE ----
    if "o-ring" in instruction or "oring" in instruction:
        return json.dumps({
            "step_metadata": {
                "step_id": "step_001",
                "raw_instruction": "Ensure the O-ring is present and seated correctly.",
                "process": "Final Assembly",
                "station": "Seal Install",
                "revision": "A"
            },
            "objects": [
                {
                    "object_id": "obj_01",
                    "name": "O-ring",
                    "expected_count": 1,
                    "attributes": ["presence", "placement"],
                    "critical": True
                }
            ],
            "verification": {
                "type": ["presence", "placement"],
                "logic": "all",
                "region_of_interest": "seal_groove",
                "temporal": False
            },
            "confidence": {
                "minimum_confidence": 0.75,
                "aggregation": "min",
                "allow_uncertain": True
            },
            "failure_handling": {
                "on_fail": "review",
                "on_uncertain": "review",
                "notes": "If seating is unclear, request human confirmation."
            }
        })

    # ---- SCREW CASE ----
    if "screw" in instruction:
        return json.dumps({
            "step_metadata": {
                "step_id": "step_002",
                "raw_instruction": "Verify that four screws secure the motor housing.",
                "process": "Final Assembly",
                "station": "Fastening",
                "revision": "A"
            },
            "objects": [
                {
                    "object_id": "obj_01",
                    "name": "screw",
                    "expected_count": 4,
                    "attributes": ["presence", "count"],
                    "critical": True
                }
            ],
            "verification": {
                "type": ["presence", "count"],
                "logic": "all",
                "region_of_interest": "motor_housing",
                "temporal": False
            },
            "confidence": {
                "minimum_confidence": 0.7,
                "aggregation": "min",
                "allow_uncertain": False
            },
            "failure_handling": {
                "on_fail": "fail",
                "on_uncertain": "review",
                "notes": "All fasteners must be present."
            }
        })

    # ---- FALLBACK CASE ----
    return json.dumps({
        "step_metadata": {
            "step_id": "unknown",
            "raw_instruction": user_prompt,
            "process": "Unknown",
            "station": "Unknown",
            "revision": "N/A"
        },
        "objects": [
            {
                "object_id": "obj_01",
                "name": "unknown_object",
                "expected_count": 1,
                "attributes": ["presence"],
                "critical": False
            }
        ],
        "verification": {
            "type": ["presence"],
            "logic": "any",
            "region_of_interest": None,
            "temporal": False
        },
        "confidence": {
            "minimum_confidence": 0.5,
            "aggregation": "min",
            "allow_uncertain": True
        },
        "failure_handling": {
            "on_fail": "review",
            "on_uncertain": "review",
            "notes": "Unrecognized instruction. Manual review required."
        }
    })
