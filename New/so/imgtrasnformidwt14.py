import cv2
import numpy as np
import pywt

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

    # Apply DWT transformation (Discrete Wavelet Transform)
    coeffs = pywt.dwt2(gray_image, 'haar')
    cA, (cH, cV, cD) = coeffs

    # Apply IDWT transformation (Inverse Discrete Wavelet Transform)
    idwt_image = pywt.idwt2((cA, (cH, cV, cD)), 'haar')

    # Convert the IDWT image back to uint8 format
    idwt_image = np.uint8(idwt_image)

    # Display the IDWT image
    cv2.imshow('IDWT Image', idwt_image)
    cv2.waitKey(0)

    # Calculate the PSNR between the original and IDWT images
    mse_idwt = np.mean((gray_image - idwt_image) ** 2)
    if mse_idwt == 0:
        psnr_idwt = float('inf')
    else:
        max_pixel_value = 255.0
        psnr_idwt = 10 * np.log10((max_pixel_value ** 2) / mse_idwt)

    # Calculate the PSNR of the original image
    mse_original = np.mean((gray_image - gray_image) ** 2)
    if mse_original == 0:
        psnr_original = float('inf')
    else:
        psnr_original = 10 * np.log10((max_pixel_value ** 2) / mse_original)

    # Calculate the PSNR of the transformed image
    mse_transformed = np.mean((gray_image - idwt_image) ** 2)
    if mse_transformed == 0:
        psnr_transformed = float('inf')
    else:
        psnr_transformed = 10 * np.log10((max_pixel_value ** 2) / mse_transformed)

    # Print the PSNR values of the original and transformed images
    print(f"PSNR value comparing Original Image and IDWT Image: {psnr_idwt:.2f} dB")
    if psnr_original == float('inf'):
        print(f"PSNR value of Original Image: Infinite dB")
    else:
        print(f"PSNR value of Original Image: {psnr_original:.2f} dB")
    print(f"PSNR value of Transformed Image: {psnr_transformed:.2f} dB")

    # Close all windows
    cv2.destroyAllWindows()
