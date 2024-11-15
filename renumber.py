import os
import re
import sys

def zero_pad_filename(directory):
    """
    Delete files starting with 'overlay' and reformat image files to have
    zero-padded numbers for accurate sorting.
    """
    # Check that directory exists
    if not os.path.isdir(directory):
        print(f"Eror: {directory} is not a valid directory.")
        return 
    
    # Regex pattern to match file names with numeric parts
    pattern = re.compile(r"^(.*?)(\d+)(.*)$")

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip if it is not a file
        if not os.path.isfile(file_path):
            continue

        # Delete files that start with "overlay"
        if filename.startswith("overlay"):
            print(f"Deleting file: {filename}")
            os.remove(file_path)
            continue

        # Reformat filenames 
        match = pattern.match(filename)
        if match:
            prefix, number, suffix = match.groups()
            # Zero pad numbers to 4 digits
            new_filename = f"{prefix}{int(number):04d}{suffix}"
            new_file_path = os.path.join(directory, new_filename)

            # Rename file if name is different
            if new_filename != filename:
                print(f"Renaming: {filename} -> {new_filename}")
                os.rename(file_path, new_file_path)

if __name__ == "__main__":
    # Check that script is called with directory argument
    if len(sys.argv) != 2:
        print("Usage: python renumber.py /path/to/image/folder")
        sys.exit(1)

    # Get directory from command line args
    image_directory = sys.argv[1]
    zero_pad_filename(image_directory)
