# tennisage

Get a tennis player's career matches from [tennisabstract.com](https://www.tennisabstract.com)
and plot the age gap between the player and each opponent, colored by win or loss.

## Install

```bash
pip install git+https://github.com/UCB-stat159-f26/hw03-3-lisaliem7.git
```

## Usage

```python
from tennisage import get_player_matches, plot_age_gap

serena = get_player_matches("Serena Williams")   # accepts "serena williams" or "SerenaWilliams"
fig = plot_age_gap(serena)

rafa = get_player_matches("Rafael Nadal")
plot_age_gap(rafa)

get_player_matches("GastonSanchez")   # raises ValueError: No player found ...
```

## Functions

- `get_player_matches(player_name)`: returns a DataFrame with columns
  `date`, `opponent`, `player_age`, `opp_age`, `age_diff`, `won`.
- `plot_age_gap(df)`: scatter plot of `player_age` (x) vs. `age_diff` (y), colored by result.

## Running the tests

```bash
pip install -e ".[test]"
pytest
```

The tests use mock career data and never contact the live website.

## Personal Reflections

**Hardest part.** The hardest part was getting set up before I wrote any package code. Cloning the course repository failed several times because `gh` was not installed on the JupyterHub, because I typed the wrong GitHub username at first, and because a "Write access not granted" error turned out to be a token problem rather than a code problem. I got unstuck by reading each error message carefully instead of retrying the same command. The second hard part was finding the player's own birthdate. The birthdate is not in the career JS file, so I had to inspect the player's page on tennisabstract.com, where it appears as `var dob = ...;`.

**Testing without a live server.** I learned that tests are more reliable when they run on small, fixed inputs. The mock female and male JS snippets let me test the cleaning functions in under a second without an internet connection. Both mocks mattered because the two file formats store opponent information differently, with a birthdate for women and an age for men. One test for each format proved that both code paths work. I kept all of the network code in `fetch.py`, so everything in `clean.py` can be tested offline.

**Small functions.** Splitting the work into small functions (`_extract_matches`, `_rows_to_frame`, `_opponent_age`, `_parse_birthdate`, and `_build_career_frame`) made each step easy to test and easy to debug. When something looked wrong, I knew exactly which function to check. Small functions kept every function well under the 20-line limit without any extra effort.

**The data.** I was surprised that the two file formats look so similar but differ in one important column. Rafael Nadal's career file stops in October 2016, even though he kept playing until 2024, while Serena Williams's file runs through her retirement in 2022, and that gap surprised me even more. My package follows the assignment and uses the `Career.js` files, but this taught me that a result can be correct for the data I loaded and still not match the real-world story. Checking the date range before trusting the plot was worth the extra minute.

**Git and small commits.** Committing after every function and every set of tests made my progress easy to follow and easy to undo. I learned that mistakes stay visible in the history. One of my commits contained tests that used a function I had not imported yet, and I fixed it in the next commit instead of hiding it. Writing messages such as "Add _opponent_age for birthdate and direct-age formats" forced me to say clearly what each step did.
