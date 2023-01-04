from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


image = np.zeros((6, 40))

if __name__ == "__main__":

    with open(Path(__file__).parent / "input.txt") as f:
        lines = iter(f.readlines())

    stack = []
    x = 1
    for row in range(image.shape[0]):
        for col in range(image.shape[1]):

            if not stack:
                line = next(lines)

                stack.append(None)

                if "noop" not in line:

                    stack.append(int(line.strip().split()[1]))

            if x-1 <= col <= x+1:
                image[row, col] = 1

            val = stack.pop(0) if stack else None

            if val is not None:
                x += val

    plt.imshow(image)
    plt.show()
