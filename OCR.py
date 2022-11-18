import os
import pytesseract
from pytesseract import Output
import cv2 as cv

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\djsce.student\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
VALID_CHARACTERS = 'a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9'
VALID_CHARACTERS = VALID_CHARACTERS.upper()
VALID_CHARACTERS = VALID_CHARACTERS.split(" ")


# For all images in directory
for i in os.listdir('processed_images_after_thresholding'):
    image = cv.imread(f'processed_images_after_thresholding/{i}')
    car_name = i.split(".")[0]

    myconfig = r"--psm 13 --oem 3"
    data = pytesseract.image_to_data(image, config=myconfig, output_type=Output.DICT)

    flattened_text = ''
    for _ in data['text']:
        flattened_text = flattened_text + _

    seperated_text = []
    for _ in flattened_text:
        seperated_text.append(_)

    for _ in seperated_text:
        if _ not in VALID_CHARACTERS:
            seperated_text.remove(_)
    
    for _ in seperated_text:
        if _ in [".", "!", "|", "<", ",", "(", ")", "[", "]", "="]:
            seperated_text.remove(_)

    flattened_text = ''
    for _ in seperated_text:
        flattened_text = flattened_text + _

    with open('Results.txt','a') as f:
        if len(flattened_text) > 4:
            f.write(f'{car_name} : ' + flattened_text + '\n')


# For one image only

# image = cv.imread(f'processed_images/Cars37.png')
#
# myconfig = r"--psm 8 --oem 3"
# data = pytesseract.image_to_data(image, config=myconfig, output_type=Output.DICT)
#
# flattened_text = ''
# for _ in data['text']:
#     flattened_text = flattened_text + _
#
# seperated_text = []
# for _ in flattened_text:
#     seperated_text.append(_)
#
# for _ in seperated_text:
#     if _ not in VALID_CHARACTERS:
#         seperated_text.remove(_)
#
# flattened_text = ''
# for _ in seperated_text:
#     flattened_text = flattened_text + _
# print(flattened_text)
