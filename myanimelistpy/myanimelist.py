import requests
from typing import List
import json

from .services.validateFields import validateFields
from .anime import Anime

# ------------------------------ Constants ----------------------------------- #
BASE_URL            = "https://api.myanimelist.net/v2"
ANIME_LIST_ENDPOINT = "anime"
AUTH_HEADER         = "X-MAL-CLIENT-ID"
# ---------------------------------------------------------------------------- #

class MyAnimeList:
    def __init__(self, client_id: str) -> None:
        """ Constructor.

        Parameters
        -----------
        client_id: :class:`str`
            MyAnimeList Client ID.
        """
        
        self.client_id = client_id
        self.base_url  =  BASE_URL

    def getAnimeList(
        self, 
        anime_name: str, 
        limit: int = 100, 
        offset: int = 0,
        fields: List[str] = []
    ) -> List[Anime]:
        # TODO: Documentation of the method

        validateFields(fields=fields)
        
        url = f"{BASE_URL}/{ANIME_LIST_ENDPOINT}?q={anime_name}&limit={limit}&offset={offset}"

        if(len(fields) > 0):
            url += f"&fields={fields}"

        response = requests.get(
            url     = url,
            headers = {AUTH_HEADER: self.client_id}
        )

        responseJson: dict  = response.json()
        animes: List[Anime] = []

        for index in range(len(responseJson["data"])):
            animes.append(
                Anime(node=responseJson["data"][index]["node"], fields=fields)
            )

        return animes
