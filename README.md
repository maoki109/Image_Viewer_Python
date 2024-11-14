# Image_Viewer_Python

This Python program displays images from a specified directory in a video-like sequence, allowing users to navigate through images. The programs shows each image at an adjustable frames-per-second (FPS) rate, displays the image file name at the top of the window, and provides controls for pausing, playing, and stepping through frames. 

## Motivation

This program works best for sequential images, such as frames captures from a live stream. The motivation behind this program was to be able to view a large set of images taken from a webcam and to be able to pause and step through the frames when a closer analysis was needed. For example, there was a project that was using object detection and segmentation in a driving scenario and frames from the webcam were captured. This program would allow us to view the captured images quickly in a video-like sequence, while also giving us the ability to pause and analyze certain frames as necessary. 

## Features:

- Play images like a video with a set FPS rate. 
- File name of the current image is displayed at the top of the screen. 
- Keyboard controls:
    - Spacebar: Pause/play.
    - 'q': Quit the program.
    - 'k': Step forward one frame.
    - 'j': Step backward one frame. 

## Prerequisites:

- Python 3
- OpenCV (cv2)

### Install OpenCV

You can install openCV using pip:

```
pip install opencv-python
```

## Usage

1. Clone this repository to your local machine. 
2. Have the images you want to display in a directory.
3. Run the program with the path to your image directory as an argument:
```
python image_viewer.py /path/to/image/folder
```

(Replace `/path/to/image/folder` with the actual path to the directory containing your images.)

### Example

```
python image_viewer.py images/
```
This will display all the images in the `images/` folder in a loop, allowing you to control playback with the keyboard. 

# To Do's:

There are still items that need to be fixed for this program:
- [x] Response to keyboard input.
- [x] Check that frames are paused when using arrow keys. 
- [ ] Response to arrow keys. 
- [ ] Separate program to rename numbered files to ensure correct order. 
