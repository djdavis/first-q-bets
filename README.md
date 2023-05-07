# All Possible Combinations of Player O/Us

This Python script generates all possible combinations of over/under decisions for a given set of players. The output is saved to a Markdown file, which can be viewed in a text editor or rendered as a table in a Markdown viewer.

## Usage

1. Download the `first_quarter_possibilities.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory where the `first_quarter_possibilities.py` file is located.
4. Run the script using the command `python first_quarter_possibilities.py`.
5. Follow the prompts to enter the name of the output file and whether to randomize the output.

## Explanation

The `first_quarter_possibilities.py` script uses the `product` function from the `itertools` module to generate all possible combinations of player decisions. The script prompts the user to enter the name of the output file, which is saved as a Markdown file in a subdirectory called `2023`. The output file contains a table of all possible combinations of player decisions, with each row corresponding to a unique combination.

The script also allows the user to choose whether to randomize the output. If randomization is enabled, the script shuffles the list of combinations randomly before saving the output to the Markdown file.

## Dependencies

The script requires Python 3.x and the `itertools` and `random` modules, which are included in the standard library.

## License

This script is released under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and use it for your own purposes!