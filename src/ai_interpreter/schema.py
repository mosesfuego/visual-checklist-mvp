VERIFICATION_SCHEMA = {
    "step_id": "string",
    "raw_instruction": "string",
    "objects": [
        {
            "name": "string",
            "expected_count": "number | null",
            "attributes": ["presence", "placement", "orientation"]
        }
    ],
    "verification_type": [
        "presence",
        "count",
        "placement",
        "orientation",
        "visual_inspection"
    ],
    "confidence_requirement": "number",
    "notes": "string | null"
}
