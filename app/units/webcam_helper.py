import cv2

def open_webcam():

    cam = cv2.VideoCapture(0)

    while True:

        success, frame = cam.read()

        cv2.imshow(
            "Webcam",
            frame
        )

        if cv2.waitKey(1) == 27:
            break

    cam.release()