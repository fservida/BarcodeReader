# main.py
# created: 2020-11-04
# last modified: 2020-11-04
# created by Francesco Servida
# greatly based on https://kalebujordan.com/reading-bar-codes-python/

import cv2
from pyzbar import pyzbar
import webbrowser
import re
import pyperclip

url_re = re.compile(r"(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)")
last_read = None


def read_barcode(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        barcode_text = barcode.data.decode('utf-8')
        global last_read
        if barcode_text != last_read:
            last_read = barcode_text
            check_url = url_re.match(last_read)
            if check_url is not None:
                url = check_url.groups()[0]
                print("URL detected: ", url)
                webbrowser.open(url)
            else:
                print("Generic Code detected: ", last_read)
                pyperclip.copy(last_read)
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
    return frame


def read_camera(camera_idx: int):
    camera = cv2.VideoCapture(camera_idx)
    ret, frame = camera.read()

    while ret:
        frame = read_barcode(frame)
        cv2.imshow('Barcode Reader', frame)
        ret, frame = camera.read()
        if cv2.waitKey(1) & 0xFF == 27:
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    read_camera(0)
