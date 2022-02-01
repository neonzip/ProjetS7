import sys
import cv2
import numpy as np


def run():
    # Loading images
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        print("No input image given, so loading default image, hornet.jpg \n")
        print("Correct Usage: python main.py <filename> \n")
        filename = 'Asian-hornet-WP.jpg'

    img = cv2.imread(filename)

    # CONVERT TO HSV COLORS
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    color1 = (10, 200, 20)  # orange
    color2 = (28, 255, 255)  # yellow

    color3 = (0, 50, 0)  # black
    color4 = (15, 200, 140)  # brown

    # Define threshold color range to filter
    mask1 = cv2.inRange(hsv_img, color1, color2)  # Mask for orange to yellow colors
    mask2 = cv2.inRange(hsv_img, color3, color4)  # Mask for brown to black colors

    # Bitwise-AND mask and original image
    resOrangeToYellow = cv2.bitwise_and(hsv_img, hsv_img, mask=mask1)
    resBrownToBlack = cv2.bitwise_and(hsv_img, hsv_img, mask=mask2)

    # Addition of the two masks
    res_hsv = cv2.addWeighted(resBrownToBlack, 1, resOrangeToYellow, 1, 0)
    res = cv2.cvtColor(res_hsv, cv2.COLOR_HSV2BGR)

    # Computing ratio of the color range Orange/Yellow
    ratioOfOrangeToYellow = cv2.countNonZero(mask1) / (hsv_img.size / 3)
    print('pixel percentage:', np.round(ratioOfOrangeToYellow * 100, 2))

    cv2.imshow("orange to yellow mask hornet", resOrangeToYellow)
    cv2.imshow("brown to black mask hornet", resBrownToBlack)
    cv2.imshow("Hornet masked", res)
    cv2.imwrite('Hornet_mask.jpg', res)
    cv2.waitKey()


run()
