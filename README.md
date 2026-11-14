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
