import wikipedia
from flask import jsonify


def get_wiki_summary(query):
    '''
        Get the summary for the first result
    '''
    parsed_query = query.replace("%20"," ")
    result = wikipedia.search(parsed_query)
    print(result)
    if result is not None:
        try:
            print(result[0])
            page = wikipedia.page(result[0])
            return jsonify(wikipedia.summary(result[0], sentences=10))
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
            for option in e.options:
                if "music" in option:
                    page = wikipedia.page(option)
                    return jsonify(wikipedia.summary(option, sentences=10))
            return jsonify({})
        except wikipedia.exceptions.PageError:
            return jsonify({})
    return jsonify({})

