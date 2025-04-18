import requests
from typing import List
from json import dumps

from .services.validateFields import validate_fields
from .models.anime import Anime

# ------------------------------ Constants ----------------------------------- #
BASE_URL                   = "https://api.myanimelist.net/v2"
ANIME_LIST_ENDPOINT        = "anime"
AUTH_HEADER                = "X-MAL-CLIENT-ID"
REQUEST_TIMEOUT_IN_SECONDS = 30
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

    def get_anime_list_in_dict(
        self,
        anime_name: str,
        limit: int = 100,
        offset: int = 0,
        fields: List[str] = None
    ) -> dict:
        """ Returns a list of dictionaries containing the anime by name.

        Parameters
        -----------
        anime_name: :class:`str`
            Name of the anime/series.
        limit: :class:`int`
            The maximum size of the list. `The default value is 100`.
        offset: :class:`int`
            The list offset. `The default value is 0`.
        fields: :class:`List[str]`
            List of fields used to show more information about the anime. If is 
            empty, the default fields are `id`, `title` and `main_picture`.

        Returns
        -----------
        animes: :class:`dict`
        """

        if fields is None:
            fields = []

        validate_fields(fields=fields)

        url = f"{BASE_URL}/{ANIME_LIST_ENDPOINT}?q={anime_name}&limit={limit}&offset={offset}"

        if len(fields) > 0:
            url += f"&fields={fields}"

        response = requests.get(
            url     = url,
            headers = {AUTH_HEADER: self.client_id},
            timeout = REQUEST_TIMEOUT_IN_SECONDS
        )

        temp: List[dict] = response.json()["data"]

        return temp

    def get_anime_list(
        self,
        anime_name: str,
        limit: int = 100,
        offset: int = 0,
        fields: List[str] = None
    ) -> List[Anime]:
        """ Returns a list of anime by name.

        Parameters
        -----------
        anime_name: :class:`str`
            Name of the anime/series.
        limit: :class:`int`
            The maximum size of the list. `The default value is 100`.
        offset: :class:`int`
            The list offset. `The default value is 0`.
        fields: :class:`List[str]`
            List of fields used to show more information about the anime. If is 
            empty, the default fields are `id`, `title` and `main_picture`.

        Returns
        -----------
        animes: :class:`List[Anime]`
        """

        if fields is None:
            fields = []

        response_json: dict = self.get_anime_list_in_dict(
            anime_name = anime_name,
            limit      = limit,
            offset     = offset,
            fields     = fields,
        )

        animes: List[Anime] = []

        for item in response_json:
            animes.append(Anime(node=item["node"], fields=fields))

        return animes

    def get_anime_List_in_json(
        self,
        anime_name: str,
        limit: int = 100,
        offset: int = 0,
        fields: List[str] = None
    ) -> str:
        """ Returns a JSON stringified containing the list of anime by name.

        Parameters
        -----------
        anime_name: :class:`str`
            Name of the anime/series.
        limit: :class:`int`
            The maximum size of the list. `The default value is 100`.
        offset: :class:`int`
            The list offset. `The default value is 0`.
        fields: :class:`List[str]`
            List of fields used to show more information about the anime. If is 
            empty, the default fields are `id`, `title` and `main_picture`.

        Returns
        -----------
        animes: :class:`str`
        """

        if fields is None:
            fields = []

        response_json: dict = self.get_anime_list_in_dict(
            anime_name = anime_name,
            limit      = limit,
            offset     = offset,
            fields     = fields,
        )

        return '{"data":' + dumps(response_json) + '}'
