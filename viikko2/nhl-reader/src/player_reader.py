import requests
from player import Player

# pylint: disable=too-few-public-methods
class PlayerReader:
    """Reads player data from an API."""
    def __init__(self, url):
        self._url = url
     

    def get_players(self):
        response = requests.get(self._url, timeout=10).json()
        return [Player(player_dict) for player_dict in response]
