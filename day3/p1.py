import string
from pathlib import Path

letters = string.ascii_lowercase + string.ascii_uppercase

priority_map = {letter: num + 1 for num, letter in enumerate(letters)}


if __name__ == "__main__":

    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.readlines()

    val = 0
    for line in lines:

        mid = len(line) // 2
        left, right = line[:mid], line[mid:]

        common = set(left).intersection(right)
        val += priority_map[common.pop()]

    print(val)