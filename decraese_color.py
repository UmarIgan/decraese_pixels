import cv2
import numpy as np
image=cv2.imread("image path here")
def color_number(image, number_of_color):
    keys=[i for i in range(1, 256)]
    values=[i for i in range(0, 256)]
    values2=(np.array([values, values, values])).T #create a dict with number of colors for hsv colors.
    dicti={key:values2 for key, values2, in zip(keys, values2)}
    upper=np.array(dicti[number_of_color][0:3], dtype='uint8')
    lower = np.array([0, 0, 0], dtype = "uint8")
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)
    cv2.imshow("image", output)#The image with decreased color
    cv2.imshow("image", image)#orginal image
    cv2.waitKey(0)
color_number(image, 210)#test
