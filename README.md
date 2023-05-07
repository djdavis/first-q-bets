# All Possible Combinations of Player O/Us

This Python script generates all possible combinations of over/under decisions for a given set of players. The output is saved to a Markdown file, which can be viewed in a text editor or rendered as a table in a Markdown viewer.

Gambling is fun, but not encouraged. Use at your own risk. 

U - under
O - over

You can use this script to know what all of the possible parlay combinations are, given your input.

# Example Input/Output

### Line 5:
`players = ["Jokic", "Murray", "Porter", "Booker", "Durant", "Ayton", "Points"]`

### Output:

| Players | Decision |
|-----| -------- |
| Jokic | U |
| Murray | O |
| Porter | U |
| Booker | U |
| Durant | U |
| Ayton | U |
| Points | O |
| ------- | -------- |
| Jokic | U |
| Murray | U |
| Porter | U |
| Booker | O |
| Durant | O |
| Ayton | O |
| Points | O |
... and so on

## Usage

1. Download the `first_quarter_possibilities.py` file.
2. Modify the list of "players" on line 5. "Points" is in this list because I also bet the over/under on 1st quarter points.
3. Open a terminal or command prompt.
4. Navigate to the directory where the `first_quarter_possibilities.py` file is located.
5. Run the script using the command `python first_quarter_possibilities.py`.
6. Follow the prompts to enter the name of the output file and whether to randomize the output.

## Explanation

The `first_quarter_possibilities.py` script uses the `product` function from the `itertools` module to generate all possible combinations of player decisions. The script prompts the user to enter the name of the output file, which is saved as a Markdown file in a subdirectory called `2023`. The output file contains a table of all possible combinations of player decisions, with each row corresponding to a unique combination.

The script also allows the user to choose whether to randomize the output. If randomization is enabled, the script shuffles the list of combinations randomly before saving the output to the Markdown file.

## Dependencies

The script requires Python 3.x and the `itertools` and `random` modules, which are included in the standard library.

## License

This script is released under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and use it for your own purposes!