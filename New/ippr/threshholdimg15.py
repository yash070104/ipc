import cv2

# Load the input image in grayscale
input_image = cv2.imread('8bitgrey.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if input_image is None:
    print("Error: Unable to load the input image.")
else:
    # Display the original image
    cv2.imshow('Original Image', input_image)
    cv2.waitKey(0)

    # Specify the threshold value (you can adjust this as needed)
    threshold_value = 128

    # Apply thresholding to create a binary image
    _, binary_image = cv2.threshold(input_image, threshold_value, 255, cv2.THRESH_BINARY)

    # Display the binary image
    cv2.imshow('Binary Image', binary_image)
    cv2.waitKey(0)

    # Save the binary image
    cv2.imwrite('binary_image.jpg', binary_image)

    # Close all windows
    cv2.destroyAllWindows()
