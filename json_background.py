import json
import os


def dump_json(contents: dict, filename: str):
    """Dumps the current terms and definitions into a file

    Args:
        contents: dict, contains the current terms and definitions.
        filename: str, contains the name of the file the terms and
                       definitions will be placed into.

    """
    print(filename)
    with open(get_filepath(f"json_files/{filename}"), "w+", encoding="utf-8") as file:
        json.dump(contents, file)
        print(f"You did it, {filename} has been updated succesfully!")


def get_json(filename: str) -> dict:
    """Gets the terms and definitions from a file.

    Args:
        filename: str, contains the name of the file the terms and
                       definitions will be placed into.

    Returns:
        dict, contains the current terms and definitions.
    """
    with open(get_filepath(f"json_files/{filename}"), "r", encoding="utf-8") as file:
        contents = json.load(file)
        print(f"You did it, successfully loaded {filename}!")
    return contents


def get_json_files() -> list:
    """Gets the filenames of the files containing terms and definitions.

    Returns:
        list, contains filenames.
    """
    filenames = []
    for filename in os.listdir("./json_files"):
        if filename.endswith(".json"):
            filenames.append(filename.replace(".json", ""))
            #print(f"File {filename} found.")
    return filenames

def get_filepath(filename: str) -> str:
    base_path = os.path.abspath(
        os.path.dirname(__file__))  # This gets the dir of app.py
    full_path = os.path.join(base_path, f"{filename}.json")
    return full_path

def create_json(filename: str):
    contents = {}
    dump_json(contents, filename)

def delete_json(filename: str):
    print(get_filepath(f"json_files\\{filename}"))
    print(get_json_files())
    if filename in get_json_files():
        os.remove(get_filepath(f"json_files\\{filename}"))