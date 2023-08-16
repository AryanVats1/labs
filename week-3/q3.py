import cv2
image = cv2.imread("C:/Users/ugcse.PG-CP.000/Desktop/210962216/source.jpg")
kernel_size = 5
box_filtered = cv2.boxFilter(image, -1, (kernel_size, kernel_size))
gaussian_filtered = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
cv2.imshow("Original Image", image)
cv2.imshow("Box Filtered Image", box_filtered)
cv2.imshow("Gaussian Filtered Image", gaussian_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()