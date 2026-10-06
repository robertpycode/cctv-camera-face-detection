import cv2
import time
import datetime
import winsound
import os

CAP_INDEX = 0
DETECTION_WIDTH = 320
DETECTION_HEIGHT = 240
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
SECONDS_TO_RECOGNITION = 5
FOURCC = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
ALARM_WAV = "alarm.wav"
BEEP_FREQUENCY = 1000
BEEP_DURATION_MS = 500
ALARM_COOLDOWN = 3.0
MINI_FACE_AREA = 1000


cap = cv2.VideoCapture(CAP_INDEX, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

fps = cap.get(cv2.CAP_PROP_FPS)
if not fps or fps != fps or fps < 1:
    fps = 20

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

recording = False
out = None
detection_stopped_time = None
timer_started = False
_alert_alarm_time = 0

def play_alarm(): """Play alarm.wav asynchronously if present else fallback to beep."""

try:
    if os.path.exists(ALARM_WAV):
        winsound.PlaySound(ALARM_WAV, winsound.SND_FILENAME | winsound.SND_ASYNC)
    else:
        winsound.Beep(BEEP_FREQUENCY, BEEP_DURATION_MS)
except Exception as e:
    print("Alarm play failed: ", e)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("[Warn] No frame from camera.")
            break


        small = cv2.resize(frame, (DETECTION_WIDTH, DETECTION_HEIGHT))
        gray_small = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)

        faces_small = face_cascade.detectMultiScale(gray_small, 1.1, 5)
        bodies_small = face_cascade.detectMultiScale(gray_small, 1.05, 3)


        x_scale = FRAME_WIDTH / DETECTION_WIDTH
        y_scale = FRAME_HEIGHT / DETECTION_HEIGHT

        detections = []
        for (x,y,w,h) in faces_small:
            rx, ry, rw, rh = int(x * x_scale), int(y * y_scale), int(w * x_scale), int(h * y_scale)
            if rw * rh >= MINI_FACE_AREA:
                detections.append(('face', (rx, ry, rw, rh)))

        for (x,y,w,h) in bodies_small:
            rx, ry, rw, rh = int(x * x_scale), int(y * y_scale), int(w * x_scale), int(h * y_scale)
            detections.append(('body', (rx, ry, rw, rh)))

        motion_detected = len(detections) > 0

        if motion_detected:
            if recording:
                timer_started = False
            else:
                recording: True
                now_str = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                filename = f'{now_str}.mp4'
                out = cv2.VideoWriter(filename, FOURCC, fps, (FRAME_WIDTH, FRAME_HEIGHT))
                if out and out.isOpened():
                    print("[INFO] Recording Started!", filename)

                    now = time.time()
                    if now - _alert_alarm_time > ALARM_COOLDOWN:
                        play_alarm()
                        _alert_alarm_time = now
                else:
                    print("[ERROR] Could not open VideoWriter. Recording Disabled")
                    if out is not None:
                        out.release()
                    out = None
                    recording = False

        elif recording:
            if timer_started:
                if time.time() - detection_stopped_time >= SECONDS_TO_RECOGNITION:
                    recording = False
                    timer_started = False
                    if out is not None:
                        out.release()
                        out = None
                    print("[INFO] Recording stopped (no motion).")
            else:
                timer_started = True
                detection_stopped_time = time.time()

        if recording and out is not None:
            out.write(frame)

        for kind, (x,y,w,h) in detections:
            color = (255, 0, 0) if kind == 'face' else (0, 255, 0)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, kind, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        cv2.putText(frame, f"Recording: {'Yes' if recording else 'No'}",(10, 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255) if recording else (0, 255, 0), 2)

        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    if out is not None:
        out.release()
    cap.release()
    cv2.destroyAllWindows()