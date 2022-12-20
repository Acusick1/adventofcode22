from pathlib import Path

packet_size = 4


if __name__ == "__main__":
        
    with open(Path(__file__).parent / "input.txt") as f:
        line = f.readline()

    for i, _ in enumerate(line):

        if len(set(line[i:i + packet_size])) == packet_size:
            break

    print(i + packet_size)