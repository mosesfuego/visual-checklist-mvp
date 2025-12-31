from ultralytics import YOLO
import cv2
#load model
model = YOLO("yolov8n.pt")
def detect_screws(image_path, conf_threshold = 0.25):
    results = model(image_path)[0]

    detections = []

    for box in results.boxes:
        cls = int(box.cls[0])
        confidencce = float(box.conf[0])
        if confidence < conf_threshold:
            continue
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        w =x2-x1
        h=y2-y1
        detections.append({
            "x": x1,
            "y": y1,
            "w": w,
            "h": h,
            "confidence": confidence
        })
    return detections
        
