import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: couldn't open video")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: couldn't read frame")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    edges_color = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    cv2.imshow('Edges', edges_color)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cap.destroyAllWindows()