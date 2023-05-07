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

# Print count of possible variations
print("Total possible variations: {}".format(total_combos))

# Save output to file
with open("possible_variations.md", "w") as f:
    f.write(output)

print("Output saved to possible_variations.md")
