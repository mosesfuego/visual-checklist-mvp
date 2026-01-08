from ai_interpreter.parser import parse_instruction
from cv.yolo_detector import YOLODetector
from decision.decision_engine import evaluate_presence


class Orchestrator:

    def __init__(self, detector=None):
        self.detector = detector or YOLODetector()

    def run(self, instruction_text: str, image_path: str):
        # 1. Interpret instruction → contract
        contract = parse_instruction(instruction_text)

        # 2. Extract object to detect
        obj = contract["objects"][0]
        object_name = obj["name"]

        # 3. Run detection
        detections = self.detector.detect(image_path, object_name)

        # 4. Make decision
        result = evaluate_presence(contract, detections)

        return {
            "instruction": instruction_text,
            "object": object_name,
            "decision": result
        }
