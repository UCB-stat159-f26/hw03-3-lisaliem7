import matplotlib

matplotlib.use("Agg")

import pandas as pd
import pytest
from mock_data import MALE_JS
from tennisage.clean import _build_career_frame
from tennisage.plot import plot_age_gap


def _mock_frame():
    return _build_career_frame(MALE_JS, pd.Timestamp("1981-09-26"))


def test_plot_age_gap_returns_figure_with_one_axis():
    fig = plot_age_gap(_mock_frame())
    assert len(fig.axes) == 1


def test_plot_age_gap_has_axis_labels():
    ax = plot_age_gap(_mock_frame()).axes[0]
    assert "age" in ax.get_xlabel().lower()
    assert "opponent" in ax.get_ylabel().lower()


def test_plot_age_gap_bad_input_raises():
    with pytest.raises(ValueError):
        plot_age_gap(pd.DataFrame({"x": [1, 2]}))
