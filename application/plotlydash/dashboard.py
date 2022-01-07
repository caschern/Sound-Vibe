"""Instantiate a Dash app."""
import dash
import flask
import re
from flask import Flask, jsonify
from dash import dcc
from dash import html
from dash import dash_table
import numpy as np
import pandas as pd
from flask import current_app as app
from .data import create_dataframe
from .layout import html_layout
 
#from application import routes

def make_lower(a_string):
    return a_string.lower()

def remove_punctuation(a_string):    
    a_string = re.sub(r'[^\w\s]','',a_string)
    return a_string

def text_pipeline(input_string):
    input_string = make_lower(input_string)
    input_string = remove_punctuation(input_string)   
    return input_string

def create_search():
    df = pd.read_csv('https://raw.githubusercontent.com/SamuelObregon1/Project-Song-Vibe/main/DATA/music_data.csv')
    return 1

def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix="/dashapp/",
        external_stylesheets=[
            "/static/dist/css/styles.css",
            "https://fonts.googleapis.com/css?family=Lato",
        ],
    )

    # Load DataFrame
    df = create_dataframe()

    # Custom HTML layout
    dash_app.index_string = html_layout

    # Create Layout
    dash_app.layout = html.Div(
        children=[
            dcc.Graph(
                id="histogram-graph",
                figure={
                    "data": [
                        {
                            "x": df["artist_name"],
                            "text": df["artist_name"],
                            "customdata": df["key"],
                            "name": "artist results",
                            "type": "histogram",
                        }
                    ],
                    "layout": {
                        "title": "The Artists",
                        "height": 500,
                        "padding": 150,
                    },
                },
            ),
            create_data_table(df),
        ],
        id="dash-container",
    )
    return dash_app.server


def create_data_table(df):
    """Create Dash datatable from Pandas DataFrame."""
    table = dash_table.DataTable(
        id="database-table",
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        sort_action="native",
        sort_mode="native",
        page_size=300,
    )
    return table