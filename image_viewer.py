import cv2 as cv
import os
import time
import argparse

# Parse command line argument to get folder path
parser = argparse.ArgumentParser(description="Display images from a folder like a video.")
parser.add_argument("folder", type=str, help="File path to the folder containing images to view.")
args = parser.parse_args()

# Set variables
IMAGE_FOLDER = args.folder
FPS = 1 # Frames per second
WINDOW_TITLE = "Image Viewer"

# Initialize playback variables and load images
current_frame = 0
paused = False
images = [os.path.join(IMAGE_FOLDER, img) for img in sorted(os.listdir(IMAGE_FOLDER)) if img.endswith(('.png', '.jpg', '.jpeg'))]

cv.namedWindow(WINDOW_TITLE, cv.WINDOW_NORMAL)  # Create a resizable window

while True:
    # Load current image
    image_path = images[current_frame]
    image = cv.imread(image_path)
    image = cv.resize(image, (800, 600)) # resize image to fit window

    # Display image and its file path
    cv.putText(image, os.path.basename(image_path), (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    cv.imshow(WINDOW_TITLE, image)

    start_time = time.time() # for FSP control

    # Handle keyboard input
    key = cv.waitKey(1) & 0xFF

    if key == ord(' '): # space bar for pause/play
        paused = not paused
    elif key == ord('q'): # 'q' to quit
        break
    elif key == 83: # right arrow key to move forward one image
        current_frame = min(current_frame + 1, len(images) - 1)
    elif key == 81: # left arrow key to move back one image
        current_frame = max(current_frame - 1, 0)

    # Update frame if not paused
    if not paused:
        current_frame = (current_frame + 1) % len(images)

    # FPS
    elapsed_time = time.time() - start_time
    delay = max(1, int((1.0 / FPS - elapsed_time) * 1000))
    cv.waitKey(delay)

cv.destroyAllWindows()