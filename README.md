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

serena = get_player_matches("Serena Williams")   # also accepts "serena williams" or "SerenaWilliams"
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

**Hardest part.** The hardest part was actually getting set up, before I wrote any
package code. Cloning the course repo failed several times: `gh` wasn't installed on the
JupyterHub, I first typed the wrong GitHub username, and a "Write access not granted"
error turned out to be a token problem rather than a code problem. I got unstuck by
reading each error message carefully instead of just retrying. The second hard part was
finding the player's own birthdate. It isn't in the career JS file at all, so I had to
look at the player's page on tennisabstract.com, where it appears as `var dob = ...;`.

**Testing without a live server.** I learned that tests are more reliable when they work
on small, fixed inputs. The mock female and male JS snippets let me test the cleaning
functions in under a second with no internet. Having both mocks mattered because the two
file formats store opponent information differently (a birthdate for women, an age for
men), and one test for each format proved both code paths work. I kept all network code
in `fetch.py`, so everything in `clean.py` can be tested offline.

**Small functions.** Splitting the work into tiny functions (`_extract_matches`,
`_rows_to_frame`, `_opponent_age`, `_parse_birthdate`, `_build_career_frame`) made
each step easy to test and easy to debug. When something looked wrong, I knew which
single function to check. It also kept every function well under the 20-line limit
without any extra effort.

**The data.** I was surprised that the two files look so similar but differ in one
important column. I was also surprised that Rafael Nadal's career file stops in
October 2016 even though he kept playing until 2024, while Serena Williams's file runs
through her 2022 retirement. My package follows the assignment and uses the `Career.js`
files, but this showed me that a result can be correct for the data you loaded and still
not match the real-world story. Checking the date range before trusting the plot was
worth it.

**Git and small commits.** Committing after every function and every set of tests made
my progress easy to follow and easy to undo. I also learned that mistakes show up in the
history: one commit of mine had tests that imported a function I hadn't imported yet, and
I fixed it in the next commit instead of hiding it. Writing messages like "Add
_opponent_age for birthdate and direct-age formats" forced me to say what each step did.
