import os
import random
import datetime
from itertools import product

players = ["Harden","Embiid", "Smart",
           "Brown", "Maxey", "Points"]
decisions = ["O", "U"]
current_year = str(datetime.date.today().year)


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
if not os.path.exists(current_year):
    os.mkdir(current_year)

# Save output to file in 2023 directory
output_filepath = os.path.join(current_year, output_filename + ".md")
with open(output_filepath, "w") as f:
    f.write(output)

# Print the count of possibilities
print("Number of possibilities:", len(combos))
print("Output saved to {}".format(output_filepath))
