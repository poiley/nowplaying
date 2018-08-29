import json, os, spotipy
import auth, data_models
from flask import Flask, render_template, url_for

application = Flask(__name__)

@application.route("/")
def main():
    auth = get_auth_obj()
    song = fetch_current_playing(auth)
    
    if not song:
        return render_template( "index.html", 
                                song="Nothing Playing",
                                art_url="/static/placeholder.jpg")
    
    return render_template( "index.html", 
                            song=song.get_song(), 
                            artist=song.get_artist(), 
                            album=song.get_album(),
                            art_url=song.get_album_art_url())

@application.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join( application.root_path,
                                      endpoint, 
                                      filename )
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

def fetch_current_playing(auth):
        spotify = spotipy.Spotify(auth=auth.user_token)
        playing = spotify.current_playback()

        if playing == None:
            return None
        
        return data_models.song(playing["item"])

def get_auth_obj():
    data = read_data()
    return auth.spotify_auth(data["username"],
                             data["scope"],
                             data["client_id"],
                             data["client_secret"],
                             redirect_uri=data["redirect_uri"])

def read_data():
    with open("auth.json") as file:
        return json.load(file)
