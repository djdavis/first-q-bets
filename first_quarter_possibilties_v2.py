import os
from itertools import product

players = ["Tatum", "Brown", "Embiid", "Harden", "Maxey", "Points"]
decisions = ["O", "U"]

# Generate all possible combinations of decisions for each player
combos = list(product(decisions, repeat=len(players)))

# Organize combos by player
player_combos = {player: [] for player in players}
for combo in combos:
    for i, decision in enumerate(combo):
        player_combos[players[i]].append(decision)

# Print table for each player
for player in players:
    # Print header row
    output = "| {} | Decision |\n".format(player)
    output += "| - | - |\n"

    # Add each possible decision as a row in the table
    for decision in decisions:
        output += "| {} | {} |\n".format(player, decision)

    # Add a separator row between players
    output += "\n"

    print(output)

# Get output file name from user
output_filename = input("Enter the name of the output file (without .md extension): ")

# Create 2023 directory if it doesn't exist
if not os.path.exists("2023"):
    os.mkdir("2023")

# Save output to file in 2023 directory
output_filepath = os.path.join("2023", output_filename + ".md")
with open(output_filepath, "w") as f:
    # Write table for each player to file
    for player in players:
        output = "| {} | Decision |\n".format(player)
        output += "| - | - |\n"
        for decision in decisions:
            output += "| {} | {} |\n".format(player, decision)
        output += "\n"
        f.write(output)

    # Print count of possibilities
    f.write("Number of possibilities: {}".format(len(combos)))

print("Output saved to {}".format(output_filepath))
