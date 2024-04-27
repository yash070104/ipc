import cv2
import matplotlib.pyplot as plt

# Load the image in color (24-bit RGB)
image = cv2.imread('color24.jpg')

# Split the image into RGB channels
b, g, r = cv2.split(image)

# Perform histogram equalization on each channel separately
equalized_b = cv2.equalizeHist(b)
equalized_g = cv2.equalizeHist(g)
equalized_r = cv2.equalizeHist(r)

# Merge the equalized channels back into an RGB image
equalized_image = cv2.merge((equalized_b, equalized_g, equalized_r))

# Calculate histograms for the original and equalized images
histogram_original = cv2.calcHist([image], [0], None, [256], [0, 256])
histogram_equalized = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])

# Plot the original and equalized images along with their histograms
plt.figure(figsize=(12, 8))

# Original Image
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(2, 2, 2)
plt.plot(histogram_original, color='black')
plt.title('Histogram of Original Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# Equalized Image
plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(equalized_image, cv2.COLOR_BGR2RGB))
plt.title('Equalized Image')

plt.subplot(2, 2, 4)
plt.plot(histogram_equalized, color='black')
plt.title('Histogram of Equalized Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
