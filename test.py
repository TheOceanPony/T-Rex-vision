import cv2
import numpy as np

cap = cv2.VideoCapture('src/test_right.mp4')

if (cap.isOpened()== False): 
  print("Error opening video stream or file")

ret, frame_prev = cap.read()
frame_prev = frame_prev[:,:,0].astype(np.float32)
frame_curr = None

while(cap.isOpened()):

  ret, frame = cap.read()
  frame = frame[:,:,0]
  if ret == True:

    # Main
    frame_curr = frame.astype(np.float32)

    #diff = norm(frame_prev - frame_curr, axis=2)
    diff = np.abs(frame_prev - frame_curr).astype(np.float32)

    #print(np.max(diff), np.min(diff), diff.dtype)

    frame_prev = frame_curr

    # Display the resulting frame
    cv2.imshow('Frame',diff)

    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

  else: 
    break

cap.release()
cv2.destroyAllWindows()
