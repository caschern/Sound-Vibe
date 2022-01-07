"""Core Flask app routes."""
from flask import Flask
from flask_assets import Environment



def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    assets = Environment()  # Create an assets environment
    assets.init_app(app)  # Initialize Flask-Assets

    with app.app_context():
        # Import parts of our application
        from .profile import profile
        from .home import home
        from .products import products
        from .assets import compile_static_assets

        # Register Blueprints
        app.register_blueprint(profile.account_bp)
        app.register_blueprint(home.home_bp)
        app.register_blueprint(products.product_bp)

        # Compile static assets
        compile_static_assets(assets)  # Execute logic

        return app


import flask
from flask import render_template, redirect, url_for, request
from flask import current_app as app
app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')
assets = Environment()  # Create an assets environment
assets.init_app(app)  # Initialize Flask-Assets


@app.route('/' method = ['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('index.html'))
        #return(flask.render_template('index.html'))
    
    if flask.request.method == 'POST':
        # Get the input from the user.
        
        user_input_text = flask.request.form['user_input_text']
        #Created new list to store userinput
        list1 = re.split('\s+', user_input_text)    
        print(list1)
        j=0
        
        #data_frame = df[df['message_clean'].str.contains(Filter)]
        
        #data_frame = df[x for x in usertext if df['message_clean'].str.contains(x).any()]
        #data_frame = df[df['message_clean'].str.contains(list1[j]) & df['message_clean'].str.contains(list1[j+1]) & df['message_clean'].str.contains(list1[j+2])]
        data_frame = df[df['message_clean'].str.contains(list1[j]) & df['message_clean'].str.contains(list1[j+1]) & df['message_clean'].str.contains(list1[j+2])]
        cd = data_frame['artist_name']
        vd = data_frame['genre']
        gg = data_frame['max value']
        db = data_frame['mood_feeling']
        ll = data_frame['track_name']

        print(gg)

        artists =[]
        genre = []
        song = []
        final = []
        gate = []
        rest = []
        boat = []
        
        list1 = re.split('\s+', user_input_text)    
        print(list1)
        j=0
        for x in gg:
            gate.append(x)
        
        for x in db:
            rest.append(x)

        for x in cd:
            artists.append(x)

        for x in vd:
            genre.append(x)
        
        for x in ll:
            song.append(x)

        i = 0
        for x in artists:
            final.append("Artist: " + artists[i] + ", Genre: " + genre[i] + ", Song: " + song[i])
            i+=1
    
        i = 0
        for x in gate:
            boat.append("Artist: " + artists[i]+ ", " + "Mood: " + rest[i])
            i+=1
        print(rest)
        #print(data_frame)
        #print(data_frame['genre'] == 'pop', data_frame['genre'] == 'blues', data_frame['genre'] == 'rock', data_frame['genre'] == 'reggae', data_frame['genre'] == 'jazz', data_frame['genre'] == 'hip hop', data_frame['genre'] == 'country')

        #fig = px.pie(data_frame, values='max value', names='mood_feeling')
        #fig.show()

        print(final)
        data_frame.head()
    
        return flask.render_template('index.html', 
            input_text=user_input_text,
            final = final,
            gate = gate,
            #the_vibes = json.dumps(gate),
            #the_labels = json.dumps(boat)
            )