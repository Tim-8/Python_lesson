import cv2

capture = cv2.VideoCapture(0)

while (True):
  ret, frame = cpture.read()
  cv2.inshow("frame", frame)
  if cv2.waitkey(1) & 0xFF == ord("q"):
    break
capture.release()

