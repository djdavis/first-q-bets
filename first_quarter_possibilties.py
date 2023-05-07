import os
from itertools import product

players = ["Tatum", "Brown", "Embiid", "Harden", "Maxey", "Points"]
decisions = ["O", "U"]

# Generate all possible combinations of decisions for each player
combos = list(product(decisions, repeat=len(players)))
total_combos = len(combos)

# Print header row
output = "| Players | Decision |\n| ------- | -------- |\n"

# Add each possible combination as a row in the table
for combo in combos:
    rows = ["| {} | {} |\n".format(player, decision) for player, decision in zip(players, combo)]
    output += "".join(rows) + "| ------- | -------- |\n"

# Get output file name from user
output_filename = input("Enter the name of the output file (without .md extension): ")

# Create 2023 directory if it doesn't exist
if not os.path.exists("2023"):
    os.mkdir("2023")

# Save output to file in 2023 directory
output_filepath = os.path.join("2023", output_filename + ".md")
with open(output_filepath, "w") as f:
    f.write(output)

print("Output saved to {}".format(output_filepath))
