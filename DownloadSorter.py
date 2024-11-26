import os
import shutil


def get_download_path():
    """Determine the user's Downloads folder based on the operating system."""
    if os.name == 'nt':  # Windows
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            return winreg.QueryValueEx(key, downloads_guid)[0]
    elif os.name == 'posix':  # macOS or Linux
        return os.path.join(os.path.expanduser('~'), 'Downloads')
    else:
        raise OSError("Unsupported operating system")


def main():
    # Get the path to the Downloads folder
    downloads_path = get_download_path()

    if not os.path.exists(downloads_path):
        print(f"Downloads folder not found: {downloads_path}")
        return

    # Get all files in the Downloads folder
    files = [f for f in os.listdir(downloads_path) if os.path.isfile(os.path.join(downloads_path, f))]

    for file in files:
        # Extract file name and extension
        name, extension = os.path.splitext(file)

        if not extension:  # Skip files without an extension
            continue

        # Create folder name based on file extension (without the dot)
        folder_name = extension[1:]

        # Path for the folder to move files into
        destination_folder = os.path.join(downloads_path, folder_name)

        try:
            # Create the folder if it doesn't exist
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
                print(f"Created folder: {folder_name}")

            # Move the file into the folder
            shutil.move(os.path.join(downloads_path, file), os.path.join(destination_folder, file))
            print(f"Moved file: {file} to {folder_name}/")
        except Exception as e:
            print(f"Error processing file {file}: {e}")


if __name__ == '__main__':
    main()
