from pathlib import Path


class Folder(object):
    def __init__(self, name, size=0, parent=None):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []


def sum_tree(folder: Folder):

    for child in folder.children:
        child = sum_tree(child)
        folder.size += child.size

    return folder


def get_closest_above(root: Folder, size_threshold):

    stack = [root]
    best = None
    best_diff = None
    while stack:

        curr = stack.pop(0)
        diff = curr.size - size_threshold

        if best is None or 0 <= diff < best_diff:
            best = curr
            best_diff = diff

        stack.extend(curr.children)

    return best


if __name__ == "__main__":

    space = 70000000
    needed = 30000000

    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.readlines()

    root = Folder("/")
    folder = root
    parent = None
    for line in lines:

        if "$ cd" in line:

            _, left, right = line.strip().split()

            if ".." in right:
                folder = folder.parent
            else:
                parent = folder

                for child in folder.children:
                    if child.name == right:
                        folder = child
                        break

        elif "$ ls" in line:
            continue

        else:
            left, right = line.strip().split()

            if "dir" in left:
                folder.children.append(Folder(name=right, parent=folder))
            else:
                folder.size += int(left)

    root = sum_tree(root)
    unused = space - root.size

    closest = get_closest_above(root, size_threshold=needed - unused)

    print(closest.size)
