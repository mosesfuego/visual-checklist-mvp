class SchemaValidationError(Exception):
    pass


REQUIRED_TOP_LEVEL_KEYS = [
    "step_metadata",
    "objects",
    "verification",
    "confidence",
    "failure_handling"
]


def validate_contract(contract: dict):
    for key in REQUIRED_TOP_LEVEL_KEYS:
        if key not in contract:
            raise SchemaValidationError(f"Missing top-level key: {key}")

    if not isinstance(contract["objects"], list) or len(contract["objects"]) == 0:
        raise SchemaValidationError("At least one object is required")

    for obj in contract["objects"]:
        validate_object(obj)


def validate_object(obj: dict):
    required_fields = ["object_id", "name", "expected_count", "attributes", "critical"]

    for field in required_fields:
        if field not in obj:
            raise SchemaValidationError(f"Object missing field: {field}")

    if not isinstance(obj["expected_count"], int):
        raise SchemaValidationError("expected_count must be an integer")

    if obj["expected_count"] < 0:
        raise SchemaValidationError("expected_count cannot be negative")
