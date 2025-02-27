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
    - 'l': Jump forward 50 frames.
    - 'h': Jump backward 50 frames.
- Trackbar to navigate through frames.

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
2. Install dependences by running `pip install -r requirements.txt` from the command line.
3. Have the images you want to display in a directory.
4. Run the program with the path to your image directory as an argument:
```
python image_viewer.py /path/to/image/folder
```

(Replace `/path/to/image/folder` with the actual path to the directory containing your images.)

5. To run program for images in a directory with a specific prefix, use `-p` or `--prefix` flag:
```
python image_viewer.py /path/to/image/folder -p prefix_str
```

(Replace `/path/to/image/folder` with the actual path to the directory containing your images, and replace `prefix_str` with the string you want to filter your image files with.)

### Examples

```
python image_viewer.py images/
```
This will display all the images in the `images/` folder in a loop, allowing you to control playback with the keyboard and trackbar.

```
python image_viewer.py images/ -p capture
```
This will display all the images in the 'images/' folder with the prefix "capture" in their filename (e.g. capture-1.png, capture-2.png, ...) in a loop, allowing you to control playback with the keyboard and trackbar. 

## To Do's:

- [x] Documentation format.
- [ ] Response to arrow keys.
- [x] Fast forward or adjustable progress bar.
- [x] Separate program to rename numbered files to ensure correct order.
- [ ] Investigate video input.
- [x] Add a confirmation dialogue for renumber.py. 
- [x] Fast forward and faster rewind.
- [ ] Textbox input to jump to a certain image.

# Renumber

**UPDATE:** The Image Viewer script no longer requires this Renumber helper script. This script had added zero-padding to file names, but this is no longer needed as `natsort` (natural sort) is now used in Image Viewer.

For my initial use case that motivated the image_viewer script, the image files were named with three parts:

1. `capture` or `overlay`: image is just the raw `capture` from the webcam or it is the raw image with outputs from vision algorithms `overlay`ed on top.
2. The image number (e.g. 1, 2, 3, ...1800, 1801 ...)
3. `man` to indicate that our system was using manual control when those images were taken, and blank if not.

As an example, the image files I was working with were labeled like this:

```
capture-1-man.jpg
capture-2-man.jpg
capture-3-man.jpg
...
capture-1800.jpg
capture-1801-man.jpg
capture-1802-man.jpg
capture-1803-man.jpg
capture-1804.jpg
capture-1805.jpg
```

### Problems

1. The images with overlayed vision algorithm outputs were not needed when analyzing new vision algorithms.
2. The numbering system messed up sorting, such that it ordered files 0, 1, 10, 100, 1000, 1001, 1002...

## Renumber

`renumber.py` is a helper script that removes image files that begin with `overlay` and adds zero-padding to the numbered part of the filename.

### Usage

1. Clone this repository to your local machine.
2. Install dependences by running `pip install -r requirements.txt` from the command line.
3. Have the images you want to rename in a directory.
4. Run the program with the path to your image directory as an argument:
```
python renumber.py /path/to/image/folder
```

(Replace `/path/to/image/folder` with the actual path to the directory containing your images.)

### Example

```
python renumber.py images/
```
This will rename all the images in the `images/` folder such that the numbers are zero-padded (up to 4 digits) and images starting with "overlay" are removed.  
