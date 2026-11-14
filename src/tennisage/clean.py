"""Private helpers that turn a tennisabstract career JS string into a clean DataFrame."""
import json
import re

import pandas as pd

DATE_COL, RESULT_COL, OPPONENT_COL, OPP_AGE_OR_DOB_COL = 0, 4, 11, 16


def _extract_matches(js_text):
    """Return the list of match rows stored in 'var morematchmx = [[...]];'."""
    marker = re.search(r"morematchmx\s*=\s*", js_text)
    if marker is None:
        raise ValueError("Could not find match data in the JS file.")
    rows, _ = json.JSONDecoder().raw_decode(js_text[marker.end():])
    return rows


def _rows_to_frame(rows):
    """Keep only the columns we need and give them readable names."""
    keep = [DATE_COL, RESULT_COL, OPPONENT_COL, OPP_AGE_OR_DOB_COL]
    df = pd.DataFrame(rows).iloc[:, keep]
    df.columns = ["date", "result", "opponent", "opp_age_or_dob"]
    return df


def _opponent_age(df):
    """Opponent age in years: from birthdate (women) or used directly (men)."""
    raw = df["opp_age_or_dob"]
    is_dob = raw.str.fullmatch(r"\d{8}")
    dob = pd.to_datetime(raw.where(is_dob), format="%Y%m%d", errors="coerce")
    age_from_dob = (df["date"] - dob).dt.days / 365.25
    age_given = pd.to_numeric(raw.where(~is_dob), errors="coerce")
    return age_from_dob.fillna(age_given)


def _parse_birthdate(page_text):
    """Return the player's birthdate from 'var dob = 19810926;' in their page."""
    match = re.search(r"var dob\s*=\s*(\d{8})", page_text)
    if match is None:
        raise ValueError("Could not find the player's birthdate.")
    return pd.to_datetime(match.group(1), format="%Y%m%d")
