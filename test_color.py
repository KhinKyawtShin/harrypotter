import cv2
import numpy as np

def visualize_hsv_range(lower_hsv, upper_hsv):
    # Create an image of 100x100 pixels
    hsv_image = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Fill the image with the median HSV value
    median_hsv = ((lower_hsv + upper_hsv) // 2).astype(np.uint8)
    hsv_image[:, :] = median_hsv

    # Convert the HSV image to BGR for display
    bgr_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    # Display the image
    cv2.imshow('HSV Color Range Visualization', bgr_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    lower_pink = np.array([120, 100, 50]) 
    upper_pink = np.array([160, 255, 200])

    visualize_hsv_range(lower_pink, upper_pink)