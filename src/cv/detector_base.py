from abc import ABC, abstractmethod
from typing import List, Dict


class BaseDetector(ABC):

    @abstractmethod
    def detect(self, image_path: str, object_name: str) -> List[Dict]:
        """
        Returns a list of detections:
        [
          {
            "bbox": [x1, y1, x2, y2],
            "confidence": 0.82
          }
        ]
        """
        pass
