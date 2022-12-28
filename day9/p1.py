from pathlib import Path
import numpy as np


if __name__ == "__main__":

    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.readlines()

    head = np.array([0, 0])
    tail = np.array([0, 0])

    tail_visited = set()
    tail_visited.add(tuple(tail))
    count = 0
    for line in lines:

        direction, distance = line.strip().split()

        if "U" in direction:
            velocity = np.array([1, 0])

        elif "D" in direction:
            velocity = np.array([-1, 0])

        elif "L" in direction:
            velocity = np.array([0, -1])

        elif "R" in direction:
            velocity = np.array([0, 1])

        for _ in range(int(distance)):

            head += velocity

            xdiff, ydiff = head - tail

            if abs(xdiff) + abs(ydiff) > 2:

                tail += np.sign([xdiff, ydiff])

            elif abs(xdiff) > 1:
                tail[0] += np.sign(xdiff)

            elif abs(ydiff) > 1:
                tail[1] += np.sign(ydiff)

            tail_visited.add(tuple(tail))
            print(head, tail)

    print(len(tail_visited))
