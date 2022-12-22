from pathlib import Path
import numpy as np


def main(matrix: np.array):

    def bfs(i, j, direction, val, curr=0):

        if direction == 0:
            i -= 1
        elif direction == 1:
            i += 1
        elif direction == 2:
            j -= 1
        elif direction == 3:
            j += 1

        curr += 1

        if 0 < i < rows - 1 and 0 < j < cols - 1 and val > matrix[i, j]:
            
            return bfs(i, j, direction, val, curr=curr)
        else:
            return curr

    rows, cols = matrix.shape
    best = -1
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            
            val = matrix[i, j]
            best = max(best, bfs(i, j, 0, val) * bfs(i, j, 1, val) * bfs(i, j, 2, val) * bfs(i, j, 3, val))

    print(best)


if __name__ == "__main__":

    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.readlines()

    matrix = np.array([[int(num) for num in line.strip()] for line in lines])
    main(matrix)
    