from flask import jsonify
from dotenv import load_dotenv
from os import environ

import lyricsgenius
load_dotenv()
genius = lyricsgenius.Genius(environ.get("GENIUS_ACCESS_TOKEN"))


def get_lyrics(title, artist_name):
    parsed_query = title.replace("%20", " ")
    parsed_artist_name = artist_name.replace("%20", " ")
    song = genius.search_song(parsed_query, parsed_artist_name)
    if song is not None:
        lyrics = {'lyrics': song.lyrics}
        return jsonify(lyrics)
    else:
        return jsonify({})


def get_song(title, artist_name):
    parsed_query = title.replace("%20", " ")
    parsed_artist_name = artist_name.replace("%20", " ")
    song = genius.search_song(parsed_query, parsed_artist_name)
    if song is not None:
        return song.to_json()
    else:
        return jsonify({})


def annotations(id):
    annotations = genius.song_annotations(id)
    if annotations is not None:
        return parse_annotations(annotations)
    else:
        return jsonify({})


def parse_annotations(annotations):
    result = {}
    for item in annotations:
        result[item[0]] = ""
        annotation_list = list(item[1][0])
        for annotation in annotation_list:
            result[item[0]] += annotation
    return result
