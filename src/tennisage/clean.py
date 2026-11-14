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
