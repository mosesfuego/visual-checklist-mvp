from dataclasses import dataclass
from typing import List, Optional


@dataclass
class CVJob:
    object_name: str
    expected_count: int
    attributes: List[str]
    region_of_interest: Optional[str]
    min_confidence: float
    critical: bool
