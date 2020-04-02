from util.adb import Adb
import cv2
import numpy
while True:
    screen = cv2.imdecode(numpy.fromstring(Adb.exec_out('screencap -p'), dtype=numpy.uint8), 0)