from pathlib import Path

if __name__ == "__main__":

    n_top = 3
    maxi = [0 for _ in range(n_top)]
    curr = 0

    with open(Path("day1") / "input.txt") as f:

        for line in f:

            line = line.strip()

            if line:
                curr += int(line)
            else:
                if curr > min(maxi):
                    maxi.remove(min(maxi))
                    maxi.append(curr)
                
                curr = 0

    print(sum(maxi))