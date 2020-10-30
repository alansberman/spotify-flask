import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from spotipy_helper import *
from flask import jsonify
#sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="792f2c7ad9fb42f983d9b450cc780f7d",client_secret="cb9814762dce43a7b77a377ccae02ab5"))
oauth = SpotifyOAuth(client_id="792f2c7ad9fb42f983d9b450cc780f7d",client_secret="cb9814762dce43a7b77a377ccae02ab5",
       redirect_uri = "http://localhost:8100/callback/", scope="user-library-read user-read-currently-playing user-top-read")
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

def get_artist_top_tracks(artist_id):
    result = sp.artist_top_tracks(artist_id)
    return jsonify(result)


def get_album(album_id):
    result = sp.album(album_id)
    return jsonify(result)

def get_user_top_tracks(term):
    result = sp.current_user_top_tracks(time_range=term,limit=50)
    return jsonify(result)

def get_user_top_artists(term):
    result = sp.current_user_top_artists(time_range=term,limit=50)
    return jsonify(result)


def get_currently_playing():
    '''
        Gets the user's currently playing track
    '''
    return sp.current_user_playing_track()

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

