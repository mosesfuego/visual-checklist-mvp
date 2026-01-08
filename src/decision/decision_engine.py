from decision.result_types import DecisionStatus, DecisionResult


def evaluate_presence(contract: dict, detections: list):
    """
    Evaluates presence/count requirements for a single object.
    """

    obj = contract["objects"][0]

    expected = obj["expected_count"]
    min_conf = contract["confidence"]["minimum_confidence"]

    valid_detections = [
        d for d in detections if d["confidence"] >= min_conf
    ]

    found = len(valid_detections)

    if found == expected:
        return DecisionResult(
            status=DecisionStatus.PASS,
            reason=f"Expected {expected} {obj['name']}(s) detected",
            metrics={
                "expected": expected,
                "found": found,
                "confidence_avg": avg_conf(valid_detections)
            }
        )

    if found < expected:
        return DecisionResult(
            status=DecisionStatus.FAIL,
            reason=f"Missing {obj['name']}(s)",
            metrics={
                "expected": expected,
                "found": found
            }
        )

    return DecisionResult(
        status=DecisionStatus.UNCERTAIN,
        reason=f"Unexpected number of {obj['name']}(s) detected",
        metrics={
            "expected": expected,
            "found": found
        }
    )


def avg_conf(detections):
    if not detections:
        return 0.0
    return sum(d["confidence"] for d in detections) / len(detections)
