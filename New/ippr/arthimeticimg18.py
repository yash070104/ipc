import cv2

# Load the first input image
input_image1 = cv2.imread('8bitgrey.jpg', cv2.IMREAD_GRAYSCALE)

# Load the second input image
input_image2 = cv2.imread('8bitgreyslice.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the images were loaded successfully
if input_image1 is None or input_image2 is None:
    print("Error: Unable to load the input images.")
else:
    # Check if the images have the same dimensions
    if input_image1.shape != input_image2.shape:
        # Resize the second image to match the size of the first image
        input_image2_resized = cv2.resize(input_image2, (input_image1.shape[1], input_image1.shape[0]))
    else:
        input_image2_resized = input_image2

    # Display the original images
    cv2.imshow('Input Image 1', input_image1)
    cv2.imshow('Input Image 2', input_image2_resized)
    cv2.waitKey(0)

    # Perform addition of two images
    added_image = cv2.add(input_image1, input_image2_resized)

    # Display the image after addition
    cv2.imshow('Added Image', added_image)
    cv2.waitKey(0)

    # Perform subtraction of two images
    subtracted_image = cv2.subtract(input_image1, input_image2_resized)

    # Display the image after subtraction
    cv2.imshow('Subtracted Image', subtracted_image)
    cv2.waitKey(0)

    # Save the images
    cv2.imwrite('added_image.jpg', added_image)
    cv2.imwrite('subtracted_image.jpg', subtracted_image)

    # Close all windows
    cv2.destroyAllWindows()
