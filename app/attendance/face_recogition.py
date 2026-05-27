import cv2

def detect_face():

    cam = cv2.VideoCapture(0)

    while True:

        success, frame = cam.read()

        cv2.imshow("Face Detection", frame)

        if cv2.waitKey(1) == 27:
            break

    cam.release()
    cv2.destroyAllWindows()