Anime List
==========

The sections below will show you how to get the anime list using different methods.

``getAnimeList()``
++++++++++++++++++

Basic example
-------------

.. code-block:: python3
    :lineno-start: 1

    from myanimelistpy.myanimelist import MyAnimeList

    CLIENT_ID = "YOUR_MY_ANIME_LIST_CLIENT_ID"

    if __name__ == "__main__":
        my_anime_list = MyAnimeList(client_id=CLIENT_ID)

        anime_list = my_anime_list.getAnimeList(
            anime_name = "Hunter x Hunter",
            limit      = 2
        )

        for anime in anime_list:
            print(f"Id: {anime.getId()}")
            print(f"Title: {anime.getTitle()}")
            print(f"Main Picture (medium): {anime.getMainPicture().getMedium()}\n")

.. admonition:: Output

    .. code:: sh

        Id: 11061
        Title: Hunter x Hunter (2011)
        Main Picture (medium): https://api-cdn.myanimelist.net/images/anime/1337/99013.jpg

        Id: 136
        Title: Hunter x Hunter
        Main Picture (medium): https://api-cdn.myanimelist.net/images/anime/8/19473.jpg

Request with fields
-------------------

.. code-block:: python3
    :lineno-start: 1

    from myanimelistpy.myanimelist import MyAnimeList

    CLIENT_ID = "YOUR_MY_ANIME_LIST_CLIENT_ID"

    if __name__ == "__main__":
        my_anime_list = MyAnimeList(client_id=CLIENT_ID)

        anime_list = my_anime_list.getAnimeList(
            anime_name = "Hunter x Hunter",
            limit      = 2,
            fields     = ["rank", "status"]
        )

        for anime in anime_list:
            print(f"Id: {anime.getId()}")
            print(f"Title: {anime.getTitle()}")
            print(f"Main Picture (medium): {anime.getMainPicture().getMedium()}")
            print(f"Rank: {anime.getRank()}")
            print(f"Status: {anime.getStatus()}\n")

.. admonition:: Output

    .. code:: sh

        Id: 11061
        Title: Hunter x Hunter (2011)
        Main Picture (medium): https://api-cdn.myanimelist.net/images/anime/1337/99013.jpg
        Rank: 9
        Status: Finished airing

        Id: 136
        Title: Hunter x Hunter
        Main Picture (medium): https://api-cdn.myanimelist.net/images/anime/8/19473.jpg   
        Rank: 165
        Status: Finished airing

.. tip:: 

    We strongly recommend using a ``.env`` file or something similar to store 
    your **Client ID**. You can use the `python-dotenv <https://pypi.org/project/python-dotenv/>`_ 
    library to do this. `Click here <https://saurabh-kumar.com/python-dotenv/>`_ 
    to check out their documentation.

    Using ``.env`` file
    ~~~~~~~~~~~~~~~~~~~

    .. code-block:: python3
        :lineno-start: 1

        from os import getenv
        from dotenv import load_dotenv

        from myanimelistpy.myanimelist import MyAnimeList

        load_dotenv()

        CLIENT_ID = getenv("CLIENT_ID")

        if __name__ == "__main__":
            my_anime_list = MyAnimeList(client_id=CLIENT_ID)

            anime_list = my_anime_list.getAnimeList(
                anime_name = "Hunter x Hunter",
                limit      = 2,
                fields     = ["rank", "status"]
            )

            for anime in anime_list:
                print(f"Id: {anime.getId()}")
                print(f"Title: {anime.getTitle()}")
                print(f"Main Picture (medium): {anime.getMainPicture().getMedium()}")
                print(f"Rank: {anime.getRank()}")
                print(f"Status: {anime.getStatus()}\n")

    All the next examples will using the `python-dotenv <https://pypi.org/project/python-dotenv/>`_ 
    library, but feel free not to use it if you don't want to.

``getAnimeListInDict()``
++++++++++++++++++++++++

.. code-block:: python3
    :lineno-start: 1

    from os import getenv
    from dotenv import load_dotenv

    from myanimelistpy.myanimelist import MyAnimeList

    load_dotenv()

    CLIENT_ID = getenv("CLIENT_ID")

    if __name__ == "__main__":
        my_anime_list = MyAnimeList(client_id=CLIENT_ID)

        anime_list = my_anime_list.getAnimeListInDict(
            anime_name = "Hunter x Hunter",
            limit      = 2,
            fields     = ["genres"]
        )

        for anime in anime_list:
            print(str(anime) + "\n")

