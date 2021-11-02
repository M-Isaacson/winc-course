import os
from shutil import rmtree
from zipfile import ZipFile, is_zipfile

__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


def main() -> None:

    clean_cache()
    cache_zip("code/files/data.zip", "code/files/cache")
    files = cached_files()
    print(find_password(files))


def clean_cache() -> None:
    """
    Creates an empty folder called cache or
    when it exists will delete its contents.
    """
    # Setting the path to work with.

    base_path = f"{os.getcwd()}/code/files/cache"
    # Make sure the base_path does really exists and is a directory.
    if os.path.exists(base_path) and os.path.isdir(base_path):
        # Clear the directory 'cache'.
        with os.scandir(base_path) as path_content:
            for item in path_content:
                if item.is_file:
                    os.remove(item)
                else:
                    # rmtree is used to avoid error if dir or subdir is not empty.
                    rmtree(item)
    else:
        # Create the directory 'cache'.
        print(base_path)
        os.mkdir(base_path)


def cache_zip(zip_path: str, cache_path: str) -> None or str:
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
        return f"'{zip_path}' is not a valid zip file!"


def cached_files() -> list:
    """
    Returns a list of files in the 'cache' folder.
    """
    file_list = []
    # Setting the path to work with.
    base_path = f"{os.getcwd()}/code/files/cache"
    # Iterating the 'cache' folder
    with os.scandir(base_path) as path_content:
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
    message = "No password found"
    stop_search = False
    for file in file_list:
        if stop_search == False:
            with open(file, "r") as txt_file:
                for line in txt_file:
                    if "password" in line:
                        raw_message = line.split(":")
                        message = raw_message[1].strip()
                        stop_search = True
                        break
        else:
            break
    return message


# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    main()
