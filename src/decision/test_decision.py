from decision.decision_engine import evaluate_presence
from ai_interpreter.parser import parse_instruction

contract = parse_instruction(
    "Ensure the O-ring is present and seated correctly."
)

# Simulate CV output
detections = [
    {"bbox": [10,10,50,50], "confidence": 0.81}
]

result = evaluate_presence(contract, detections)
print(result)
