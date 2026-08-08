import sys
from pathlib import Path

# Add project root to Python path
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from dash.testing.application_runners import import_app


def test_header_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")

    assert header.is_displayed()
    assert header.text == "Pink Morsel Sales Dashboard"


def test_visualisation_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    chart = dash_duo.wait_for_element(
        "#sales-line-chart .js-plotly-plot",
        timeout=10
    )

    assert chart.is_displayed()


def test_region_picker_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    picker = dash_duo.find_element("#region-filter")

    assert picker.is_displayed()