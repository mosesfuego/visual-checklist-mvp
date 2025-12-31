from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

def detect_screws(image_path, conf_threshold=0.25):
    results = model(image_path)[0]
    detections = []

    for box in results.boxes:
        confidence = float(box.conf[0])
        if confidence < conf_threshold:
            continue

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        detections.append({
            "bbox": [x1, y1, x2, y2],
            "confidence": confidence
        })

    return detections

