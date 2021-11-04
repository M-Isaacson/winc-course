import os
from shutil import rmtree
from zipfile import ZipFile, is_zipfile

__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


def main():
    clean_cache()
    cache_zip("code/files/data.zip", "code/files/cache")
    files = cached_files()
    print(files)
    print(find_password(files))


def clean_cache():
    """
    Creates an empty folder called cache or
    when it exists will delete its contents.
    """
    # Setting the path to work with.
    cache_path = f"{os.path.dirname(__file__)}/cache"
    # Make sure the base_path does really exists and is a directory.
    if os.path.exists(cache_path) and os.path.isdir(cache_path):
        # Clear the directory 'cache'.
        with os.scandir(cache_path) as path_content:
            for item in path_content:
                if item.is_file:
                    os.remove(item)
                else:
                    # rmtree is used to avoid error if dir or subdir is not empty.
                    user_cmd = input(f"{item} already exists, remove?:")
                    if user_cmd == "y":
                        rmtree(item)
    else:
        # Create the directory 'cache'.
        os.makedirs(cache_path)


def cache_zip(zip_path: str, cache_path: str):
    """
    Unzip a zip file in the 'cache' folder

    Parameters
    ----------
    zip_path : str
        Path of the zip (including filename)
    cache_path : str
        Path of the directory (folder)
    """
    # Be sure to have a clean 'cache' folder.
    clean_cache()
    # Check if zip file is indeed a zip file. If True unzip otherwise return error message.
    if is_zipfile(zip_path):
        with ZipFile(zip_path, "r") as zip_file:
            zip_file.extractall(cache_path)
    else:
        return None


def cached_files() -> list:
    """
    Returns a list of files in the 'cache' folder.
    """
    file_list = []
    # Setting the path to work with.
    cache_path = f"{os.path.dirname(__file__)}/cache"
    # Iterating the 'cache' folder
    with os.scandir(cache_path) as path_content:
        for item in path_content:
            if item.is_file:
                file_list.append(item.path)
    return file_list


def find_password(file_list: list) -> str:
    """
    Find a password in a bunch of files.

    Parameters
    ----------
    file_list : list
        List of files where a password might be in.

    Returns
    -------
    str
        The password or an error message.
    """
    for file in file_list:
        with open(file, "r") as txt_file:
            for line in txt_file:
                if "password" in line:
                    raw_message = line.split(":")
                    message = raw_message[1].strip()
                    return message
    return None


# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    main()
