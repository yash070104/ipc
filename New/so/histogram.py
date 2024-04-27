import cv2
import matplotlib.pyplot as plt

# Load the image in color (24-bit RGB)
image = cv2.imread('new.jpg')

# Split the image into RGB channels
b, g, r = cv2.split(image)

# Calculate histograms for each channel
histogram_b = cv2.calcHist([b], [0], None, [256], [0, 256])
histogram_g = cv2.calcHist([g], [0], None, [256], [0, 256])
histogram_r = cv2.calcHist([r], [0], None, [256], [0, 256])

# Plot the histograms
plt.figure(figsize=(8, 6))

# Plot histogram for blue channel
plt.subplot(3, 1, 1)
plt.plot(histogram_b, color='blue')
plt.title('Histogram of Blue Channel')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# Plot histogram for green channel
plt.subplot(3, 1, 2)
plt.plot(histogram_g, color='green')
plt.title('Histogram of Green Channel')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# Plot histogram for red channel
plt.subplot(3, 1, 3)
plt.plot(histogram_r, color='red')
plt.title('Histogram of Red Channel')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
