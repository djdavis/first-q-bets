import os
import random
from itertools import product

players = ["Jokic", "Murray", "Porter", "Booker", "Durant", "Ayton", "Points"]
decisions = ["O", "U"]

# Get user input for whether to randomize output or not
while True:
    randomize_output = input("Do you want to randomize the output? (y/n): ").lower()
    if randomize_output == "y" or randomize_output == "n":
        break

randomize_output = randomize_output == "y"

# Get user input for whether to output HTML table or not
while True:
    output_html = input("Do you want to output an HTML table? (y/n): ").lower()
    if output_html == "y" or output_html == "n":
        break

output_html = output_html == "y"

# Generate all possible combinations of decisions for each player
combos = list(product(decisions, repeat=len(players)))

# Optionally shuffle the combos list randomly
if randomize_output:
    random.shuffle(combos)

total_combos = len(combos)

# Initialize the output string
if output_html:
    output = "<table>\n<tr><th>Players</th><th>Decision</th></tr>\n"
else:
    output = "| Players | Decision |\n| ------- | -------- |\n"

# Add each possible combination as a row in the table
for combo in combos:
    if output_html:
        rows = ["<tr><td>{}</td><td>{}</td></tr>\n".format(player, decision) for player, decision in zip(players, combo)]
        output += "".join(rows)
    else:
        rows = ["| {} | {} |\n".format(player, decision) for player, decision in zip(players, combo)]
        output += "".join(rows) + "| ------- | -------- |\n"

# Get output file name from user
output_filename = input("Enter the name of the output file (without extension): ")

# Create 2023 directory if it doesn't exist
if not os.path.exists("2023"):
    os.mkdir("2023")

# Save output to file in 2023 directory
if output_html:
    output_filepath = os.path.join("2023", output_filename + ".html")
else:
    output_filepath = os.path.join("2023", output_filename + ".md")

with open(output_filepath, "w") as f:
    f.write(output)

# Print the count of possibilities
print("Number of possibilities:", len(combos))
print("Output saved to {}".format(output_filepath))
