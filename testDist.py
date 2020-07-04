import numpy as np
import cv2
import base64


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #cv2.imwrite('./images/img_{}.jpg'.format(i), gray)
    retval, buffer = cv2.imencode('.jpg', frame)

    # Convert to base64 encoding and show start of data
    jpg_as_text = base64.b64encode(buffer)
    print(jpg_as_text)
    if(i>1):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()