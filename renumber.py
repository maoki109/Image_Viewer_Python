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

def user_confirmation(prompt="Are you sure?", valid_responses=("yes", "no")):
    """
    Asks the user for confirmation with a given prompt and validates the response.
    
    Args:
        prompt (str, optional): The question to ask the user. Defaults to "Are you sure?".
        valid_responses (tuple, optional): Valid responses to accept. Defaults to ("yes", "no").
    
    Returns:
        bool: True if the user confirms, False otherwise.
    """
    while True:
        response = input(f"{prompt} ({'/'.join(valid_responses)}) ").lower()
        if response in valid_responses:
            return response == "yes"
        else:
            print("Invalid input. Please enter", '/'.join(valid_responses))

if __name__ == "__main__":
    # Check that script is called with directory argument
    if len(sys.argv) != 2:
        print("Usage: python renumber.py /path/to/image/folder")
        sys.exit(1)

    # Get directory from command line args
    image_directory = sys.argv[1]
    my_prompt = "Are you sure you want to proceed? This will delete all overlay images and reformat the numbering of remaining files."
    if user_confirmation(my_prompt):
        print("Action confirmed. Proceeding...")
        zero_pad_filename(image_directory)
    else:
        print("Action cancelled.")
        sys.exit(1)
