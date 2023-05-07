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

# Add header row to the table
output = "<table style='border-collapse: collapse;'>\n<tr style='background-color: #f2f2f2;'><th>Selection</th><th>Players</th><th>Decision</th></tr>\n"

# Add each possible combination as a row in the table
for i, combo in enumerate(combos):
    rows = ["<td><input type='checkbox' name='selection' value='{0}'></td>".format(i + 1)]
    rows += ["<td>{0}</td><td>{1}</td>".format(player, decision) for player, decision in zip(players, combo)]
    output += "<tr style='border: 1px solid black;'>{0}</tr>\n".format("".join(rows))

    # Add separator every 10 rows
    if i % 10 == 9:
        output += "<tr style='border: none; height: 10px;'></tr>\n"

# Close the table
output += "</table>"

# Get output file name from user
output_filename = input("Enter the name of the output file (without .html extension): ")

# Create 2023 directory if it doesn't exist
if not os.path.exists("2023"):
    os.mkdir("2023")

# Save output to file in 2023 directory
output_filepath = os.path.join("2023", output_filename + ".html")
with open(output_filepath, "w") as f:
    f.write(output)

# Print the count of possibilities
print("Number of possibilities:", len(combos))
print("Output saved to {}".format(output_filepath))
