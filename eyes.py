import time
import cv2
import numpy as np
from imutils.video import VideoStream
import imutils

usingPiCamera = False
# Set initial frame size.
frameSize = (320, 240)

# Initialize mutithreading the video stream.
vs = VideoStream(src=0, usePiCamera=usingPiCamera, resolution=frameSize,
        framerate=32).start()
vs1 = VideoStream(src=2,resolution=frameSize, framerate=32).start()
time.sleep(2.0)

timeCheck = time.time()

while True:

    frame = vs.read()
    frame1 = vs1.read()

    if not usingPiCamera:
        frame = imutils.rotate(frame, angle=270)
        frame1 = imutils.rotate(frame1, angle=270)


    # Show video stream
    cv2.imshow('orig', frame)
    cv2.imshow('twah',frame1)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop.
    if key == ord("q"):
        break
    print(1/(time.time() - timeCheck))
    timeCheck = time.time()
# Cleanup before exit.
cv2.destroyAllWindows()
vs.stop()

