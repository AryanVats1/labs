import cv2
import numpy as np
img = cv2.imread("C:/Users/ugcse.PG-CP.000/Desktop/210962216/download.jfif", 0)
target = cv2.imread("C:/Users/ugcse.PG-CP.000/Desktop/210962216/source.jpg", 0)
cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
source_hist, _ = np.histogram(img.flatten(), bins=256, range=[0, 256])
target_hist, _ = np.histogram(target.flatten(), bins=256, range=[0, 256])
source_cdf = source_hist.cumsum()
target_cdf = target_hist.cumsum()
source_cdf_normalized = source_cdf * 255 / source_cdf[-1]
target_cdf_normalized = target_cdf * 255 / target_cdf[-1]
mapping = np.interp(source_cdf_normalized, target_cdf_normalized, range(256))
matched_image = mapping[img]
cv2.imshow('Matched Image', matched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
