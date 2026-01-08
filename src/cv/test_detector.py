from cv.yolo_detector import YOLODetector

detector = YOLODetector()
image = "src/sample.jpg"

detections = detector.detect(image, "person")  # use known COCO class

print(detections)
