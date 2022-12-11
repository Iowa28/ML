import cv2
import sys

def run():
    # cascPath = sys.argv[1]
    # faceCascade = cv2.CascadeClassifier(cascPath)
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    while True:
        ret, frame = video_capture.read()

        if frame is None:
            print('frame is None')
            break

        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #
        # faces = faceCascade.detectMultiScale(
        #     gray,
        #     scaleFactor=1.1,
        #     minNeighbors=5,
        #     minSize=(30, 30),
        #     flags=cv2.CV_HAAR_SCALE_IMAGE
        # )

        faces = faceCascade.detectMultiScale(frame)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow('frame', frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q') or key == 27:
            break

    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    run()