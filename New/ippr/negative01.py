import cv2

# Load the image in grayscale
image = cv2.imread('input_image.png', cv2.IMREAD_GRAYSCALE)

# Calculate the negative of the image
negative_image = 255 - image

# Save or display the negative image
cv2.imwrite('negative_image.jpg', negative_image)
cv2.imshow('Negative Image', negative_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
