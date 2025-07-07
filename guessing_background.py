from json_background import get_json
import random
def setup(file_contents):
    content = {"correct":0,
               "incorrect":0,
               "fc":file_contents}
    return content

def get_rd(cont):
    ter, defi = random.choice(list(cont["fc"].items()))
    return ter, defi

monkey = get_json("test_td")
info = setup(monkey)

def temp_set():
    term, definition = get_rd(info)
    meh = input(f"Guess for {term}: ")
    if meh == definition:
        print("Correct")
    else:
        print(f"Incorrect, {definition}")
