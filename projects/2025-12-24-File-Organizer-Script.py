import os
import shutil

def organize_files():
    """
    Organizes files in a specified directory into subfolders based on file type.
    """
    print("Hello! I'm your file organizer. Let's make your folder neat!")

    # Ask the user for the directory path they want to organize
    target_directory = input("Please type the FULL path of the directory you want to organize: ")

    # Check if the path provided is actually a directory that exists
    if not os.path.isdir(target_directory):
        print(f"Oops! It looks like '{target_directory}' isn't a valid directory. Please check the path and try again.")
        return # Exit the function if the directory is invalid

    print(f"Okay, I'm going to start organizing files in: {target_directory}")

    # Define categories and the file extensions that belong to them
    # This is a dictionary where each key is a folder name and its value is a list of extensions
    file_categories = {
        "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.ico'],
        "Documents": ['.pdf', '.doc', '.docx', '.txt', '.odt', '.rtf', '.tex'],
        "Spreadsheets": ['.xls', '.xlsx', '.csv', '.ods'],
        "Presentations": ['.ppt', '.pptx', '.odp'],
        "Videos": ['.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.webm'],
        "Audio": ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.wma', '.m4a'],
        "Archives": ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'],
        "Executables": ['.exe', '.dmg', '.app', '.msi', '.bin'],
        "Code": ['.py', '.java', '.c', '.cpp', '.js', '.html', '.css', '.php', '.rb', '.go', '.sh'],
        "Others": [] # This will be our default for files that don't match any specific category
    }

    # Loop through every item (file or folder) in the chosen directory
    for item in os.listdir(target_directory):
        # Build the full path for the current item
        item_full_path = os.path.join(target_directory, item)

        # We only want to organize actual files, not subdirectories
        if os.path.isfile(item_full_path):
            # Get the file extension (like ".jpg" from "picture.jpg")
            # os.path.splitext returns a tuple: (base, extension)
            _, file_extension = os.path.splitext(item_full_path)
            # Convert the extension to lowercase for easier matching
            file_extension = file_extension.lower()

            # Figure out which category this file belongs to
            destination_folder_name = "Others" # Start by assuming it's 'Others'

            # Go through our defined categories
            for category, extensions in file_categories.items():
                if file_extension in extensions:
                    destination_folder_name = category # We found a match!
                    break # No need to check other categories for this file

            # Create the full path for the destination folder (e.g., "C:/MyFiles/Images")
            destination_folder_path = os.path.join(target_directory, destination_folder_name)

            # If the destination folder doesn't exist yet, create it
            if not os.path.exists(destination_folder_path):
                try:
                    os.makedirs(destination_folder_path)
                    print(f"Created a new folder: '{destination_folder_name}'")
                except OSError as e:
                    print(f"Error: Couldn't create folder '{destination_folder_name}'. Maybe a permission issue? Error: {e}")
                    continue # Skip moving this file if we can't create the folder

            # Create the full path for where the file will end up
            destination_file_path = os.path.join(destination_folder_path, item)

            # Now, move the file!
            try:
                # IMPORTANT: Check if a file with the same name already exists in the destination
                if os.path.exists(destination_file_path):
                    print(f"Skipping '{item}': A file with this name already exists in '{destination_folder_name}'.")
                    continue # Don't overwrite, just skip

                shutil.move(item_full_path, destination_file_path)
                print(f"Moved '{item}' to '{destination_folder_name}/'")
            except shutil.Error as e:
                print(f"Problem moving '{item}': {e}. Maybe a file is open or permissions are wrong.")
            except Exception as e:
                print(f"An unexpected error happened while moving '{item}': {e}")

    print("\nAll done! Your directory should be much cleaner now. Have a great day!")

# This makes sure our `organize_files()` function runs only when the script is executed directly.
if __name__ == "__main__":
    organize_files()