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

    # Specify the color channel to enhance (0 for Blue, 1 for Green, 2 for Red)
    channel_to_enhance = 2  # Enhance the Red channel in this example

    # Specify the enhancement factor (you can adjust this as needed)
    enhancement_factor = 1.5  # Increase the Red channel intensity by 50%

    # Split the image into its RGB channels
    b, g, r = cv2.split(input_image)

    # Enhance the selected color channel by multiplying with the enhancement factor
    enhanced_channel = cv2.multiply(r if channel_to_enhance == 2 else g if channel_to_enhance == 1 else b,
                                    enhancement_factor)

    # Merge the enhanced channel back with the other channels
    merged_image = cv2.merge((b, g, enhanced_channel)) if channel_to_enhance == 2 \
        else cv2.merge((b, enhanced_channel, r)) if channel_to_enhance == 1 \
        else cv2.merge((enhanced_channel, g, r))

    # Display the enhanced image
    cv2.imshow('Enhanced Image', merged_image)
    cv2.waitKey(0)

    # Save the enhanced image
    cv2.imwrite('enhanced_image.jpg', merged_image)

    # Close all windows
    cv2.destroyAllWindows()
