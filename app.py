import json

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

test_file = "test_td.json"
test_contents = get_json(test_file)
dump_json(test_contents, test_file)
