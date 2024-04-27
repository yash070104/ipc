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

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    # Apply DCT transformation
    dct_image = cv2.dct(np.float32(gray_image))

    # Apply IDCT transformation
    idct_image = cv2.idct(dct_image)

    # Convert the IDCT image back to uint8 format
    idct_image = np.uint8(idct_image)

    # Display the IDCT image
    cv2.imshow('IDCT Image', idct_image)
    cv2.waitKey(0)

    # Calculate the PSNR between the original and IDCT images
    mse_idct = np.mean((gray_image - idct_image) ** 2)
    if mse_idct == 0:
        psnr_idct = float('inf')
    else:
        max_pixel_value = 255.0
        psnr_idct = 10 * np.log10((max_pixel_value ** 2) / mse_idct)
    
    # Calculate the PSNR of the original image
    mse_original = np.mean((gray_image - gray_image) ** 2)
    if mse_original == 0:
        psnr_original = float('inf')
    else:
        psnr_original = 10 * np.log10((max_pixel_value ** 2) / mse_original)

    # Print the PSNR values
    print(f"PSNR value comparing Original Image and IDCT Image: {psnr_idct:.2f} dB")
    print(f"PSNR value of Original Image: {psnr_original:.2f} dB")
    print(f"PSNR value of IDCT Image: {psnr_idct:.2f} dB")

    # Close all windows
    cv2.destroyAllWindows()
