import os

def rename_files_in_directory(directory, substring_to_remove):
    try:
        # List all files in the directory
        files = os.listdir(directory)
        
        # Iterate over each file in the directory
        for filename in files:
            if substring_to_remove in filename:
                # Construct the new filename by removing the substring
                new_filename = filename.replace(substring_to_remove, "")
                
                # Construct full file paths
                old_file = os.path.join(directory, filename)
                new_file = os.path.join(directory, new_filename)
                
                # Rename the file
                os.rename(old_file, new_file)
                
                print(f'Renamed: "{filename}" -> "{new_filename}"')
            else:
                print(f'Skipped: "{filename}" (substring not found)')
    
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Get user input for directory and substring
    directory = input("Enter the directory path: ")
    substring_to_remove = input("Enter the substring to remove from file names: ")
    
    # Validate directory
    if not os.path.isdir(directory):
        print("Error: The specified directory does not exist.")
        return
    
    # Call the function to rename files
    rename_files_in_directory(directory, substring_to_remove)

if __name__ == "__main__":
    main()
