import cv2
import numpy as np

# Load the image in color (24-bit)
image = cv2.imread('new.jpg')

# Calculate the negative of the image
negative_image = 255 - image

# Save or display the negative image
cv2.imwrite('negative_image.jpg', negative_image)
cv2.imshow('Negative Image', negative_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
