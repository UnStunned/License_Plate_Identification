import cv2
import os
import numpy

car = cv2.imread('processed_images/Cars0.png', 0)
cv2.imshow('car1', car)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret, car = cv2.threshold(car, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('car2', car)
cv2.waitKey(0)
cv2.destroyAllWindows()
