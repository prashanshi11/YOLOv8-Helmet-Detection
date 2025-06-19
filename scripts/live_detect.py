from ultralytics import YOLO
import cv2
import platform
import time

# Alert sound function
def beep_alert():
    if platform.system() == 'Windows':
        import winsound
        duration = 500  # milliseconds
        freq = 1000  # Hz
        winsound.Beep(freq, duration)
    else:
        # For Mac/Linux
        import os
        os.system('play -nq -t alsa synth 0.3 sine 1000')  # requires 'sox' installed

# Load model
model = YOLO('C:/Users/hp/runs/detect/train16/weights/best.pt')


# Class names (edit based on your model)
class_names = ['head', 'helmet', 'vest']

cap = cv2.VideoCapture(0)
alert_cooldown = 2  # seconds between alerts
last_alert_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]
    annotated_frame = results.plot()

    labels = results.names
    detections = results.boxes.cls.tolist()

    heads = 0
    helmets = 0

    for cls in detections:
        label = labels[int(cls)]
        if label == 'head':
            heads += 1
        elif label == 'helmet':
            helmets += 1

    # Alert if more heads than helmets (i.e., someone without a helmet)
    if heads > helmets and (time.time() - last_alert_time > alert_cooldown):
        print("⚠️ No helmet detected! Sounding alert.")
        beep_alert()
        last_alert_time = time.time()

    cv2.imshow("Safety Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
