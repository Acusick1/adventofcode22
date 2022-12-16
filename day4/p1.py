from pathlib import Path


if __name__ == "__main__":

    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.readlines()

    count = 0
    for line in lines:
        a, b = line.strip().split(",")

        a_min, a_max = map(int, a.split("-"))
        b_min, b_max = map(int, b.split("-"))

        if (a_min <= b_min and a_max >= b_max) or (b_min <= a_min and b_max >= a_max):
            count += 1

    print(count)