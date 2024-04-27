import cv2

# Load the input image
input_image = cv2.imread('new.jpg')

# Check if the image was loaded successfully
if input_image is None:
    print("Error: Unable to load the input image.")
else:
    # Get the height and width of the input image
    height, width = input_image.shape[:2]

    # Define the rotation angle (90 degrees for clockwise, -90 degrees for anti-clockwise)
    angle_clockwise = 90
    angle_anticlockwise = -90

    # Compute the rotation matrix for clockwise and anti-clockwise rotation
    rotation_matrix_clockwise = cv2.getRotationMatrix2D((width / 2, height / 2), angle_clockwise, 1)
    rotation_matrix_anticlockwise = cv2.getRotationMatrix2D((width / 2, height / 2), angle_anticlockwise, 1)

    # Perform the actual rotations
    rotated_image_clockwise = cv2.warpAffine(input_image, rotation_matrix_clockwise, (width, height))
    rotated_image_anticlockwise = cv2.warpAffine(input_image, rotation_matrix_anticlockwise, (width, height))

    # Display the original and rotated images
    cv2.imshow('Original Image', input_image)
    cv2.imshow('Rotated Clockwise', rotated_image_clockwise)
    cv2.imshow('Rotated Anti-Clockwise', rotated_image_anticlockwise)

    # Save the rotated images
    cv2.imwrite('rotated_clockwise.jpg', rotated_image_clockwise)
    cv2.imwrite('rotated_anticlockwise.jpg', rotated_image_anticlockwise)

    # Wait for a key press and then close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
