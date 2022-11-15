import cv2
import os
import numpy

DIRECTORY = 'processed_images_after_thresholding'

for _ in os.listdir(DIRECTORY):
    car = cv2.imread(f'{DIRECTORY}/{_}')
    car = car.reshape(-1)
    flag = 0
    for i in car:
        if i == 255:
            print(f"{_} is not a black image!")
            flag = 1
            break
    if flag == 0:
        print(f"{_} is a black image!")
        c = cv2.imread(f'processed_images/{_}')
        cv2.imwrite(f"{DIRECTORY}/{_}", c)




