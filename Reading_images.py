import cv2
import os
import numpy
from xml.dom import minidom

edge_enhancement_kernel = numpy.ones((3, 3)) / -8
edge_enhancement_kernel[1][1] = 1

sharpening_kernel = numpy.zeros((3, 3))
sharpening_kernel[1][1] = 5
sharpening_kernel[1][0] = -1
sharpening_kernel[0][1] = -1
sharpening_kernel[2][1] = -1
sharpening_kernel[1][2] = -1

reading_directory = "images"
writing_directory = "processed_images"

for _ in os.listdir(reading_directory):
    car = cv2.imread(f'images/{_}', -1)
    car = cv2.filter2D(car, -1, sharpening_kernel)
    car = cv2.cvtColor(car, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f"{writing_directory}/{_}", car)

annotations_directory = 'annotations'

for _ in os.listdir(annotations_directory):
    current_car = _.split(".")[0]

    tree = minidom.parse(f'annotations/{_}')
    xmin = tree.getElementsByTagName('xmin')
    xmin_value = int(xmin[0].firstChild.data)

    ymin = tree.getElementsByTagName('ymin')
    ymin_value = int(ymin[0].firstChild.data)

    xmax = tree.getElementsByTagName('xmax')
    xmax_value = int(xmax[0].firstChild.data)

    ymax = tree.getElementsByTagName('ymax')
    ymax_value = int(ymax[0].firstChild.data)

    pre_result = cv2.imread(f'processed_images/{current_car}.png', -1)
    final_output = pre_result[ymin_value:ymax_value, xmin_value:xmax_value]
    cv2.imwrite(f"{writing_directory}/{current_car}.png", final_output)

