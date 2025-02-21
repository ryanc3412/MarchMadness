import random

def rand_bracket():
    sections = ["SOUTH", "MIDWEST", "EAST", "WEST"]
    seeds = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]

    rounds = {
        "First Round": [seeds.copy() for _ in range(4)],
        "Second Round": [[0] * 8 for _ in range(4)],
        "Sweet Sixteen": [[0] * 4 for _ in range(4)],
        "Elite Eight": [[0] * 2 for _ in range(4)],
        "Final Four": [0] * 4
    }
    
    champion_round = {"Championship": [0] * 2, "Winner": [0]}

    for i, region in enumerate(sections):
        print(f"\n\n**{region} Bracket**")
        simulate_round(rounds["First Round"][i], rounds["Second Round"][i], "First Round")
        simulate_round(rounds["Second Round"][i], rounds["Sweet Sixteen"][i], "Second Round")
        simulate_round(rounds["Sweet Sixteen"][i], rounds["Elite Eight"][i], "Sweet Sixteen")
        simulate_round(rounds["Elite Eight"][i], rounds["Final Four"], "Elite Eight", i)

    print("\n**Final Four**")
    simulate_round(rounds["Final Four"], champion_round["Championship"], "Final Four")

    print("\n**Championship**")
    simulate_round(champion_round["Championship"], champion_round["Winner"], "Championship")

    print(f"\n**Champion: {champion_round['Winner'][0]}**")


def simulate_round(current, next_round, round_name, index=None):
    """Simulates a single round and determines winners."""
    print(f"\n{round_name}")
    winners = []
    for i in range(0, len(current), 2):
        winner = random.choice([current[i], current[i + 1]])
        winners.append(winner)
        print(f"{current[i]} vs {current[i+1]} -> Winner: {winner}")
    
    if index is not None:
        next_round[index] = winners[0]  # Special case for final four
    else:
        next_round[:] = winners
        