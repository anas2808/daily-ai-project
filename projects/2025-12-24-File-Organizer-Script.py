import os
import shutil

# --- Configuration Section ---
# This is the main directory we want to organize.
# It's important to change this to the actual path of the folder you want to clean up!
# For example, it could be your 'Downloads' folder.
# On Windows, it might look like: "C:\\Users\\YourName\\Downloads"
# On macOS/Linux, it might look like: "/Users/YourName/Downloads"
source_directory = input("Please enter the FULL path of the directory you want to organize: ")

# This is a dictionary that maps file extensions to the names of folders where they should go.
# I tried to think of all the common file types I have!
organize_map = {
    # Image Files
    '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images', '.gif': 'Images',
    '.bmp': 'Images', '.tiff': 'Images', '.webp': 'Images', '.ico': 'Images',

    # Document Files
    '.pdf': 'Documents', '.doc': 'Documents', '.docx': 'Documents',
    '.txt': 'Documents', '.rtf': 'Documents', '.odt': 'Documents',
    '.xls': 'Documents', '.xlsx': 'Documents', '.csv': 'Documents',
    '.ppt': 'Documents', '.pptx': 'Documents', '.epub': 'Documents',

    # Audio Files
    '.mp3': 'Audio', '.wav': 'Audio', '.aac': 'Audio', '.flac': 'Audio',
    '.ogg': 'Audio', '.wma': 'Audio', '.m4a': 'Audio',

    # Video Files
    '.mp4': 'Videos', '.mov': 'Videos', '.avi': 'Videos', '.mkv': 'Videos',
    '.flv': 'Videos', '.wmv': 'Videos', '.webm': 'Videos', '.mkv': 'Videos',

    # Archive Files (compressed files)
    '.zip': 'Archives', '.rar': 'Archives', '.7z': 'Archives',
    '.tar': 'Archives', '.gz': 'Archives', '.bz2': 'Archives', '.iso': 'Archives',

    # Executable Files and Installers
    '.exe': 'Programs', '.msi': 'Programs', '.dmg': 'Programs', '.app': 'Programs',
    '.deb': 'Programs', '.rpm': 'Programs',

    # Code Files and Scripts
    '.py': 'Code', '.java': 'Code', '.c': 'Code', '.cpp': 'Code',
    '.html': 'Code', '.css': 'Code', '.js': 'Code', '.php': 'Code',
    '.json': 'Code', '.xml': 'Code', '.yml': 'Code', '.yaml': 'Code',
    '.sh': 'Code', '.bat': 'Code',

    # Other common types
    '.torrent': 'Torrents',
    '.psd': 'Design Files', '.ai': 'Design Files', '.sketch': 'Design Files',
}

# This is the folder name for files whose extensions aren't in our `organize_map`.
# They will all go here so we can review them later.
other_folder_name = "Others"

# --- Helper Function to Handle Duplicate File Names ---
# This function makes sure we don't accidentally overwrite files if two files
# have the exact same name but might be different versions or just duplicates.
def get_unique_filename(destination_path, filename):
    base_name, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename # Start with the original filename

    # Keep trying new names until we find one that doesn't exist in the destination
    while os.path.exists(os.path.join(destination_path, new_filename)):
        new_filename = f"{base_name} ({counter}){extension}"
        counter += 1
    return new_filename

# --- Main File Organization Logic ---
def organize_files(directory_to_organize):
    # First, let's make sure the directory actually exists.
    if not os.path.isdir(directory_to_organize):
        print(f"Error: The directory '{directory_to_organize}' does not exist or is not a valid directory.")
        print("Please double-check the path you entered.")
        return # Stop the script if the directory is bad

    print(f"\n--- Starting to organize files in: '{directory_to_organize}' ---")

    try:
        # Get a list of all files and folders directly inside our target directory.
        # We don't go into subfolders for this basic script to keep it simple!
        entries = os.listdir(directory_to_organize)
    except OSError as e:
        print(f"Error accessing directory '{directory_to_organize}'. Permission denied or path is invalid: {e}")
        return

    # Loop through each item (file or folder) in the directory
    for item in entries:
        full_item_path = os.path.join(directory_to_organize, item)

        # We only want to move files, not other folders already present in the source_directory.
        if os.path.isfile(full_item_path):
            # Split the file name into its base and its extension (e.g., "my_photo", ".jpg")
            filename_without_ext, file_extension = os.path.splitext(item)
            file_extension = file_extension.lower() # Convert extension to lowercase for easier matching

            # Figure out which folder this file should go into based on its extension.
            # If the extension isn't in our map, it goes into the 'Others' folder.
            target_folder_name = organize_map.get(file_extension, other_folder_name)
            
            # Build the full path for the destination folder (e.g., "Downloads/Images")
            destination_folder_path = os.path.join(directory_to_organize, target_folder_name)

            # Check if the destination folder exists; if not, create it.
            if not os.path.exists(destination_folder_path):
                try:
                    os.makedirs(destination_folder_path) # os.makedirs can create intermediate folders too!
                    print(f"Created new folder: '{destination_folder_path}'")
                except OSError as e:
                    print(f"Error creating folder '{destination_folder_path}'. Please check permissions: {e}")
                    continue # If we can't create the folder, we can't move the file, so skip to the next file.

            # Get a unique filename for the destination to prevent overwriting.
            unique_filename = get_unique_filename(destination_folder_path, item)
            destination_file_path = os.path.join(destination_folder_path, unique_filename)

            # Finally, move the file!
            try:
                shutil.move(full_item_path, destination_file_path)
                print(f"Moved: '{item}' -> '{target_folder_name}/{unique_filename}'")
            except shutil.Error as e:
                print(f"Failed to move '{item}' to '{destination_folder_path}'. Error: {e}")
            except Exception as e: # Catch any other unexpected issues during the move
                print(f"An unexpected error occurred while moving '{item}': {e}")
        # If it's a directory, we just leave it where it is for this script's purpose.
        # This prevents accidentally trying to move folders that are already organized or sub-directories.

    print(f"\n--- File organization complete for '{directory_to_organize}'! ---")
    print("Hope your folder looks much cleaner now!")

# This makes sure our `organize_files` function runs when the script is executed.
if __name__ == "__main__":
    organize_files(source_directory)