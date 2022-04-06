import cv2
import numpy as np

img = cv2.imread("./bilder/plan_link2.jpg")
# minimum value of brown pixel in BGR order -> burleywood
COLOR_MIN = np.array([128, 255, 255], np.uint8)
# maximum value of brown pixel in BGR order -> brown
COLOR_MAX = np.array([128, 255, 255], np.uint8)

dst = cv2.inRange(img, COLOR_MIN, COLOR_MAX)
no_brown = cv2.countNonZero(dst)
if no_brown > 0:
    print("ausfall")
else:
    print("kein ausfall")