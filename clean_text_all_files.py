import os

def clear_file_contents(directory):
    # Walk through the directory and all subdirectories
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            # Check if it is a file
            if os.path.isfile(file_path):
                # Open the file in write mode, which will clear its contents
                with open(file_path, 'w') as file:
                    file.write('')  # Write an empty string to clear the file
                print(f'Cleared content of file: {file_path}')

# Specify the directory
directory_path = input('Enter path to directory: ')
clear_file_contents(directory_path)
