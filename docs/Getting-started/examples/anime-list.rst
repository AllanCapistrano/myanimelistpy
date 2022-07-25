Anime List
==========

These sections below will show simple examples of different usages of the 
``getAnimeList()`` method.

Basic example
-------------

.. code-block:: python3
   
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

Output

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

Output

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