import os
import random
from itertools import product

players = ["Jokic", "Murray", "Porter", "Booker", "Durant", "Ayton", "Points"]
decisions = ["O", "U"]


def test_generate_combos():
    combos = generate_combos(decisions, players)
    assert len(combos) == 2 ** len(players)


def test_save_output():
    output = "| Players | Decision |\n| ------- | -------- |\n"
    output_filepath = os.path.join("test", "test_output.md")
    save_output(output, output_filepath)
    assert os.path.exists(output_filepath)


def test_generate_and_save_output():
    combos = generate_combos(decisions, players)
    output = generate_output_table(combos, players)
    output_filepath = os.path.join("test", "test_generate_and_save_output.md")
    generate_and_save_output(output, output_filepath)
    assert os.path.exists(output_filepath)


def generate_combos(decisions, players):
    # Generate all possible combinations of decisions for each player
    combos = list(product(decisions, repeat=len(players)))
    return combos


def generate_output_table(combos, players):
    # Print header row
    output = "| Players | Decision |\n| ------- | -------- |\n"

    # Add each possible combination as a row in the table
    for combo in combos:
        rows = ["| {} | {} |\n".format(player, decision) for player, decision in zip(players, combo)]
        output += "".join(rows) + "| ------- | -------- |\n"
    return output


def generate_and_save_output(output, output_filepath):
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)

    # Save output to file
    save_output(output, output_filepath)

    # Print the count of possibilities
    print("Number of possibilities:", output.count("| O |") + output.count("| U |"))
    print("Output saved to {}".format(output_filepath))


def save_output(output, output_filepath):
    with open(output_filepath, "w") as f:
        f.write(output)


if __name__ == "__main__":
    # Get user input for whether to randomize output or not
    randomize_output = input("Do you want to randomize the output? (y/n): ").lower() == "y"

    # Generate all possible combinations of decisions for each player
    combos = generate_combos(decisions, players)

    # Optionally shuffle the combos list randomly
    if randomize_output:
        random.shuffle(combos)

    # Generate the output table
    output = generate_output_table(combos, players)

    # Get output file name from user
    output_filename = input("Enter the name of the output file (without .md extension): ")

    # Save output to file
    output_filepath = os.path.join("2023", output_filename + ".md")
    generate_and_save_output(output, output_filepath)
