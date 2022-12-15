import string
from pathlib import Path

letters = string.ascii_lowercase + string.ascii_uppercase

priority_map = {letter: num + 1 for num, letter in enumerate(letters)}


if __name__ == "__main__":

    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.readlines()

    val = 0
    for start_id in range(0, len(lines), 3):
        
        items = []
        for id in range(start_id, start_id + 3):
            
            items.append(lines[id].strip())

        common = set(items[0]).intersection(*items[1:])
        val += priority_map[common.pop()]

    print(val)
