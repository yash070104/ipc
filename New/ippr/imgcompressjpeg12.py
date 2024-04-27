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

    # Apply JPEG compression to the image with a compression factor (quality) of 90
    jpeg_quality = 90
    compressed_image_path = 'compressed_image.jpg'
    cv2.imwrite(compressed_image_path, input_image, [int(cv2.IMWRITE_JPEG_QUALITY), jpeg_quality])

    # Load and display the compressed image
    compressed_image = cv2.imread(compressed_image_path)
    cv2.imshow('Compressed Image', compressed_image)
    cv2.waitKey(0)

    # Calculate the PSNR between the original and compressed images
    mse_compressed = np.mean((input_image - compressed_image) ** 2)
    if mse_compressed == 0:
        psnr_compressed = float('inf')
    else:
        max_pixel_value = 255.0
        psnr_compressed = 10 * np.log10((max_pixel_value ** 2) / mse_compressed)
    
    # Calculate the PSNR between the original and decompressed images
    mse_decompressed = np.mean((input_image - compressed_image) ** 2)
    if mse_decompressed == 0:
        psnr_decompressed = float('inf')
    else:
        max_pixel_value = 255.0
        psnr_decompressed = 10 * np.log10((max_pixel_value ** 2) / mse_decompressed)

    # Print the PSNR values
    print(f"PSNR value comparing Original Image and Compressed Image: {psnr_compressed:.2f} dB")
    print(f"PSNR value of Original Image: {psnr_decompressed:.2f} dB")
    print(f"PSNR value of Compressed Image: {psnr_compressed:.2f} dB")
    
    # Close all windows
    cv2.destroyAllWindows()
