from flask import Flask, jsonify
from flask_cors import CORS
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy_helper import *
from wiki_helper import *
from genius_helper import *
# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', methods=['GET'])
def auth_spotify():
    return get_playlist_tracks('Klas nommers')

@app.route('/playlist/<id>', methods=['GET'])
def playlist(id):
    return get_playlist(id)

@app.route('/track/<id>/details', methods=['GET'])
def details(id):
    return get_track_details(id)

@app.route('/track/<title>/artist/<artist_name>/lyrics', methods=['GET'])
def lyrics(title, artist_name):
    return get_lyrics(title, artist_name)

@app.route('/track/<id>/audio-analysis', methods=['GET'])
def audio_analysis(id):
    return get_track_audio_analysis(id)

@app.route('/track/<id>/audio-features', methods=['GET'])
def audio_features(id):
    return get_track_audio_features(id)

@app.route('/artist/<id>', methods=['GET'])
def artist(id):
    return get_artist(id)

@app.route('/artist/<id>/related', methods=['GET'])
def related_artists(id):
    return get_related_artists(id)

@app.route('/<name>/summary', methods=['GET'])
def wiki_summary(name):
    return get_wiki_summary(name)

@app.route('/artist/<id>/top-tracks', methods=['GET'])
def artist_top_tracks(id):
    return get_artist_top_tracks(id)

@app.route('/album/<id>', methods=['GET'])
def album(id):
    return get_album(id)

@app.route('/playlist/<playlist_id>/add-track/<track_id>', methods=['POST'])
def add_track(playlist_id, track_id):
    return get_album(id)

@app.route('/my-top-tracks/<term>', methods=['GET'])
def user_top_tracks(term):
   return get_user_top_tracks(term)

@app.route('/my-top-tracks/<term>/features', methods=['GET'])
def user_top_tracks_features(term):
   return get_several_audio_features(term)




@app.route('/my-top-artists/<term>', methods=['GET'])
def user_top_artists(term):
   return get_user_top_artists(term)

@app.route('/search/<query>/tracks', methods=['GET'])
def track_search(query):
    return search_tracks(query)

@app.route('/search/<query>/artists', methods=['GET'])
def artist_search(query):
    return search_artists(query)

@app.route('/search/<query>/albums', methods=['GET'])
def album_search(query):
    return search_albums(query)

@app.route('/search/<query>/playlists', methods=['GET'])
def playlist_search(query):
    return search_playlists(query)        

@app.route('/playlists', methods=['GET'])
def playlists():
   return jsonify(get_user_playlists())

@app.route('/artist/<query>/info', methods=['GET'])
def artists_info(query):
   return get_db_artist(query)
if __name__ == '__main__':
    app.run()
