# import the necessary Packages
import numpy as np
import cv2

image = cv2.imread('capsicum.jpg')
cv2.imshow('Original image', image)  # reading the original image
cv2.waitKey(0)  # holds the screen

(h, w, d) = image.shape
print("width = {}, height = {}, depth = {}".format(w, h, d))

# BGR because openCv is kinda weird
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscaled image', grayImage)
cv2.waitKey(0)

print("Original Image = \n", image)
print("Gray Image = \n", grayImage)

#  gives R, G, B values at a particular location
(B, G, R) = image[130, 150]
print("\n Image values \n R = {}, G = {}, B = {}".format(R, G, B))


img = cv2.imread('capsicum2.jpg')
print("Capsicum image:\n \n", img)
print("\n \n ......Image One Channel \n", img[:, :, 0])



# wrong code, won't run, coz now we have just two values or maybe a single value - let's check
# uncomment this below
# (B, G, R) = grayImage[130, 150]
# print("Gray Image values \n R = {}, G = {}, B = {}".format(R, G, B))


B = grayImage[130, 150]  # try with B, W & then with just B
print("\n B = ", B)

'''
-----------Check the IPYNB File-----------


img2 = cv2.imread('capsicum2.jpg', 3)
print("\n img2 = \n", img2)

from PIL import Image
im = Image.open('capsicum2.jpg')
pixels = list(im.getdata())
print("\n Pixels = \n", pixels)
im.show()
'''