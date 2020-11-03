import wikipedia
from flask import jsonify
import requests

def get_wiki_summary(query):
    '''
        Get the summary for the first result
    '''
    parsed_query = query.replace("%20"," ")
    result = wikipedia.search(parsed_query)
    if result is not None:
        try:
            return jsonify(wikipedia.summary(result[0], sentences=10))
        except wikipedia.exceptions.DisambiguationError as e:
            for option in e.options:
                if "music" in option:
                    return jsonify(wikipedia.summary(option, sentences=10))
            return jsonify({})
        except wikipedia.exceptions.PageError:
            return jsonify({})
    return jsonify({})


def get_db_artist(query):
    parsed_query = query.replace(" ","_")
    return requests.get(f'http://www.theaudiodb.com/api/v1/json/1/search.php?s={parsed_query}').json()

    
def get_db_album(query):
    parsed_query = query.replace(" ","_")
    return requests.get(f'http://www.theaudiodb.com/api/v1/json/1/search.php?s={parsed_query}').json()

def get_db_track(query):
    parsed_query = query.replace("","_")
    return requests.get(f'http://www.theaudiodb.com/api/v1/json/1/search.php?s={parsed_query}').json()