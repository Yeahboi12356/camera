import cv2
import time
import datetime

def main():
    print("press q to exit camera")
    print("language >:")
    print("1.indonesian")
    print("2.english")
    n = int(input("input: "))
    if n == 1:
        indonesian()
    elif n == 2:
        english()
    else:
        print("number not valid")
        main()
def english():
    cap = cv2.VideoCapture(0)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    body_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade__fullbody.xml")

    recording = False
    detection_stopped_time = None
    timer_started = False
    seconds = 5
    frame_size  = (int(cap.get(3)), int(cap.get(4)))
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    while True:
        _, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        bodies = face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) + len(bodies) >0:
            if recording:
                timer_started = False
            else:
                recording = True
                currect_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                out = cv2.VideoWriter(f"{currect_time}.mp4", fourcc, 20, frame_size)
                print("\nfaces detected!")
                print("Started Recording..")
        elif recording:
            if timer_started:
                if time.time() - recording_stopped_time >= seconds:
                    recording = False
                    timer_started = False
                    out.release()
                    print("\nfaces not found")
                    print("Stop recording..")
            else:
                timer_started = True
                recording_stopped_time = time.time()
        if recording:
            out.write(frame)

        for (x, y, widgt, height) in faces:
            cv2.rectangle(frame, (x,y), (x + widgt, y + height), (0, 0, 255), 3)
        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) == ord('q'):
            break

    out.release()
    cap.release()
    cv2.destroyAllWindows()

def indonesian():
    cap = cv2.VideoCapture(0)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    body_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade__fullbody.xml")

    recording = False
    detection_stopped_time = None
    timer_started = False
    seconds = 5
    frame_size  = (int(cap.get(3)), int(cap.get(4)))
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    while True:
        _, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        bodies = face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) + len(bodies) >0:
            if recording:
                timer_started = False
            else:
                recording = True
                currect_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                out = cv2.VideoWriter(f"{currect_time}.mp4", fourcc, 20, frame_size)
                print("\nwajah terditeksi")
                print("merekam..")
        elif recording:
            if timer_started:
                if time.time() - recording_stopped_time >= seconds:
                    recording = False
                    timer_started = False
                    out.release()
                    print("\nwajah tidak terditeksi")
                    print("menghentikan rekaman..")
            else:
                timer_started = True
                recording_stopped_time = time.time()
        if recording:
            out.write(frame)

        for (x, y, widgt, height) in faces:
            cv2.rectangle(frame, (x,y), (x + widgt, y + height), (0, 0, 255), 3)
        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) == ord('q'):
            break

    out.release()
    cap.release()
    cv2.destroyAllWindows()

main()
