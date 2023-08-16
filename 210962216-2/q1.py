import cv2
import numpy as np
img = cv2.imread("C:/Users/ugcse.PG-CP.000/Desktop/210962216/download.jfif", 0)
cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
equalized_image = cv2.equalizeHist(img)
cv2.imshow("Equalized Image (OpenCV)", equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
hist, bins = np.histogram(img.flatten(), bins=256, range=[0, 256])
cdf = hist.cumsum()
cdf_normalized = cdf * 255 / cdf[-1]
equalized_image_manual = np.interp(img, bins[:-1], cdf_normalized).astype(np.uint8)
cv2.imshow("Equalized Image (Manual)", equalized_image_manual)
cv2.waitKey(0)
cv2.destroyAllWindows()
