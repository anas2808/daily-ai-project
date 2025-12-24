import os
import shutil

# Hey there! This is my first big project: a File Organizer!
# I'm gonna make some folders and move files into them based on their type.

# First, I need to tell my script what kind of files go into which folder.
# This is like my little rule book!
file_types = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'],
    "Documents": ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx', '.csv'],
    "Videos": ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv'],
    "Audio": ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
    "Archives": ['.zip', '.rar', '.7z', '.tar', '.gz'],
    "Executables": ['.exe', '.msi', '.dmg', '.app', '.bat', '.sh'], # Careful with these!
    "Code": ['.py', '.html', '.css', '.js', '.java', '.c', '.cpp', '.php', '.json', '.xml'],
}

# This function will ask the user which folder they want to clean up.
# It also checks if the folder exists, so we don't try to organize a non-existent place!
def get_target_directory():
    while True:
        target_dir = input("Enter the path of the directory you want to organize (or press Enter to use the current directory): ").strip()
        
        if not target_dir: # If the user just pressed Enter, use where the script is running
            target_dir = os.getcwd()
            print(f"Using current directory: {target_dir}")
            return target_dir
        elif os.path.isdir(target_dir): # Check if the path actually leads to a directory
            return target_dir
        else:
            print("Oops! That's not a valid directory. Please double-check the path and try again.")

# This is the main part where all the organizing happens!
def organize_files(directory_to_organize):
    print(f"\nAlright, let's start organizing files in: {directory_to_organize}")

    # First, I need to make sure all my category folders exist.
    # If they don't, I'll create them!
    for folder_name in file_types.keys():
        folder_path = os.path.join(directory_to_organize, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path) # os.makedirs creates folders, even if parent folders are missing
            print(f"Created folder: {folder_name}/")

    # I also need a special folder for files that don't fit into any category.
    others_folder_path = os.path.join(directory_to_organize, "Others")
    if not os.path.exists(others_folder_path):
        os.makedirs(others_folder_path)
        print(f"Created folder: Others/")

    # Now, I'll go through every single thing in the chosen directory.
    for filename in os.listdir(directory_to_organize):
        file_path = os.path.join(directory_to_organize, filename)

        # I only want to move actual files, not the folders I just made or any other sub-folders.
        if os.path.isfile(file_path):
            # Let's get the file's extension, like '.jpg' or '.pdf'.
            # os.path.splitext splits "myfile.jpg" into ("myfile", ".jpg")
            _, extension = os.path.splitext(filename)
            extension = extension.lower() # Good practice to make it lowercase for easier matching!

            moved_file = False # A little flag to know if I successfully moved the file
            
            # Now, I'll check my 'rule book' to see where this file belongs.
            for category, extensions in file_types.items():
                if extension in extensions:
                    target_folder = os.path.join(directory_to_organize, category)
                    destination_path = os.path.join(target_folder, filename)
                    
                    try:
                        shutil.move(file_path, destination_path) # shutil.move does the actual moving!
                        print(f"Moved '{filename}' to '{category}/'")
                        moved_file = True
                        break # Found a home for it, so I can stop checking other categories
                    except shutil.Error as e:
                        print(f"Error moving '{filename}' to '{category}/': {e}")
                        # This might happen if a file with the same name already exists in the destination
                        # For now, I'll just report the error and move on.
                    except Exception as e: # Catch any other unexpected problems
                        print(f"An unexpected error occurred with '{filename}': {e}")
                        
            # If the file didn't match any of my categories, it goes to 'Others'.
            if not moved_file:
                target_folder = others_folder_path
                destination_path = os.path.join(target_folder, filename)
                try:
                    shutil.move(file_path, destination_path)
                    print(f"Moved '{filename}' to 'Others/'")
                except shutil.Error as e:
                    print(f"Error moving '{filename}' to 'Others/': {e}")
                except Exception as e:
                    print(f"An unexpected error occurred with '{filename}': {e}")

    print("\nFile organization complete! 🎉 Your directory is now much tidier!")
    print("Hope this script was helpful!")

# This makes sure my code only runs when I directly execute the script.
# It's a common Python thing!
if __name__ == "__main__":
    directory = get_target_directory()
    organize_files(directory)