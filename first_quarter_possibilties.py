import os
import random
from itertools import product

players = ["Jokic", "Murray", "Porter", "Booker", "Durant", "Ayton", "Points"]
decisions = ["O", "U"]

# Get user input for whether to randomize output or not
randomize_output = input("Do you want to randomize the output? (y/n): ").lower() == "y"

# Generate all possible combinations of decisions for each player
combos = list(product(decisions, repeat=len(players)))

# Optionally shuffle the combos list randomly
if randomize_output:
    random.shuffle(combos)

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

# Print the count of possibilities
print("Number of possibilities:", len(combos))
print("Output saved to {}".format(output_filepath))
