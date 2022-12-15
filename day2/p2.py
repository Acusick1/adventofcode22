from pathlib import Path

shape_score = {"A": 1, "B": 2, "C": 3}
result_map = {"X": 0, "Y": 3, "Z": 6}
shape_keys = list(shape_score.keys())

if __name__ == "__main__":
    
    with open(Path(__file__).parent / "input.txt") as f:

        score = 0

        for line in f:
            opponent_key, outcome = line.split()

            opp_shape_id = shape_keys.index(opponent_key)

            if outcome == "X":
                player_key = shape_keys[opp_shape_id - 1]

            elif outcome == "Y":
                player_key = shape_keys[opp_shape_id]

            else:
                player_key = shape_keys[(opp_shape_id + 1) % 3] 


            score += result_map[outcome] + shape_score[player_key]

    print(score)