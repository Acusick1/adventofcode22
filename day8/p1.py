from pathlib import Path
import numpy as np


def main(matrix: np.array):

    rows, cols = matrix.shape
    count = (2 * (rows + cols)) - 4
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            
            if matrix[i, j] > np.array([matrix[:i, j].max(), matrix[i+1:, j].max(), matrix[i, :j].max(), matrix[i, j+1:].max()]).min():
                count += 1

    print(count)


if __name__ == "__main__":

    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.readlines()

    matrix = np.array([[int(num) for num in line.strip()] for line in lines])
    main(matrix)
    