import re
from pathlib import Path


def get_stacks(start=1, step=4, n_stacks=9):

    stacks = [[] for _ in range(n_stacks)] 

    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.readlines()

    for line in lines:

        line = line.strip()

        if line:

            for i, j in enumerate(range(start, len(line), step)):
                
                if line[j] != " ":
                    stacks[i].append(line[j])
        else:
            break        
            
    stacks = [list(reversed(stack)) for stack in stacks]
    return stacks


if __name__ == "__main__":

    stacks = get_stacks()
        
    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.readlines()

    for line in lines:
        
        if line.startswith("move"):
            
            nums = list(map(int, re.findall(r"(\d+)", line)))
            
            moving = [stacks[nums[1] - 1].pop(-i) for i in range(nums[0], 0, -1)]
            stacks[nums[2] - 1].extend(moving)

    print("".join([stack[-1] for stack in stacks]))