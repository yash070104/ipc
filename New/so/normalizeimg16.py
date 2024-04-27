import cv2
import numpy as np

# Load the input image
input_image = cv2.imread('new.jpg')

# Check if the image was loaded successfully
if input_image is None:
    print("Error: Unable to load the input image.")
else:
    # Display the original image
    cv2.imshow('Original Image', input_image)
    cv2.waitKey(0)

    # Normalize the image to the range [0, 1]
    normalized_image = input_image.astype(np.float32) / 255.0

    # Display the normalized image (scaled between 0 and 1)
    cv2.imshow('Normalized Image', normalized_image)
    cv2.waitKey(0)

    # Save the normalized image
    cv2.imwrite('normalized_image.jpg', normalized_image * 255)

    # Close all windows
    cv2.destroyAllWindows()
