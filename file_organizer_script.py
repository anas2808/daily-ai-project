import os
import shutil
from pathlib import Path

def get_file_category(file_extension):
    """
    Determine the category of a file based on its extension.
    
    Args:
        file_extension (str): The file extension.
        
    Returns:
        str: The category for the file.
    """
    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Music': ['.mp3', '.wav', '.aac'],
        'Videos': ['.mp4', '.avi', '.mov'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
    }

    for category, extensions in categories.items():
        if file_extension.lower() in extensions:
            return category
    return 'Others'

def organize_files(directory):
    """
    Organize files in the specified directory into categorized folders.
    
    Args:
        directory (str): The path to the directory to organize.
    """
    try:
        # Ensure the directory exists
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"The directory '{directory}' does not exist.")
        
        # Iterate over each file in the directory
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            
            # Skip directories
            if os.path.isdir(file_path):
                continue
            
            # Determine file category
            file_extension = os.path.splitext(filename)[1]
            category = get_file_category(file_extension)
            
            # Create category directory if it doesn't exist
            category_dir = os.path.join(directory, category)
            if not os.path.exists(category_dir):
                os.makedirs(category_dir)
            
            # Move file to the appropriate category directory
            shutil.move(file_path, os.path.join(category_dir, filename))
            print(f"Moved '{filename}' to '{category}'")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """
    Main function to execute the file organizer.
    """
    # Specify the directory to organize
    directory_to_organize = input("Enter the directory path to organize: ").strip()
    
    # Organize the files in the specified directory
    organize_files(directory_to_organize)

if __name__ == "__main__":
    main()