import plotly.express as px
from dash import Dash, html, dcc, dash_table


class SCVisualAnalytics:
    def __init__(self, dataframe):
        self.df = dataframe

        self.app = Dash(__name__)

        self.app.layout = html.Div(children=[
            html.H1(children='Welcome to SCVisualAnalytics'),

            html.Div(children=[
                dcc.Graph(
                    id="mean_price",
                    figure=self.__get_pie_mean_rental("price", "location", title="Mean price of rental"),
                    style={'width': '50%'}
                ),
                dcc.Graph(
                    id="mean_price_re",
                    figure=self.__get_pie_mean_rental("deposit_price", "location", title='Mean deposit of rental'),
                    style={'width': '50%'}
                ),
            ], style={
                'display': 'flex',
                'flex-direction': 'row'
            }),

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

    def run_server(self, debug: bool = False):
        print("NOTE: Preparing server...")
        self.app.run_server(debug=debug)

    def __get_table_columns(self):
        df_c = self.df
        columns = []
        for i in df_c.columns:
            if i in ['title', 'location', 'price', 'area', 'media_price', 'rooms_number', 'deposit_price']:
                columns.append({"name": i, "id": i})
        return columns

    def __get_mean_by_column(self, column):
        return self.df.groupby(column).mean().reset_index()

    def __get_pie_mean_rental(self, values, names, title):
        df_m = self.__get_mean_by_column('location')
        fig = px.pie(self.df, values=df_m[values], names=df_m[names], title=title, hole=.3)
        fig.update_traces(textinfo='value')
        return fig
