import cv2
from src.cv.detect_screws import detect_screws

IMAGE_PATH = "data/sample pics/pcb_1_screw.jpg"

def visualize(image_path, detections):
    img = cv2.imread(image_path)

    for det in detections:
        x1, y1, x2, y2 = det["bbox"]
        conf = det["confidence"]

        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(
            img,
            f"{conf:.2f}",
            (x1, max(y1 - 5, 15)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            1
        )

    cv2.imshow("Detections", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detections = detect_screws(IMAGE_PATH, conf_threshold=0.2)

print(f"TOTAL DETECTED: {len(detections)}")
visualize(IMAGE_PATH, detections)
