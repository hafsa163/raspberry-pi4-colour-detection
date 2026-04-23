import cv2
import numpy as np

def find_camera():
    for i in range(10):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"Camera found at index {i}")
            return cap
    return None

cap = find_camera()
if cap is None:
    print("No camera found")
    exit()

REAL_WIDTH = 6.0
FOCAL_LENGTH = 700

cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break
    frame = cv2.resize(frame, (640, 480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=2)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 200:
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.04 * perimeter, True)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.drawContours(frame, [approx], -1, (0, 255, 0), 3)
            distance = (REAL_WIDTH * FOCAL_LENGTH) / w
            cv2.putText(frame, "Red object detected",
                       (x, y - 10),
                       cv2.FONT_HERSHEY_SIMPLEX,
                       0.6, (0, 255, 0), 2)
            cv2.putText(frame, f"Distance: {int(distance)}cm",
                       (x, y + h + 20),
                       cv2.FONT_HERSHEY_SIMPLEX,
                       0.6, (0, 255, 0), 2)
    cv2.imshow("Webcam Feed", frame)
    cv2.imshow("Red Mask", mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()