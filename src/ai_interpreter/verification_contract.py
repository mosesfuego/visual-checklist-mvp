# src/ai_interpreter/verification_contract.py

VERIFICATION_TYPES = {"presence", "count", "placement", "orientation"}

class VerificationContract:
    """
    Canonical definition of a visual verification step.
    """

    def __init__(
        self,
        step_metadata: dict,
        objects: list,
        verification: dict,
        confidence: dict,
        failure_handling: dict,
    ):
        self.step_metadata = step_metadata
        self.objects = objects
        self.verification = verification
        self.confidence = confidence
        self.failure_handling = failure_handling
