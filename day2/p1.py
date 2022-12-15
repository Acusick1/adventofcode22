from pathlib import Path

opponent_map = {"A": 1, "B": 2, "C": 3}
player_map = {"X": 1, "Y": 2, "Z": 3}

if __name__ == "__main__":
    
    with open(Path(__file__).parent / "input.txt") as f:

        score = 0

        for line in f:
            opponent_key, player_key = line.split()
            player_val = player_map[player_key]
            opponent_val = opponent_map[opponent_key]

            score += player_map[player_key]

            if player_val == opponent_val:
                score += 3

            elif player_val - opponent_val in [1, -2]:
                score += 6

    print(score)