from orchestrator.runner import Orchestrator


class MockDetector:
    def detect(self, image_path, object_name):
        # Fake detection for demo
        return [
            {"bbox": [10, 10, 50, 50], "confidence": 0.85}
        ]


orch = Orchestrator(detector=MockDetector())

result = orch.run(
    instruction_text="Ensure the O-ring is present and seated correctly.",
    image_path="src/sample.jpg"
)

print(result)
