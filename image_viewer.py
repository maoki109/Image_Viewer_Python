import argparse
import cv2 as cv
import os
import sys
import time
from natsort import natsorted


def display_images(directory, prefix):
    """
    Display images in a direcory in sequential order with ability to pause
    and move forward/backwards frame-by-frame with keyboard.
    Navigation with trackbar GUI also supported. 
    """

    # Set variables
    global current_frame
    FPS = 20  # Frames per second
    WINDOW_TITLE = "Image Viewer"

    # Initialize playback variables and load images
    current_frame = 0
    paused = False
    images = [os.path.join(directory, img) for img in natsorted(os.listdir(directory)) if (
        img.endswith(('.png', '.jpg', '.jpeg')) and img.startswith(prefix))]
    # NOTE: natsorted identifies numbers anywhere in a string and sorts them "naturally."
    # If naming convention changes, consider using other variations such as humansorted().

    if not images:
        print("No images found in the directory with given prefix.")
        return

    cv.namedWindow(WINDOW_TITLE, cv.WINDOW_NORMAL)  # Create a resizable window
    cv.createTrackbar("Frame", WINDOW_TITLE, 0, len(
        images) - 1, trackbar)  # Create trackbar

    while True:
        # Load current image
        image_path = images[current_frame]
        image = cv.imread(image_path)
        # image = cv.resize(image, (800, 600)) # resize image to fit window

        if image is None:
            print(f"Failed to load image: {image_path}")
            break

        # Display image and its file path
        cv.putText(image, os.path.basename(image_path), (10, 30),
                   cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        cv.imshow(WINDOW_TITLE, image)
        cv.setTrackbarPos("Frame", WINDOW_TITLE, current_frame)

        # Handle keyboard input
        key = cv.waitKey(1) & 0xFF

        if key == ord(' '):  # space bar for pause/play
            paused = not paused
        elif key == ord('q'):  # 'q' to quit
            break
        elif key == ord('k') and paused:  # 'k' to move forward one image
            current_frame = min(current_frame + 1, len(images) - 1)
        elif key == ord('j') and paused:  # 'j' to move back one image
            current_frame = max(current_frame - 1, 0)
        elif key == ord('l'):  # 'l' to move forward 50 images
            current_frame = min(current_frame + 50, len(images) - 1)
        elif key == ord('h'):  # 'h' to move back 50 images
            current_frame = max(current_frame - 50, 0)

        # Update frame if not paused
        if not paused:
            time.sleep(1.0 / FPS)
            current_frame = (current_frame + 1) % len(images)  # images loop

    cv.destroyAllWindows()


def trackbar(val):
    global current_frame
    current_frame = val


if __name__ == "__main__":
    prefix = ""
    parser = argparse.ArgumentParser()
    # Script must be called with a directory argument
    parser.add_argument("directory", help="path to image folder")
    # Optional argument to specify prefix of file names
    parser.add_argument(
        "-p", "--prefix", help="specify prefix of files to view")
    args = parser.parse_args()
    if args.prefix:
        prefix = args.prefix
    display_images(args.directory, prefix=prefix)
