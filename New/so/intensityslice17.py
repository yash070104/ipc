import cv2
import numpy as np

# Load the input image in grayscale
input_image = cv2.imread('8bitgreyslice.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if input_image is None:
    print("Error: Unable to load the input image.")
else:
    # Display the original image
    cv2.imshow('Original Image', input_image)
    cv2.waitKey(0)

    # Define the intensity range to highlight (you can adjust these values as needed)
    lower_threshold = 100
    upper_threshold = 200

    # Preserve background (apply gray-level slicing)
    preserved_image = input_image.copy()
    preserved_image[(input_image >= lower_threshold) & (input_image <= upper_threshold)] = 255

    # Display the image with preserved background
    cv2.imshow('Preserved Background Image', preserved_image)
    cv2.waitKey(0)

    # Non-preserve background (apply gray-level slicing)
    non_preserved_image = input_image.copy()
    non_preserved_image[(input_image >= lower_threshold) & (input_image <= upper_threshold)] = 0

    # Display the image with non-preserved background
    cv2.imshow('Non-preserved Background Image', non_preserved_image)
    cv2.waitKey(0)

    # Save the images
    cv2.imwrite('preserved_background_image.jpg', preserved_image)
    cv2.imwrite('non_preserved_background_image.jpg', non_preserved_image)

    # Close all windows
    cv2.destroyAllWindows()
