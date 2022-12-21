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


def get_candidates(root: Folder, size_threshold=100000):

    candidates = []
    stack = [root]
    while stack:

        curr = stack.pop(0)
        if curr.size <= size_threshold:
            candidates.append(curr)

        stack.extend(curr.children)

    return candidates


if __name__ == "__main__":

    with open(Path(__file__).parent / "input.txt") as f:
        lines = iter(f.readlines())

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
    candidates = get_candidates(root)

    print(sum([c.size for c in candidates]))
