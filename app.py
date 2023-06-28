import pandas as pd
import dash
from dash import dcc
from dash import html
import plotly.express as px

# Create a dash application
# Imports the CSV from URL
# 	- Columns Index, Organization Id, Name, Website, Country, Description, Founded, Industry, Number of employees
# 2. Displays the information from the CSV as a Dash Table.
# 3. Displays the information from the CSV as a graph.
# 	- The graph should be an appropriate type for the data.
# 	- The graph must not be a Histogram.

app = dash.Dash(__name__)

# Read CSV file
url = "https://media.githubusercontent.com/media/datablist/sample-csv-" \
      "files/main/files/organizations/organizations-1000.csv"
df = pd.read_csv(url)

# Create Dash Table Component
table = html.Table(
    [
        html.Thead(
            html.Tr([html.Th(col) for col in df.columns])
        ),
        html.Tbody(
            [
                html.Tr([html.Td(str(row[col])) for col in df.columns])
                for _, row in df.iterrows()
            ]
        )
    ]
)

# Create Dash Graph Component using Plotly
graph = px.scatter(df, x="Founded", y="Number of employees", color="Country", hover_name="Name")

app.layout = html.Div(
    [
        html.H1("Organization Data"),
        # Dash Table and Graph components will be added here
        table,
        dcc.Graph(figure=graph)
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
