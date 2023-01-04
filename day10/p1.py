from pathlib import Path


if __name__ == "__main__":

    save = list(range(20, 221, 40))

    with open(Path(__file__).parent / "input.txt") as f:
        lines = iter(f.readlines())

    stack = []
    save_sum = 0
    x = 1
    for i in range(1, max(save) + 1):

        if not stack:
            line = next(lines)

            stack.append(None)

            if "noop" not in line:
                
                stack.append(int(line.strip().split()[1]))
        
        if i in save:
            save_sum += i * x

        val = stack.pop(0) if stack else None

        if val is not None:
            x += val

    print(save_sum)
    print(i)