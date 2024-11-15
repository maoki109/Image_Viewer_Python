import cv2 as cv
import os
import sys
import time

def display_images(directory):
    """
    Display images in a direcory in sequential order with ability to pause
    and move forward/backwards frame-by-frame.
    """

    # Set variables
    FPS = 20 # Frames per second
    WINDOW_TITLE = "Image Viewer"

    # Initialize playback variables and load images
    current_frame = 0
    paused = False
    images = [os.path.join(directory, img) for img in sorted(os.listdir(directory)) if img.endswith(('.png', '.jpg', '.jpeg'))]

    cv.namedWindow(WINDOW_TITLE, cv.WINDOW_NORMAL)  # Create a resizable window

    while True:
        # Load current image
        image_path = images[current_frame]
        image = cv.imread(image_path)
        image = cv.resize(image, (800, 600)) # resize image to fit window

        # Display image and its file path
        cv.putText(image, os.path.basename(image_path), (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        cv.imshow(WINDOW_TITLE, image)

        # Handle keyboard input
        key = cv.waitKey(1) & 0xFF

        if key == ord(' '): # space bar for pause/play
            paused = not paused
        elif key == ord('q'): # 'q' to quit
            break
        elif key == ord('k') and paused: # 'k' to move forward one image
            current_frame = min(current_frame + 1, len(images) - 1)
        elif key == ord('j') and paused: # 'j' to move back one image
            current_frame = max(current_frame - 1, 0)

        # Update frame if not paused
        if not paused:
            time.sleep(1.0 / FPS)
            current_frame = (current_frame + 1) % len(images) # images loop

    cv.destroyAllWindows()

if __name__ == "__main__":
    # Check that script is called with directory argument
    if len(sys.argv) != 2:
        print("Usage: python image_viewer.py /path/to/image/folder")
        sys.exit(1)

    # Get directory from command line args
    image_directory = sys.argv[1]
    display_images(image_directory)