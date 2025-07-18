import torch
import cv2
import os
import numpy as np

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', trust_repo=True)
model.eval()

# Define illegal zones (x1, y1, x2, y2)
illegal_zones = [
    (100, 100, 400, 400),  # Zone 1
    (500, 200, 700, 500)   # Zone 2
]

def is_illegal_fishing(detections, zones):
    for det in detections:
        x1, y1, x2, y2, conf, cls = det
        for zx1, zy1, zx2, zy2 in zones:
            if x1 < zx2 and x2 > zx1 and y1 < zy2 and y2 > zy1:
                return True
    return False

def draw_boxes(image_path, detections, zones, output_path):
    image = cv2.imread(image_path)

    # Draw illegal zones
    for zx1, zy1, zx2, zy2 in zones:
        cv2.rectangle(image, (zx1, zy1), (zx2, zy2), (0, 0, 255), 2)

    # Draw valid detections
    for det in detections:
        x1, y1, x2, y2, conf, cls = det
        label = f"{model.names[int(cls)]} {conf:.2f}"
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (255, 255, 0), 2)
        cv2.putText(image, label, (int(x1), int(y1) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)

    cv2.imwrite(output_path, image)

def run_detection(image_path):
    results = model(image_path)
    detections = results.xyxy[0].cpu().numpy()
    class_names = model.names

    # Allow only boats or ships
    allowed_labels = ["boat", "ship", "vessel"]
    filtered_detections = []

    for det in detections:
        cls_id = int(det[5])
        label = class_names[cls_id].lower()
        if any(allowed in label for allowed in allowed_labels):
            filtered_detections.append(det)

    result_img_path = os.path.join("static/results", os.path.basename(image_path))
    draw_boxes(image_path, filtered_detections, illegal_zones, result_img_path)

    status = "🚫 Illegal fishing detected!" if is_illegal_fishing(filtered_detections, illegal_zones) else "✅ No illegal activity detected."
    return result_img_path, status
