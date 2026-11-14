# Tennis Age Gap 🎾

### Exploring Age Differences in Professional Tennis

Tennis Age Gap is a Python package developed for UC Berkeley STAT 159 Homework 3. It retrieves career match records from [Tennis Abstract](https://www.tennisabstract.com/) and visualizes how a player's age compares to their opponents over time.

I chose Serena Williams and Rafael Nadal as my main examples to explore how age differences change throughout a professional tennis career. The package can also be used with other players available on Tennis Abstract.

---

## 1. Exploring the Results

Each point on the visualization represents a match. The horizontal axis shows the selected player's age, while the vertical axis represents the player's age minus their opponent's age.

- **Positive values:** The player was older than their opponent.
- **Negative values:** The player was younger than their opponent.
- **Zero:** Both players were approximately the same age.
- **Blue points:** Wins.
- **Orange points:** Losses.

### Serena Williams

![Serena Williams Age Gap](images/serena_example.png)

The Serena Williams dataset contains **1,038 matches**, dated October 30, 1995, through August 29, 2022.

The visualization shows how her age relative to her opponents changed across the available match records. These observations represent the records retrieved from Tennis Abstract, not an independently verified count of every professional match she played.

### Rafael Nadal

![Rafael Nadal Age Gap](images/rafa_example.png)

The Rafael Nadal dataset contains **1,096 matches**, dated September 10, 2001, through October 10, 2016.

Unlike Serena's dataset, Nadal's retrieved career file ends before his professional career ended. Therefore, the visualization only represents the portion of his career available from the source.

---

## 2. Quick Start

### Install the package

Run the following command in your terminal:

```bash
pip install git+https://github.com/UCB-stat159-f26/hw03-3-lisaliem7.git
```

The repository is private, so installation requires GitHub authentication and access to the repository. Authentication tokens should not be stored in scripts.

### Generate your first visualization

```python
from tennisage import get_player_matches, plot_age_gap

# Retrieve player records
serena = get_player_matches("Serena Williams")

# Preview the dataset
print(serena.head())

# Generate the plot
fig = plot_age_gap(serena)

# Save the figure
fig.savefig("serena_plot.png", dpi=150)
```

The package retrieves the available records, calculates the age differences, and returns a matplotlib figure.

---

## 3. Using the Python Functions

The package provides two main functions: `get_player_matches()` for retrieving match data and `plot_age_gap()` for creating visualizations.

### Retrieving career records

The `get_player_matches()` function accepts player names in multiple formats.

```python
from tennisage import get_player_matches

serena = get_player_matches("serena williams")
serena = get_player_matches("Serena Williams")
serena = get_player_matches("SerenaWilliams")

rafa = get_player_matches("Rafael Nadal")
```

If a player is not found, the function raises an informative error.

```python
get_player_matches("GastonSanchez")

# ValueError: No player found for 'GastonSanchez'. Check the spelling, e.g. 'Serena Williams'.
```

### What's inside the dataset?

The function returns a pandas DataFrame containing six columns:

| Column | What it represents |
|---|---|
| `date` | Match date recorded by Tennis Abstract |
| `opponent` | Opponent's name |
| `player_age` | Selected player's age in decimal years |
| `opp_age` | Opponent's age in decimal years |
| `age_diff` | Player age minus opponent age |
| `won` | True for a win and False for a loss |

Ages calculated from birth dates use elapsed days divided by 365.25. When an opponent's age is already provided as a number, the package uses that value directly.

Records without a usable opponent age are removed.

### Plotting age differences

Use `plot_age_gap()` with the DataFrame returned by `get_player_matches()`.

```python
from tennisage import plot_age_gap

fig = plot_age_gap(serena)
fig.savefig("my_plot.png", dpi=150)
```

The plotting function returns a matplotlib figure. It also checks whether the input DataFrame came from `get_player_matches()` and raises a `ValueError` if the input is invalid.

---

## 4. Understanding the Data

### How the package collects information

The package converts a player's name into the format used by Tennis Abstract. For example, `"serena williams"` becomes `"SerenaWilliams"`.

It then downloads the player's career file and extracts the available match records.

Because the career file does not include the player's own birth date, the package retrieves that information separately from the player's profile page.

The data is also stored differently depending on the player:

- Women's files provide opponents' birth dates.
- Men's files provide opponents' ages as numeric values.

The package handles both formats and converts the available information into comparable age measurements.

### Things to keep in mind

Tennis Abstract does not necessarily provide complete career records for every player.

For example, Serena Williams' retrieved records extend through 2022, while Rafael Nadal's file stops in October 2016.

The package does not independently verify whether all professional matches are included.

Some dates may also represent tournament dates rather than the exact dates matches were played, so calculated ages are approximate.

Additionally, future changes to Tennis Abstract's website or data structure may require updates to the retrieval functions.

---

## 5. Checking the Package

I used automated tests to verify that the package processes match records correctly and creates the expected visualizations.

### Running the tests

Install the testing dependencies from the repository root:

```bash
pip install -e ".[test]"
```

Then run:

```bash
pytest
```

### What the tests cover

The tests use small mock career files for a female and male player instead of contacting the live website.

They check:

- Parsing match records and selecting columns.
- Handling different opponent age formats.
- Reading player birth dates.
- Building the final pandas DataFrame.
- Converting player names.
- Checking plotting labels and validating inputs.

I checked the live data-download functions separately by running them against Tennis Abstract.

Using mock files allows the automated test suite to run in under a second without repeatedly downloading data.

---

## 6. What I Learned

One of my biggest takeaways from this project was learning that successfully downloading data does not mean the data is complete.

When I retrieved Rafael Nadal's records, I noticed that his career file stopped in 2016 even though he continued playing professionally for years afterward. This helped me understand why it is important to check the limitations of a dataset instead of assuming the source contains everything.

I also learned how useful it is to separate a larger programming task into smaller functions. Since men's and women's career files store opponent information differently, organizing each step into its own function made the code easier to test and troubleshoot.

Writing tests using mock files was another part of the project that helped me. Rather than contacting the website each time, I could test the functions using small examples and identify problems much faster.

The most challenging part for me was getting everything set up on GitHub. I initially had problems cloning the repository because `gh` was not installed, and my authentication token did not work. Learning to read the terminal error messages helped me figure out what was going wrong.

I also became more comfortable making smaller commits, pushing changes, and verifying that my updates appeared on GitHub.

Overall, this assignment helped me improve my understanding of Python packaging, automated testing, version control, and the importance of documenting data limitations.

---

## 7. Tools and Requirements

The package dependencies are listed in `pyproject.toml`.

| Package | Purpose |
|---|---|
| pandas | Organizing and processing match records |
| requests | Downloading data from Tennis Abstract |
| matplotlib | Creating age comparison plots |
| pytest | Running automated tests |

`pytest` is an optional testing dependency.

As specified in STAT 159 HW3, this project does not require a Makefile or an `environment.yml` file.

---

## 8. References and License

**Data:** [Tennis Abstract](https://www.tennisabstract.com/)

**Visualization inspiration:** [New York Times — Serena Williams Age Comparison](https://www.nytimes.com/interactive/2022/08/28/sports/tennis/serena-age-opponents.html)

The visualizations use the same general age-comparison idea introduced in HW2 without reproducing the original annotations.

The package code is released under the MIT License. This license does not grant rights to third-party data or graphics.
