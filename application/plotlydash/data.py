"""Prepare data for Plotly Dash."""
import numpy as np
import pandas as pd


def create_dataframe():
    """Create Pandas DataFrame from local CSV."""
    df = pd.read_csv('C:/Users/Y/Desktop/flask_prac/app/data/music_data.csv')
    return df
