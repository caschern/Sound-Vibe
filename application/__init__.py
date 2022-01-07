"""Initialize Flask app."""
from ddtrace import patch_all
from flask import Flask
from flask_assets import Environment
import nltk
import pandas as pd
import string
import numpy as np
import re
from dotenv import load_dotenv

from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import string
patch_all()


def create_dataframe():
    """Create Pandas DataFrame from local CSV."""
    df = pd.read_csv('https://raw.githubusercontent.com/caschern/Project-Song-Vibe/main/DATA/music_data.csv')
    return df

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
stopwords = stopwords.words('english')

def make_lower(a_string):
    return a_string.lower()

def remove_punctuation(a_string):    
    a_string = re.sub(r'[^\w\s]','',a_string)
    return a_string

def text_pipeline(input_string):
    input_string = make_lower(input_string)
    input_string = remove_punctuation(input_string)   
    return input_string

def init_app():
    """Construct core Flask application with embedded Dash app."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    assets = Environment()
    assets.init_app(app)
    

    with app.app_context():
        # Import parts of our application
        from .home import home
        from .assets import compile_static_assets

        # Register Blueprints
        app.register_blueprint(home.home_bp)
        compile_static_assets(assets)

        return app