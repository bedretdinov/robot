import logging
from websocket_server import WebsocketServer
import cv2
import base64
import time

cap = cv2.VideoCapture(0)


def videoCapture(client, server, message):

    if(message=='capture'):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # cv2.imwrite('./images/img_{}.jpg'.format(i), gray)
        gray = cv2.resize(gray, (int(100), int(100)))
        retval, buffer = cv2.imencode('.jpg', gray)

        # Convert to base64 encoding and show start of data
        jpg_as_text = base64.b64encode(buffer)
        server.send_message_to_all(jpg_as_text)


server = WebsocketServer(13254, host='0.0.0.0')
server.set_fn_message_received(videoCapture)
server.run_forever()