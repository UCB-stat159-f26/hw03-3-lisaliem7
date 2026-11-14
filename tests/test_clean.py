import pandas as pd
import pytest
from mock_data import FEMALE_JS, MALE_JS
from tennisage.clean import _extract_matches, _rows_to_frame, _opponent_age, _parse_birthdate, _build_career_frame


def test_extract_matches_female_returns_three_rows():
    assert len(_extract_matches(FEMALE_JS)) == 3


def test_extract_matches_male_returns_three_rows():
    assert len(_extract_matches(MALE_JS)) == 3


def test_extract_matches_keeps_opponent_name():
    rows = _extract_matches(FEMALE_JS)
    assert rows[0][11] == "Anne Miller"


def test_extract_matches_bad_input_raises():
    with pytest.raises(ValueError):
        _extract_matches("this is not a career file")


def test_rows_to_frame_has_expected_columns():
    df = _rows_to_frame(_extract_matches(FEMALE_JS))
    assert list(df.columns) == ["date", "result", "opponent", "opp_age_or_dob"]


def test_rows_to_frame_male_result_values():
    df = _rows_to_frame(_extract_matches(MALE_JS))
    assert df["result"].tolist() == ["L", "L", "W"]


def _frame_with_dates(js_text):
    df = _rows_to_frame(_extract_matches(js_text))
    df["date"] = pd.to_datetime(df["date"], format="%Y%m%d")
    return df


def test_opponent_age_from_birthdate_for_women():
    ages = _opponent_age(_frame_with_dates(FEMALE_JS))
    assert ages.iloc[0] == pytest.approx(18.78, abs=0.05)


def test_opponent_age_used_directly_for_men():
    ages = _opponent_age(_frame_with_dates(MALE_JS))
    assert ages.iloc[0] == pytest.approx(22.264, abs=0.01)


def test_parse_birthdate_reads_dob_line():
    page = "<script>var name = 'x'; var dob = 19810926; var y = 2;</script>"
    assert _parse_birthdate(page) == pd.Timestamp("1981-09-26")


def test_parse_birthdate_missing_raises():
    with pytest.raises(ValueError):
        _parse_birthdate("<html>no birthdate here</html>")


def test_build_career_frame_columns():
    df = _build_career_frame(MALE_JS, pd.Timestamp("1981-09-26"))
    expected = ["date", "opponent", "player_age", "opp_age", "age_diff", "won"]
    assert list(df.columns) == expected


def test_build_career_frame_win_flags():
    df = _build_career_frame(MALE_JS, pd.Timestamp("1981-09-26"))
    assert df["won"].tolist() == [False, False, True]


def test_build_career_frame_age_difference():
    df = _build_career_frame(MALE_JS, pd.Timestamp("1981-09-26"))
    assert df["age_diff"].iloc[0] == pytest.approx(-2.31, abs=0.05)
