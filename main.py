import os
import shutil
from glob import glob


def get_download_path():
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')


def main():
    downloads_path = get_download_path()
    files = [f for f in os.listdir(downloads_path)]
    folder_list = glob(downloads_path + "/*/")
    for f in files:
        print(f)
        name, extension = os.path.splitext(f)
        try:
            if extension[1:] in folder_list:
                shutil.move(downloads_path + "/" + f, downloads_path + "/" + extension[1:])
                print("Moved file {" + f + "} ")
            else:
                to_create_directory = downloads_path + "/" + extension[1:]
                os.makedirs(to_create_directory)
                print("Created Folder {" + extension[1:] + "} ")
                folder_list.append(extension[1:])
                shutil.move(downloads_path + "/" + f, downloads_path + "/" + extension[1:])
                print("Moved file {" + f + "} to " + extension[1:] + " folder")
        except:
            files.remove(f)


if __name__ == '__main__':
    main()
