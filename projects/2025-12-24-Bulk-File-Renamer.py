import os
import sys

def get_target_directory():
    """Prompts the user for a directory path and validates it."""
    while True:
        target_dir = input("Enter the directory path where your files are located: ").strip()
        if not target_dir:
            print("Directory path cannot be empty. Please try again.")
        elif not os.path.isdir(target_dir):
            print(f"Error: '{target_dir}' is not a valid directory. Please try again.")
        else:
            return target_dir

def get_files_in_directory(directory_path):
    """Retrieves a list of files from the specified directory."""
    files = []
    try:
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)
            if os.path.isfile(item_path):
                files.append(item)
    except OSError as e:
        print(f"Error accessing directory '{directory_path}': {e}")
        sys.exit(1)
    return files

def get_renaming_choice():
    """Displays renaming options and gets the user's choice."""
    print("\nChoose a renaming option:")
    print("1. Find and Replace (e.g., 'image_v1.jpg' -> 'photo_v1.jpg')")
    print("2. Add Prefix (e.g., 'document.pdf' -> 'FINAL_document.pdf')")
    print("3. Add Suffix (e.g., 'report.docx' -> 'report_v2.docx')")
    print("4. Add Numbering (e.g., 'file.txt' -> 'file_001.txt')")
    while True:
        choice = input("Enter your choice (1/2/3/4): ").strip()
        if choice in ['1', '2', '3', '4']:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

def get_find_replace_strings():
    """Gets the find and replace strings from the user."""
    find_str = input("Enter the string to find: ")
    replace_str = input("Enter the string to replace it with: ")
    return find_str, replace_str

def get_prefix_string():
    """Gets the prefix string from the user."""
    return input("Enter the prefix to add: ")

def get_suffix_string():
    """Gets the suffix string from the user."""
    return input("Enter the suffix to add: ")

def get_numbering_options():
    """Gets starting number and padding for numbering from the user."""
    while True:
        try:
            start_num_str = input("Enter starting number for numbering (e.g., 1): ")
            padding_str = input("Enter number of digits for padding (e.g., 3 for 001, 002): ")

            start_num = int(start_num_str)
            padding = int(padding_str)

            if start_num <= 0:
                print("Starting number must be a positive integer.")
                continue
            if padding <= 0:
                print("Padding must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid number. Please enter an integer.")
    return start_num, padding

def generate_new_names(files, choice, find_str=None, replace_str=None, prefix=None, suffix=None, start_num=None, padding=None):
    """Generates a map of old names to new names based on the chosen option."""
    rename_map = {}
    file_counter = start_num if start_num is not None else 0 # For numbering

    for old_name in files:
        new_name = old_name
        base_name, extension = os.path.splitext(old_name)

        if choice == '1':  # Find and Replace
            if find_str and find_str in new_name:
                new_name = new_name.replace(find_str, replace_str)
        elif choice == '2': # Add Prefix
            if prefix:
                new_name = prefix + new_name
        elif choice == '3': # Add Suffix
            if suffix:
                new_name = base_name + suffix + extension
        elif choice == '4': # Add Numbering
            if start_num is not None and padding is not None:
                number_str = str(file_counter).zfill(padding)
                new_name = f"{base_name}_{number_str}{extension}"
                file_counter += 1

        if new_name != old_name:
            rename_map[old_name] = new_name
    return rename_map

def preview_changes(rename_map):
    """Displays a preview of the renaming changes."""
    if not rename_map:
        print("\nNo files will be renamed based on your criteria.")
        return False
    print("\n--- Renaming Preview ---")
    for old_name, new_name in rename_map.items():
        print(f"'{old_name}' -> '{new_name}'")
    print("------------------------")
    return True

def execute_renames(directory_path, rename_map):
    """Executes the renaming operations."""
    if not rename_map:
        print("No renames to execute.")
        return

    print("\nAttempting to rename files...")
    success_count = 0
    fail_count = 0
    for old_name, new_name in rename_map.items():
        old_path = os.path.join(directory_path, old_name)
        new_path = os.path.join(directory_path, new_name)
        try:
            # Check if new_path already exists to prevent overwriting without warning
            if os.path.exists(new_path):
                print(f"Warning: New file '{new_name}' already exists. Skipping '{old_name}' to prevent overwrite.")
                fail_count += 1
                continue

            os.rename(old_path, new_path)
            print(f"Renamed '{old_name}' to '{new_name}'")
            success_count += 1
        except OSError as e:
            print(f"Error renaming '{old_name}' to '{new_name}': {e}")
            fail_count += 1
    print(f"\nRenaming complete. {success_count} successful, {fail_count} failed.")

def main():
    """Main function to run the Bulk File Renamer."""
    print("Welcome to the Bulk File Renamer!")

    target_directory = get_target_directory()
    print(f"Targeting directory: {target_directory}")

    all_files = get_files_in_directory(target_directory)
    if not all_files:
        print("No files found in the specified directory. Exiting.")
        sys.exit(0)
    
    # Sort files for predictable numbering
    all_files.sort()
    print(f"Found {len(all_files)} files in the directory.")

    renaming_choice = get_renaming_choice()

    # Variables to hold parameters for chosen renaming mode
    find_str = None
    replace_str = None
    prefix = None
    suffix = None
    start_num = None
    padding = None

    if renaming_choice == '1': # Find and Replace
        find_str, replace_str = get_find_replace_strings()
        if not find_str:
            print("Find string cannot be empty. Exiting.")
            sys.exit(0)
    elif renaming_choice == '2': # Add Prefix
        prefix = get_prefix_string()
        if not prefix:
            print("Prefix cannot be empty. Exiting.")
            sys.exit(0)
    elif renaming_choice == '3': # Add Suffix
        suffix = get_suffix_string()
        if not suffix:
            print("Suffix cannot be empty. Exiting.")
            sys.exit(0)
    elif renaming_choice == '4': # Add Numbering
        start_num, padding = get_numbering_options()

    rename_map = generate_new_names(all_files, renaming_choice, find_str, replace_str, prefix, suffix, start_num, padding)

    if not preview_changes(rename_map):
        sys.exit(0)

    confirmation = input("Do you want to proceed with these renames? (yes/no): ").strip().lower()
    if confirmation == 'yes':
        execute_renames(target_directory, rename_map)
    else:
        print("Renaming cancelled.")

if __name__ == "__main__":
    main()