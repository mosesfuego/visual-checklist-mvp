from ultralytics import YOLO
from cv.detector_base import BaseDetector


class YOLODetector(BaseDetector):

    def __init__(self, model_path="yolov8n.pt"):
        self.model = YOLO(model_path)

    def detect(self, image_path: str, object_name: str):
        results = self.model(image_path)[0]
        detections = []

        for box in results.boxes:
            cls_name = self.model.names[int(box.cls[0])]
            if cls_name.lower() != object_name.lower():
                continue

            detections.append({
                "bbox": list(map(int, box.xyxy[0])),
                "confidence": float(box.conf[0])
            })

        return detections
