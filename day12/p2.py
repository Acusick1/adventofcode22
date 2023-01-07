import numpy as np
import string
from pathlib import Path

all_letters = string.ascii_letters


def bfs(start_ij: tuple[int, int], grid):

    steps = 0
    stack = [start_ij]
    visited = set()

    while stack:

        children = set()
        steps += 1

        for node in stack:
            visited.add(node)

            for direction in range(4):

                ii, jj = node

                if direction == 0:
                    ii += 1
                elif direction == 1:
                    ii -= 1
                elif direction == 2:
                    jj += 1
                elif direction == 3:
                    jj -= 1

                if 0 <= ii < grid.shape[0] and 0 <= jj < grid.shape[1]:

                    if grid[ii, jj] == grid.min():
                        return steps

                    elif grid[node] - grid[ii, jj] <= 1 and (ii, jj) not in visited:
                        children.add((ii, jj))

        stack = children


if __name__ == "__main__":

    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.readlines()

    elevation_map = np.array([[all_letters.index(letter)
                             for letter in line.strip()] for line in lines])

    old_start = np.unravel_index(elevation_map.argmax(), elevation_map.shape)
    elevation_map[old_start] = 0

    finish = np.unravel_index(elevation_map.argmax(), elevation_map.shape)
    elevation_map[finish] = 26
    n_steps = bfs(start_ij=finish, grid=elevation_map)

    print(n_steps)
