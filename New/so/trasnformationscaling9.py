import cv2

# Load the image in color (24-bit RGB)
image = cv2.imread('new.jpg')

# Get the original image dimensions
original_height, original_width = image.shape[:2]

# Scale the image by a factor of 2
scaled_image_up = cv2.resize(image, (2 * original_width, 2 * original_height), interpolation=cv2.INTER_LINEAR)

# Scale the image by a factor of 0.5
scaled_image_down = cv2.resize(image, (original_width // 2, original_height // 2), interpolation=cv2.INTER_LINEAR)

# Display or save the scaled images
cv2.imshow('Scaled Image (Factor 2)', scaled_image_up)
cv2.imshow('Scaled Image (Factor 0.5)', scaled_image_down)
cv2.waitKey(0)
cv2.destroyAllWindows()
