import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load processed data
df = pd.read_csv("daily_sales.csv")

# Convert date to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")


def create_figure(region):
    """Create the sales line chart for the selected region."""

    if region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == region]

    # Aggregate sales by date
    daily_sales = (
        filtered_df.groupby("date", as_index=False)["sales"]
        .sum()
        .sort_values("date")
    )

    fig = px.line(
        daily_sales,
        x="date",
        y="sales",
        title="Pink Morsel Sales Over Time"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales",
        template="plotly_white",
        margin=dict(l=50, r=30, t=70, b=50),
        hovermode="x unified"
    )

    return fig


# Create Dash app
app = Dash(__name__)

app.layout = html.Div(
    className="container",
    children=[
        html.H1(
            "Pink Morsel Sales Dashboard",
            className="title"
        ),

        html.P(
            "Explore Pink Morsel sales by region",
            className="subtitle"
        ),

        html.Div(
            className="filter-container",
            children=[
                html.Label(
                    "Select Region:",
                    className="filter-label"
                ),

                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                        {"label": "All", "value": "all"},
                    ],
                    value="all",
                    inline=True,
                    className="radio-options"
                )
            ]
        ),

        dcc.Graph(
            id="sales-line-chart",
            figure=create_figure("all"),
            className="chart"
        )
    ]
)


@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    return create_figure(selected_region)


if __name__ == "__main__":
    app.run(debug=True)