from flask_caching import Cache
from flask import Flask, jsonify, redirect, request
from flask_cors import CORS
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy_helper import *
from wiki_helper import *
from genius_helper import *
# configuration
DEBUG = True


config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "simple",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_mapping(config)
cache = Cache(app)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/', methods=['GET'])
def auth_spotify():
    return get_playlist_tracks('Klas nommers')


@app.route('/playlist/<id>', methods=['GET'])
@cache.cached(timeout=300)
def playlist(id):
    return get_playlist(id)


@app.route('/track/<id>/details', methods=['GET'])
@cache.cached(timeout=300)
def details(id):
    return get_track_details(id)


@app.route('/track/<title>/artist/<artist_name>/lyrics', methods=['GET'])
@cache.cached(timeout=300)
def lyrics(title, artist_name):
    return get_lyrics(title, artist_name)


@app.route('/track/<id>/audio-analysis', methods=['GET'])
@cache.cached(timeout=300)
def audio_analysis(id):
    return get_track_audio_analysis(id)


@app.route('/track/<id>/audio-features', methods=['GET'])
@cache.cached(timeout=300)
def audio_features(id):
    return get_track_audio_features(id)


@app.route('/artist/<id>', methods=['GET'])
@cache.cached(timeout=300)
def artist(id):
    return get_artist(id)


@app.route('/genres', methods=['GET'])
@cache.cached(timeout=300)
def genres():
    return get_genres()


@app.route('/discover', methods=['GET'])
def discover():
    seed_artists = request.args.get('seed_artists').split('&')
    seed_tracks = request.args.get('seed_tracks').split('&')
    seed_genres = request.args.get('seed_genres').split('&')

    return get_recommendations(seed_artists, seed_genres, seed_tracks)


@app.route('/artist/<id>/related', methods=['GET'])
@cache.cached(timeout=300)
def related_artists(id):
    return get_related_artists(id)


@app.route('/<name>/summary', methods=['GET'])
@cache.cached(timeout=300)
def wiki_summary(name):
    return get_wiki_summary(name)


@app.route('/artist/<id>/top-tracks', methods=['GET'])
@cache.cached(timeout=300)
def artist_top_tracks(id):
    return get_artist_top_tracks(id)


@app.route('/album/<id>', methods=['GET'])
@cache.cached(timeout=300)
def album(id):
    return get_album(id)


@app.route('/playlist/<playlist_id>/add-track/<track_id>', methods=['GET'])
@cache.cached(timeout=300)
def add_track(playlist_id, track_id):
    return add_track_to_playlist(playlist_id, track_id)


@app.route('/my-top-tracks/<term>', methods=['GET'])
@cache.cached(timeout=300)
def user_top_tracks(term):
    return get_user_top_tracks(term)


@app.route('/currently-playing', methods=['GET'])
def now_playing():
    return get_currently_playing()


@app.route('/my-top-tracks/<term>/features', methods=['GET'])
@cache.cached(timeout=300)
def user_top_tracks_features(term):
    return get_several_audio_features(term)


@app.route('/playlist/<playlist_id>/features', methods=['GET'])
@cache.cached(timeout=300)
def get_playlist_features(playlist_id):
    return get_features_of_playlist(playlist_id)


@app.route('/my-top-artists/<term>', methods=['GET'])
@cache.cached(timeout=300)
def user_top_artists(term):
    return get_user_top_artists(term)


@app.route('/search/<query>/tracks', methods=['GET'])
@cache.cached(timeout=300)
def track_search(query):
    return search_tracks(query)


@app.route('/search/<query>/artists', methods=['GET'])
@cache.cached(timeout=300)
def artist_search(query):
    return search_artists(query)


@app.route('/search/<query>/albums', methods=['GET'])
@cache.cached(timeout=300)
def album_search(query):
    return search_albums(query)


@app.route('/search/<query>/playlists', methods=['GET'])
@cache.cached(timeout=300)
def playlist_search(query):
    return search_playlists(query)


@app.route('/playlists', methods=['GET'])
@cache.cached(timeout=300)
def playlists():
    return jsonify(get_user_playlists())


@app.route('/artist/<query>/info', methods=['GET'])
@cache.cached(timeout=300)
def artists_info(query):
    return get_db_artist(query)


@app.route('/album/<query>/info', methods=['GET'])
@cache.cached(timeout=300)
def album_info(query):
    return get_db_album(query)


@app.route('/track/<track>/artist/<artist>/info', methods=['GET'])
@cache.cached(timeout=300)
def genius_track_info(track, artist):
    return get_song(track, artist)


@app.route('/track/<track_id>/annotations', methods=['GET'])
@cache.cached(timeout=300)
def genius_track_annotations(track_id):
    return annotations(track_id)


if __name__ == '__main__':
    app.run()
