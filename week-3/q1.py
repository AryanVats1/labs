import cv2
import numpy as np
img = cv2.imread('C:/Users/ugcse.PG-CP.000/Desktop/210962216/source.jpg')
blurred = cv2.GaussianBlur(img, (0, 0), 5)
unsharp_mask = cv2.subtract(img, blurred)
enhanced_image = cv2.add(img, unsharp_mask)
cv2.imshow("Original Image", img)
cv2.imshow("Blurred Image", blurred)
cv2.imshow("Unsharp Mask", unsharp_mask)
cv2.imshow("Enhanced Image", enhanced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()