from enum import Enum
from dataclasses import dataclass


class DecisionStatus(Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    UNCERTAIN = "UNCERTAIN"


@dataclass
class DecisionResult:
    status: DecisionStatus
    reason: str
    metrics: dict
