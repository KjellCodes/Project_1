import json

def dump_json(contents: dict, filename: str):
    """ Dumps the current terms and definitions into a file

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

test_contents = {"Term1": "Def1",
                 "Term2": "Def2"}
test_file = "test_td.json"
dump_json(test_contents, test_file)