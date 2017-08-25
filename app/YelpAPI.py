from urllib.parse import quote
import requests
import json
import pprint as pp
import random
from app import db
from app.models import Restaurant

API_HOST = "https://api.yelp.com/"
SEARCH_PATH = "v3/businesses/search"


def request(host, path, bearer_token, url_params=None):
    """Given a bearer token, send a GET request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        bearer_token (str): OAuth bearer token, obtained using client_id and client_secret.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % bearer_token,
    }

    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)
    return response.json()

def getRestaurants(bearer_token, location = "Jet Propulsion Laboratory", num=5):
    params = {"location": location,
          "term" : "restaurants",
          "limit" : "50",
          "open_now": True}
    result = request(API_HOST, SEARCH_PATH, bearer_token, params)['businesses']
    return random.sample(result, num)

if __name__ == "__main__":

    things = getRestaurants(bearer_token, num=1)
    pp.pprint(things)
    print(things[0]['image_url'])
