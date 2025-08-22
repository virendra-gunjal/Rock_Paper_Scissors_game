import random

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    # First move
    if prev_play == "":
        return "R"

    # Helper to beat a move
    def beat(move):
        return {"R": "P", "P": "S", "S": "R"}[move]

    # --- Strategy against Quincy ---
    quincy_pattern = ["R", "P", "P", "S", "R"]
    if len(opponent_history) >= 5 and opponent_history[-5:] == quincy_pattern:
        # We detected quincy
        next_idx = len(opponent_history) % len(quincy_pattern)
        return beat(quincy_pattern[next_idx])

    # --- Strategy against Kris ---
    # Kris copies your last move, so beat what you just played
    if len(opponent_history) >= 2 and opponent_history[-1] == opponent_history[-2]:
        return beat(opponent_history[-1])

    # --- Strategy against Mrugesh (frequency-based) ---
    if len(opponent_history) > 10:
        counts = {m: opponent_history.count(m) for m in ["R", "P", "S"]}
        likely = max(counts, key=counts.get)  # Most frequent move
        return beat(likely)

    # --- Default strategy (works vs Abbey) ---
    return random.choice(["R", "P", "S"])
