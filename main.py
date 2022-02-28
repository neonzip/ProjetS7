import sys
import cv2
import numpy as np
from boundingbox import *
from colour_mask import *


# Should be launch with the terminal by putting the image to analyse in first parameter
def main():
    # Loading images
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        print("No input image given, so loading default image, hornet.jpg \n")
        print("Correct Usage: python main.py <filename> \n")
        filename = 'Asian-hornet-WP.jpg'

    img = cv2.imread(filename)

    colour_mask(img)
    boundingbox("Hornet_mask.jpg", filename)


main()
