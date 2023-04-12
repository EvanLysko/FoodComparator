import requests

_base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
_url_key_ending = "&key=AIzaSyD6XC9bqblOB1b0UdXo88jGUX0qT2Jwd4Q"

def __getUrlQueryFromTextSearch(text_search_string):
    text_search_string = text_search_string.replace(" ", "%20")
    print("url: " + _base_url + text_search_string + _url_key_ending)
    return _base_url + text_search_string + _url_key_ending

def get(search_string):
    """_summary_

    Args:
        search_string (_type_): _description_ can be search string or next_page_token

    Returns:
        _type_: _description_ json of request
    """
    try:
        response = requests.get(__getUrlQueryFromTextSearch(search_string))
    except requests.exceptions.RequestException as e:
        raise requestError(e)
    return response.json()

def requestError(e):
    print(e)
    
