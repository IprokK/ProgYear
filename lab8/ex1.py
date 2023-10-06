import cv2

image_path = 'images/variant-1.jpg'
original_image = cv2.imread(image_path)

gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Photo_new', gray_image)
cv2.waitKey(0)
