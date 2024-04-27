import cv2

# Load the input noisy image
noisy_image = cv2.imread('new.jpg')

# Check if the image was loaded successfully
if noisy_image is None:
    print("Error: Unable to load the input image.")
else:
    # Display the original noisy image
    cv2.imshow('Noisy Image', noisy_image)
    cv2.waitKey(0)

    # Apply Gaussian blur to smooth the image
    kernel_size = (5, 5)  # Adjust kernel size as needed
    smoothed_image = cv2.GaussianBlur(noisy_image, kernel_size, sigmaX=0)

    # Display the smoothed image
    cv2.imshow('Smoothed Image', smoothed_image)
    cv2.waitKey(0)

    # Save the smoothed image
    cv2.imwrite('smoothed_image.jpg', smoothed_image)

    # Close all windows
    cv2.destroyAllWindows()