.. admonition:: Output

    .. code:: sh

        {'node': {'id': 11061, 'title': 'Hunter x Hunter (2011)', 'main_picture': {'medium': 'https://api-cdn.myanimelist.net/images/anime/1337/99013.jpg', 'large': 'https://api-cdn.myanimelist.net/images/anime/1337/99013l.jpg'}, 'genres': [{'id': 1, 'name': 'Action'}, {'id': 2, 'name': 'Adventure'}, {'id': 10, 'name': 'Fantasy'}, {'id': 27, 'name': 'Shounen'}]}}

        {'node': {'id': 136, 'title': 'Hunter x Hunter', 'main_picture': {'medium': 'https://api-cdn.myanimelist.net/images/anime/8/19473.jpg', 'large': 'https://api-cdn.myanimelist.net/images/anime/8/19473l.jpg'}, 'genres': [{'id': 1, 'name': 'Action'}, {'id': 2, 'name': 'Adventure'}, {'id': 10, 'name': 'Fantasy'}, {'id': 27, 'name': 'Shounen'}]}}

.. note:: 

    You can access dictionary properties using square brackets:

    .. code-block:: python3
        :lineno-start: 19

        for anime in anime_list:
            print(f"Title: {anime['node']['title']}")
            print(f"Genres: {anime['node']['genres']}\n")

    .. admonition:: Output

        .. code:: sh

            Title: Hunter x Hunter (2011)
            Genres: [{'id': 1, 'name': 'Action'}, {'id': 2, 'name': 'Adventure'}, {'id': 10, 'name': 'Fantasy'}, {'id': 27, 'name': 'Shounen'}]

            Title: Hunter x Hunter
            Genres: [{'id': 1, 'name': 'Action'}, {'id': 2, 'name': 'Adventure'}, {'id': 10, 'name': 'Fantasy'}, {'id': 27, 'name': 'Shounen'}]

``getAnimeListInJSON()``
++++++++++++++++++++++++

.. code-block:: python3
    :lineno-start: 1

    from os import getenv
    from dotenv import load_dotenv

    from myanimelistpy.myanimelist import MyAnimeList

    load_dotenv()

    CLIENT_ID = getenv("CLIENT_ID")

    if __name__ == "__main__":
        my_anime_list = MyAnimeList(client_id=CLIENT_ID)

        anime_list = my_anime_list.getAnimeListInJSON(
            anime_name = "Hunter x Hunter",
            limit      = 2,
            fields     = ["num_episodes"]
        )

        print(anime_list)

.. admonition:: Output

    .. code:: sh

        {"data":[{"node": {"id": 11061, "title": "Hunter x Hunter (2011)", "main_picture": {"medium": "https://api-cdn.myanimelist.net/images/anime/1337/99013.jpg", "large": "https://api-cdn.myanimelist.net/images/anime/1337/99013l.jpg"}, "num_episodes": 148}}, {"node": {"id": 136, "title": "Hunter x Hunter", "main_picture": {"medium": "https://api-cdn.myanimelist.net/images/anime/8/19473.jpg", "large": "https://api-cdn.myanimelist.net/images/anime/8/19473l.jpg"}, "num_episodes": 62}}]}

.. note:: 

    JSON Viewer

    .. code-block:: json

        {
            "data": [
                {
                    "node": {
                        "id": 11061,
                        "title": "Hunter x Hunter (2011)",
                        "main_picture": {
                        "medium": "https://api-cdn.myanimelist.net/images/anime/1337/99013.jpg",
                        "large": "https://api-cdn.myanimelist.net/images/anime/1337/99013l.jpg"
                        },
                        "num_episodes": 148
                    }
                },
                {
                    "node": {
                        "id": 136,
                        "title": "Hunter x Hunter",
                        "main_picture": {
                        "medium": "https://api-cdn.myanimelist.net/images/anime/8/19473.jpg",
                        "large": "https://api-cdn.myanimelist.net/images/anime/8/19473l.jpg"
                        },
                        "num_episodes": 62
                    }
                }
            ]
        }