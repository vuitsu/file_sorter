import os
import shutil

def sort_files_by_extension():
    path = input("Enter the path of the directory: ")

    # Get a list of all files in the specified directory
    files = os.listdir(path)

    # Create a dictionary to store the file extensions as keys and lists of
    # corresponding files as values
    files_by_extension = {}

    # Iterate over the list of files
    for file in files:
        # Get the file extension
        extension = os.path.splitext(file)[1][1:]

        # If the file extension is not already a key in the dictionary, add it
        if extension not in files_by_extension:
            files_by_extension[extension] = []

        # Add the file to the list of files for the corresponding extension
        files_by_extension[extension].append(file)

    # Create a directory for each file extension
    for extension in files_by_extension:
        os.mkdir(path + '/' + extension)

    # Move the files to the appropriate directories
    for extension in files_by_extension:
        for file in files_by_extension[extension]:
            shutil.move(path + '/' + file, path + '/' + extension + '/' + file)

# Call the function
sort_files_by_extension()
