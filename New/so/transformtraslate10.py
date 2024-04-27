import cv2
import numpy as np

# Load the image in color (24-bit RGB)
image = cv2.imread('new.jpg')

# Define the translation parameters (shift values)
shift_right = 20
shift_down = 10

# Create the combined translation matrix for shifting down and right
translation_matrix_combined = np.float32([[1, 0, shift_right], [0, 1, shift_down]])

# Apply the combined translation to the image
translated_image_combined = cv2.warpAffine(image, translation_matrix_combined, (image.shape[1], image.shape[0]))

# Create individual translation matrices for reference
translation_matrix_right = np.float32([[1, 0, shift_right], [0, 1, 0]])
translation_matrix_down = np.float32([[1, 0, 0], [0, 1, shift_down]])

# Apply the translations to the image for individual outputs
translated_image_right = cv2.warpAffine(image, translation_matrix_right, (image.shape[1], image.shape[0]))
translated_image_down = cv2.warpAffine(image, translation_matrix_down, (image.shape[1], image.shape[0]))

# Display or save the translated images
cv2.imshow('Translated Image (Shifted Right)', translated_image_right)
cv2.imshow('Translated Image (Shifted Down)', translated_image_down)
cv2.imshow('Translated Image (Shifted Down & Right)', translated_image_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
