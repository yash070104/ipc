import cv2
import numpy as np

# Load the image in color (24-bit RGB)
image = cv2.imread('color24.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Prewitt operator for edge detection
prewitt_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
prewitt_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

# Combine the horizontal and vertical edge images
edge_image = cv2.magnitude(prewitt_x, prewitt_y)
edge_image = np.uint8(edge_image)

# Threshold the edge image to create a binary mask
threshold_value = 50
_, segmented_image = cv2.threshold(edge_image, threshold_value, 255, cv2.THRESH_BINARY)

# Save or display the segmented image
cv2.imwrite('segmented_image.jpg', segmented_image)
cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
