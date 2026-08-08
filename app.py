import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load the processed data
df = pd.read_csv("daily_sales.csv")

# Convert date to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")

# Aggregate sales across all regions for each date
daily_sales = df.groupby("date", as_index=False)["sales"].sum()

# Create the line chart
fig = px.line(
    daily_sales,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time"
)

# Add axis labels
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales"
)

# Create Dash application
app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Pink Morsel Sales Dashboard"),

        dcc.Graph(
            id="sales-line-chart",
            figure=fig
        )
    ]
)

if __name__ == "__main__":
    app.run(debug=True)