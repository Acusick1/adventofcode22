from pathlib import Path
import numpy as np


if __name__ == "__main__":

    n_knots = 10

    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.readlines()

    knots = np.zeros((n_knots, 2))

    tail_visited = set()
    tail_visited.add(tuple(knots[-1,:]))

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

            knots[0,:] += velocity

            for i in range(1, n_knots):
                xdiff, ydiff = knots[i-1,:] - knots[i,:]

                if abs(xdiff) + abs(ydiff) > 2:

                    knots[i,:] += np.sign([xdiff, ydiff])

                elif abs(xdiff) > 1:
                    knots[i, 0] += np.sign(xdiff)

                elif abs(ydiff) > 1:
                    knots[i, 1] += np.sign(ydiff)
                else:
                    break

            tail_visited.add(tuple(knots[-1,:]))
            print(knots[0,:], knots[-1,:])

    print(len(tail_visited))
