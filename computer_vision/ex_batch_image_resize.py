#write a script that resizes all images in a directory to 100x100.

import cv2
import glob

folder = 'imgs'

image_list = glob.glob(folder+'/*.jpg')
print(image_list)

for img_name in image_list:
    img = cv2.imread(img_name,0)
    resized_img = cv2.resize(img, (100,100))
    new_name = img_name.replace(".jpg","_resized.jpg")

    cv2.imwrite(new_name,resized_img)
