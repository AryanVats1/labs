import cv2
import numpy as np
image = cv2.imread("C:/Users/ugcse.PG-CP.000/Desktop/210962216/matrix.jfif", cv2.IMREAD_GRAYSCALE)
blurred_image = cv2.GaussianBlur(image, (5, 5), 1.4)
gradient_x = cv2.Sobel(blurred_image, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(blurred_image, cv2.CV_64F, 0, 1, ksize=3)
gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
gradient_direction = np.arctan2(gradient_y, gradient_x) * (180 / np.pi)
edges = cv2.Canny(blurred_image, threshold1=30, threshold2=100, apertureSize=3, L2gradient=True)
cv2.imshow("Original Image", image)
cv2.imshow("Detected Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
