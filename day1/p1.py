from pathlib import Path

if __name__ == "__main__":

    maxi, curr = 0, 0

    with open(Path("day1") / "input.txt") as f:

        for line in f:
            if line:
                curr += int(line.strip())
            else:
                maxi = max(maxi, curr)
                curr = 0
        
    print(maxi)