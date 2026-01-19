import os
import sys
from typing import List

def get_files_in_directory(directory: str) -> List[str]:
    """
    Retrieves a list of filenames from the specified directory.

    :param directory: The directory path to scan for files.
    :return: A list of filenames in the directory.
    """
    try:
        files = os.listdir(directory)
        return [f for f in files if os.path.isfile(os.path.join(directory, f))]
    except OSError as e:
        print(f"Error accessing directory {directory}: {e}")
        sys.exit(1)

def rename_files(directory: str, prefix: str) -> None:
    """
    Renames files in the specified directory by adding a prefix.

    :param directory: The directory containing files to rename.
    :param prefix: The prefix to add to each filename.
    """
    files = get_files_in_directory(directory)
    for filename in files:
        new_name = prefix + filename
        try:
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            print(f"Renamed '{filename}' to '{new_name}'")
        except OSError as e:
            print(f"Error renaming file {filename} to {new_name}: {e}")

def main():
    """
    Main function to run the bulk file renamer.
    """
    if len(sys.argv) != 3:
        print("Usage: python bulk_rename.py <directory> <prefix>")
        sys.exit(1)

    directory = sys.argv[1]
    prefix = sys.argv[2]

    if not os.path.isdir(directory):
        print(f"The specified directory does not exist: {directory}")
        sys.exit(1)

    rename_files(directory, prefix)

if __name__ == "__main__":
    main()