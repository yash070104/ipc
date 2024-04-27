import cv2
import numpy as np

# Load the image in color (24-bit RGB)
image = cv2.imread('color24.jpg')

# Convert RGB to CMY
cmy_image = 255 - image

# Separate the channels
c, m, y = cv2.split(cmy_image)

# Create an all-white channel for the K (black) component
k = np.ones_like(c) * 255

# Merge the CMYK channels back into a 24-bit CMY image
cmy_image = cv2.merge((c, m, y, k))

# Save or display the CMY image
cv2.imwrite('cmy_image.jpg', cmy_image)
cv2.imshow('CMY Image', cmy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
