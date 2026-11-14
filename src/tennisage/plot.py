"""Make the NYT-style age-gap scatter plot."""
import matplotlib.pyplot as plt

REQUIRED_COLUMNS = ["player_age", "age_diff", "won"]
WIN_COLOR, LOSS_COLOR = "#1f77b4", "#d95f02"


def _check_columns(df):
    """Raise a clear error if the DataFrame didn't come from get_player_matches."""
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(
            f"DataFrame is missing columns {missing}. Build it with get_player_matches()."
        )


def _scatter_by_result(ax, df):
    """Draw wins and losses as differently colored points."""
    for won, color, label in [(True, WIN_COLOR, "Win"), (False, LOSS_COLOR, "Loss")]:
        subset = df[df["won"] == won]
        ax.scatter(subset["player_age"], subset["age_diff"],
                   c=color, label=label, alpha=0.7, s=25)


def _style_axes(ax):
    """Add the zero line, axis labels and legend."""
    ax.axhline(0, color="gray", linewidth=0.8)
    ax.set_xlabel("Player's age")
    ax.set_ylabel("Player's age minus opponent's age (years)")
    ax.legend(title="Result")


def plot_age_gap(df):
    """Scatter plot of player age vs. age gap, colored by win/loss.

    Example: plot_age_gap(get_player_matches("Serena Williams"))
    """
    _check_columns(df)
    fig, ax = plt.subplots(figsize=(9, 6))
    _scatter_by_result(ax, df)
    _style_axes(ax)
    return fig
