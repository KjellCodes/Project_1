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
    with open(f"./json_files/{filename}", "w+", encoding="utf-8") as file:
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
    with open(f"./json_files/{filename}", "r", encoding="utf-8") as file:
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
            print(f"File {filename} found.")
    return filenames

"""for i in range(3,10):
    temp_fn = f"test_td{i}.json"
    td_1 = i * 2 - 1
    td_2 = i * 2
    temp_dict = {f"Term_{td_1}": f"Def_{td_1}",
                 f"Term_{td_2}": f"Def_{td_2}",}
    print(temp_dict)
    dump_json(temp_dict, temp_fn)"""