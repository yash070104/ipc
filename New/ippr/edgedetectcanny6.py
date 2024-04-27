import cv2

# Load the image in color (24-bit RGB)
image = cv2.imread('color24.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray_image, threshold1=50, threshold2=150)

# Save or display the segmented image
cv2.imwrite('segmented_image.jpg', edges)
cv2.imshow('Segmented Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
