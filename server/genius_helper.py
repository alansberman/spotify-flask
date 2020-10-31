client_id = "nZ8EhjSky3BnaKKlGjcCItoebIbxmkiM-wqlqbwYZli__DPbg3kQeoPxqziTxD3P"
client_secret = "9qr4PrKcOh5FD5rVJ0IGHXO42JZw-SNYxb-uco9uP9eHl7wYcMQdi75WtndxXkrUJtiX9vTjnyHlICYuOMcH6g"
access_token = "7KhExl9xO6ya4KNscebab7jyVIdP7wM-Qfu18HbSyF1-NNvMFcbZ7s9qb-9X2uRw"
from flask import jsonify

import lyricsgenius
genius = lyricsgenius.Genius(access_token)


def get_lyrics(title, artist_name):
    parsed_query = title.replace("%20"," ")
    parsed_artist_name = artist_name.replace("%20", " ")
    song = genius.search_song(parsed_query, artist_name)
    if song is not None:
        lyrics = { 'lyrics': song.lyrics}
        return jsonify(lyrics)
    else:
        return jsonify({})
