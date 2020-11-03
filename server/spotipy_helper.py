import spotipy
from os import environ
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from flask import jsonify
from dotenv import load_dotenv
load_dotenv()

scopes = ["user-read-currently-playing",
          "user-read-playback-state",
          "user-modify-playback-state",
          "playlist-read-collaborative",
          "playlist-modify-private",
          "playlist-read-private",
          "playlist-modify-public",
          "user-library-modify",
          "user-library-read",
          "user-read-private",
          "user-read-email",
          "user-follow-read",
          "user-follow-modify",
          "user-read-recently-played",
          "user-read-playback-position",
          "user-top-read"]
scopes = " ".join(scopes)

oauth = SpotifyOAuth(client_id=environ.get("SPOTIFY_CLIENT_ID"),client_secret=environ.get("SPOTIFY_CLIENT_SECRET"),
       redirect_uri = "http://localhost:8100/callback/", scope=scopes)
sp = spotipy.Spotify(auth_manager=oauth)

def refresh_token_if_expired():
    token = oauth.get_cached_token()
    result = oauth.is_token_expired(token)
    if not result:
        oauth.refresh_access_token(token['refresh_token'])


def get_playlist_tracks(playlist):
    '''
        Gets the (first 100) tracks of a playlist (if found)
        Params:
            playlist | string | playlist searched for
    '''
    result = sp.search(q=playlist, type='playlist')
    for item in result['playlists']['items']:
        if item['name'] == playlist:
            return get_track(sp.playlist_tracks(item['uri']))
    return None


def search_tracks(query):
    parsed_query = query.replace("%20"," ")
    result = sp.search(q=parsed_query, type='track')
    if result:
        return jsonify(result)
    return jsonify({})

def search_albums(query):
    parsed_query = query.replace("%20"," ")
    result = sp.search(q=parsed_query, type='album')
    if result:
        return jsonify(result)
    return jsonify({})

def search_artists(query):
    parsed_query = query.replace("%20"," ")
    result = sp.search(q=parsed_query, type='artist')
    if result:
        return jsonify(result)
    return jsonify({})

def search_playlists(query):
    parsed_query = query.replace("%20"," ")
    result = sp.search(q=parsed_query, type='playlist')
    if result:
        return jsonify(result)
    return jsonify({})

def get_playlist(playlist_id):
    result = sp.playlist(playlist_id)
    return jsonify(result)

def get_track_audio_features(track_id):
    result = sp.audio_features(track_id)
    return jsonify(result)

def get_track_details(track_id):
    result = sp.track(track_id)
    return jsonify(result)


def get_track_audio_analysis(track_id):
    result = sp.audio_analysis(track_id)
    return jsonify(result)

def get_artist(artist_id):
    result = sp.artist(artist_id)
    return jsonify(result)

def get_related_artists(artist_id):
    result = sp.artist_related_artists(artist_id)
    return jsonify(result)

def get_artist_top_tracks(artist_id):
    result = sp.artist_top_tracks(artist_id)
    return jsonify(result)


def get_album(album_id):
    result = sp.album(album_id)
    return jsonify(result)

def add_track_to_playlist(playlist_id, track_id):
    result = sp.playlist_add_items(playlist_id, [track_id])
    return jsonify(result)

def get_user_top_tracks(term):
    result = sp.current_user_top_tracks(time_range=term,limit=50)
    return jsonify(result)

def get_user_top_artists(term):
    result = sp.current_user_top_artists(time_range=term,limit=50)
    return jsonify(result)

def get_several_audio_features(term):
    result = sp.current_user_top_tracks(time_range=term,limit=50)
    ids = []
    for track in result['items']:
        ids.append(track['id'])
    response = sp.audio_features(ids)
    return jsonify(response)

def get_features_of_playlist(playlist_id):
    result = sp.playlist(playlist_id)
    ids = []
    for track in result['tracks']['items']:
        # print(track['track'].keys())
        ids.append(track['track']['id'])
    response = sp.audio_features(ids)
    return jsonify(response)


def get_currently_playing():
    '''
        Gets the user's currently playing track
    '''
    return jsonify(sp.current_user_playing_track())

def get_user_playlists():
    '''
        Gets the user's currently playing track
    '''
    #refresh_token_if_expired()
    return sp.current_user_playlists()

def get_track(tracks):
    '''
        Gets the info for the (first 100) tracks of a playlist
        Params:
            tracks | Response | tracks
    '''
    tracklist = []
    for track in tracks['items']:
        song = (track['track']['name'], track['track']['artists'][0]['name'], track['track']['uri'])
        tracklist.append(song)
    return jsonify(tracklist)

