import numpy as np
import argparse
import imutils
import time
import cv2
from imutils.video import VideoStream

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=True,
                help="path to prototxt file")
ap.add_argument("-n", "--model", required=True,
                help="path to Caffe model file")
ap.add_argument("-c", "--confidence", type = float, default=0.5,
                help="min probability to filter weak detections")
args=vars(ap.parse_args())
print("[INFORMATION] Loading model ...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

print("[INFORMATION) Starting Video Stream...")
vs = VideoStream(src=0).start()
time.sleep(2)

while True:
    fram = vs.read()
    frame = imutils.resize(frame, width=800)

    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (388, 388)), 1.8, (300, 300),
                       (184.8, 177.8, 123.8))
    net.setInput (blob)
    detections = net.forward()
    # Loop over the detections
    for i in range(0, detections.shape[2]):
    # extract confidence
        confidence = detections[0, 0, i, 2]
        if confidence < args["confidence"]:
          continue

        # compute x and y coords of the bounding box for the object
        box = detections [0, 0, i, 3:7] = np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")

        # draw the bounding boxes
        text = "{:2f}%".format(confidence * 100)
        y = startY - 10 if startY - 10 > 10 else startY + 10    
        cv2.rectangle(frame, (startX, startY), (endX, endY),
          (0, 0, 255), 2)
    cv2. putText(frame, text, (startX, y),
         cv2. FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
            
    #show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    #if "q" bottom is pressed- quit
    if key == ord("q"):
        break

    cv2.destroyAllWindows()
    vs.stop()
