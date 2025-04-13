from ultralytics import YOLO
import cv2

# Load YOLOv8 model (you can use 'yolov8n.pt' for lightweight detection)
model = YOLO("yolov8n.pt")

# Open default webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLOv8 inference
    results = model(frame, verbose=False)[0]

    # Annotate frame with bounding boxes and labels
    annotated_frame = results.plot()

    # Display the result
    cv2.imshow("YOLOv8 Webcam Detection", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
