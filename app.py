import json
import os

def dump_json(contents: dict, filename: str):
    """Dumps the current terms and definitions into a file

    Args:
        contents: dict, contains the current terms and definitions.
        filename: str, contains the name of the file the terms and
                       definitions will be placed into.
    
    """
    if not filename.endswith(".json"):
        pass
    with open(filename, "w", encoding="utf-8") as file:
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
    if not filename.endswith(".json"):
        pass
    with open(filename, "r", encoding="utf-8") as file:
        contents = json.load(file)
        print(f"You did it, successfully loaded {filename}!")
    return contents

def get_json_files() -> list:
    """Gets the filenames of the files containing terms and definitions.

    Returns:
        list, contains filenames.
    """
    filenames = []
    for filename in os.listdir("."):
        if filename.endswith(".json"):
            filenames.append(filename)
            print(f"File {filename} found.")
    return filenames

def temp_select_file(file_list: list) -> str:
    """Temporary way of selecting which file to use.

    Args:
        file_list: list, contains filenames.

    Returns:
        str, contains the name of the selected file.
    """
    for count, filename in enumerate(file_list):
        print(f"{count}: {filename}")
    print("Please select a file using the number")
    chosen_number = int(input(""))
    if not file_list[chosen_number]:
        pass
    print(f"You selected {file_list[chosen_number]}")
    return file_list[chosen_number]

test_files = get_json_files()
test_file = temp_select_file(test_files)
test_contents = get_json(test_file)
dump_json(test_contents, test_file)
