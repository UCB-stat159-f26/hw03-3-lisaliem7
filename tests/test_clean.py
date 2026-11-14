import pytest
from mock_data import FEMALE_JS, MALE_JS
from tennisage.clean import _extract_matches


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
