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
