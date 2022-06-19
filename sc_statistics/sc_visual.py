import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, html, dcc, dash_table


class SCVisualAnalytics:
    def __init__(self, dataframe):
        self.df = dataframe

        self.app = Dash(__name__)

        self.app.layout = html.Div(children=[
            html.H1(children='Hello Dash'),

            dash_table.DataTable(
                id='table',
                columns=self.__get_table_columns(),
                data=self.df.to_dict('records'),
                style_cell=dict(textAlign='left'),
                style_header=dict(backgroundColor="paleturquoise"),
                style_data=dict(backgroundColor="lavender"),
                page_size=10
            ),
        ])

    def run_server(self, debug: bool):
        self.app.run_server(debug=debug)

    def __get_table_columns(self):
        df_c = self.df
        columns = []
        for i in df_c.columns:
            if i in ['title', 'location', 'price', 'area', 'media_price', 'rooms_number', 'deposit_price']:
                columns.append({"name": i, "id": i})

        return columns
