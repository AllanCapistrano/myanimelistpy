Reference
=========

The following section outlines the reference of myanimelistpy.

MyAnimeList
+++++++++++

.. class:: myanimelist.MyAnimeList(client_id)

.. list-table::
    :widths: 10
    :header-rows: 1

    * - Methods
    * - :ref:`getAnimeList <getanimelist>`
    * - :ref:`getAnimeListInDict <getanimelistindict>`
    * - :ref:`getAnimeListInJSON <getanimelistinjson>`

**Parameters:**
    - client_id (`str <https://docs.python.org/3/library/stdtypes.html#str>`_) - MyAnimeList Client ID.

Methods
-------

.. method:: getAnimeList(anime_name, limit = 100, offset = 0, fields = [])
.. _getAnimeList:

    Returns a list of anime by name.

    **Parameters:**
      - anime_name(`str <https://docs.python.org/3/library/stdtypes.html#str>`_) -  Name of the anime/series.
      - limit(Optional[`int <https://docs.python.org/3/library/functions.html#int>`_]) - The maximum size of the list. The default value is 100.
      - offset(Optional[`int <https://docs.python.org/3/library/functions.html#int>`_]) -  The list offset. The default value is 0.
      - fields(Optional[`List <https://docs.python.org/3/library/stdtypes.html#list>`_ [`str <https://docs.python.org/3/library/stdtypes.html#str>`_]]) - List of fields used to show more information about the anime. If is empty, the default fields are id, title and main_picture.

    **Raises:**
      - `ValueError <https://docs.python.org/3/library/exceptions.html#ValueError>`_ - The 'field' is not a valid field!

    **Returns:**
        List of animes.
        
    **Return type:**
        `List <https://docs.python.org/3/library/stdtypes.html#list>`_ [Anime]

.. method:: getAnimeListInDict(anime_name, limit = 100, offset = 0, fields = [])
.. _getAnimeListInDict:

    Returns a list of dictionaries containing the anime by name.

    **Parameters:**
      - anime_name(`str <https://docs.python.org/3/library/stdtypes.html#str>`_) -  Name of the anime/series.
      - limit(Optional[`int <https://docs.python.org/3/library/functions.html#int>`_]) - The maximum size of the list. The default value is 100.
      - offset(Optional[`int <https://docs.python.org/3/library/functions.html#int>`_]) -  The list offset. The default value is 0.
      - fields(Optional[`List <https://docs.python.org/3/library/stdtypes.html#list>`_ [`str <https://docs.python.org/3/library/stdtypes.html#str>`_]]) - List of fields used to show more information about the anime. If is empty, the default fields are id, title and main_picture.

    **Raises:**
      - `ValueError <https://docs.python.org/3/library/exceptions.html#ValueError>`_ - The 'field' is not a valid field!

    **Returns:**
        List of animes in `dict <https://docs.python.org/3/library/stdtypes.html#dict>`_ type.
        
    **Return type:**
        `dict <https://docs.python.org/3/library/stdtypes.html#dict>`_

.. method:: getAnimeListInJSON(anime_name, limit = 100, offset = 0, fields = [])
.. _getAnimeListInJSON:

    Returns a JSON stringified containing the list of anime by name.

    **Parameters:**
      - anime_name(`str <https://docs.python.org/3/library/stdtypes.html#str>`_) -  Name of the anime/series.
      - limit(Optional[`int <https://docs.python.org/3/library/functions.html#int>`_]) - The maximum size of the list. The default value is 100.
      - offset(Optional[`int <https://docs.python.org/3/library/functions.html#int>`_]) -  The list offset. The default value is 0.
      - fields(Optional[`List <https://docs.python.org/3/library/stdtypes.html#list>`_ [`str <https://docs.python.org/3/library/stdtypes.html#str>`_]]) - List of fields used to show more information about the anime. If is empty, the default fields are id, title and main_picture.

    **Raises:**
      - `ValueError <https://docs.python.org/3/library/exceptions.html#ValueError>`_ - The 'field' is not a valid field!

    **Returns:**
        List of animes in `JSON <https://www.json.org/json-en.html>`_ format.
        
    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_