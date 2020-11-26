import json
import urllib

def read_bing_key():
    """
    Reads the BING API key from a file called 'bing.key'.
    returns: a string which is either None, or with a key.
    Remember: put bing.key in you .gitignore file to avoid committing it!
    """
    bing_api_key = None
    
    try:
        with open('bing.key','r') as f:
            bing_api_key = f.readline()
    except:
        raise IOError('bing.key file not found')

    return bing_api_key

def run_query(search_items):
    """
    Given a string containing seach terms (query),
    returns a list of results from the Bing search engine
    """