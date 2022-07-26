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

        .. TODO: Colocar hyperlink em Anime

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

Services
++++++++

Services that are used in the library.

.. list-table::
    :widths: 10
    :header-rows: 1

    * - Methods
    * - :ref:`validateFields <validatefields>`

.. method:: services.validateFields(fields)
.. _validateFields:

    Validate the fields provided.

    **Parameters:**
    - fields(`List <https://docs.python.org/3/library/stdtypes.html#list>`_ [`str <https://docs.python.org/3/library/stdtypes.html#str>`_]) - List of fields.

    **Raises:**
      - `ValueError <https://docs.python.org/3/library/exceptions.html#ValueError>`_ - The 'field' is not a valid field!

    **Returns:**
        If the fields are valid or not.
        
    **Return type:**
        `bool <https://docs.python.org/3/library/functions.html#bool>`_

Models
++++++

Models are classes that are received from MyAnimeList and are not meant to be 
created by the user of the library.

.. danger:: 
    The classes listed below are not intended to be created by users and are 
    also read-only.

    .. TODO: Colocar hyperlink em Anime

    For example, this means that you should not make your own Anime instances 
    nor should you modify the Anime instance yourself.

AlternativeTitles
-----------------
.. _AlternativeTitles:

.. class:: models.alternativeTitles.AlternativeTitles(synonyms, english, japanese)

.. list-table::
    :widths: 10
    :header-rows: 1

    * - Methods
    * - :ref:`getSynonyms <getSynonyms>`
    * - :ref:`getEnglish <getEnglish>`
    * - :ref:`getJapanese <getJapanese>`

**Parameters:**
    - synonyms (`List <https://docs.python.org/3/library/stdtypes.html#list>`_ [`str <https://docs.python.org/3/library/stdtypes.html#str>`_]) - A list of title synonyms.
    - english (`str <https://docs.python.org/3/library/stdtypes.html#str>`_) - English version of the title.
    - japanese (`str <https://docs.python.org/3/library/stdtypes.html#str>`_) - Japanese version of the title.

Methods
~~~~~~~

.. method:: getSynonyms()
.. _getSynonyms:

    List of synonyms.

    **Return type:**
        `List <https://docs.python.org/3/library/stdtypes.html#list>`_ [`str <https://docs.python.org/3/library/stdtypes.html#str>`_]

.. method:: getEnglish()
.. _getEnglish:

    English version.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: getJapanese()
.. _getJapanese:

    Japanese version.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

Anime
-----
.. _Anime:

.. class:: Anime(node, fields)

.. list-table::
    :widths: 10 10
    :header-rows: 1

    * - Methods
      - Methods
    * - :ref:`getAlternativeTitle <getAlternativeTitle>`
      - :ref:`getStartDate <getStartDate>`
    * - :ref:`getEndDate <getEndDate>`
      - :ref:`getSynopsis <getSynopsis>`
    * - :ref:`getMean <getMean>`
      - :ref:`getRank <getRank>`
    * - :ref:`getPopularity <getPopularity>`
      - :ref:`getNumUserList <getNumUserList>`
    * - :ref:`getNumScoringUsers <getNumScoringUsers>`
      - :ref:`getNsfwClassification <getNsfwClassification>`
    * - :ref:`getGenres <getGenres>`
      - :ref:`getCreatedAt <getCreatedAt>`
    * - :ref:`getUpdatedAt <getUpdatedAt>`
      - :ref:`getMediaType <getMediaType>`
    * - :ref:`getStatus <getStatus>`
      - :ref:`getNumEpisodes <getNumEpisodes>`
    * - :ref:`getStartSeason <getStartSeason>`
      - :ref:`getBroadcast <getBroadcast>`
    * - :ref:`getSource <getSource>`
      - :ref:`getAvgEpisodeDurationInSeconds <getAvgEpisodeDurationInSeconds>`
    * - :ref:`getRating <getRating>`
      - :ref:`getStudios <getStudios>`
    * - :ref:`getPictures <getPictures>`
      - :ref:`getBackground <getBackground>`
    * - :ref:`getRelatedAnimes <getRelatedAnimes>`
      - :ref:`getRelatedMangas <getRelatedMangas>`
    * - :ref:`getRecommendations <getRecommendations>`
      - :ref:`getStatistics <getStatistics>`

**Parameters:**
    - node (`dict <https://docs.python.org/3/library/stdtypes.html#dict>`_) - The JSON object anime.
    - fields (`List <https://docs.python.org/3/library/stdtypes.html#list>`_ [`str <https://docs.python.org/3/library/stdtypes.html#str>`_]) - The fields used for the request.

Methods
~~~~~~~

.. method:: getAlternativeTitle()
.. _getAlternativeTitle:

    The alternative title of the anime.

    **Return type:**
        :ref:`AlternativeTitles <AlternativeTitles>`

.. method:: getStartDate()
.. _getStartDate:

    The anime start date. Format ``YYYY-mm-dd``.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: getEndDate()
.. _getEndDate:

    The anime end date. Format ``YYYY-mm-dd``.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: getSynopsis()
.. _getSynopsis:

    Anime synopsis.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: getMean()
.. _getMean:

    Mean score.

    **Return type:**
        `float <https://docs.python.org/3/library/functions.html#float>`_

.. method:: getRank()
.. _getRank:

    Anime rank.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: getPopularity()
.. _getPopularity:

    Anime popularity.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: getNumUserList()
.. _getNumUserList:

    The number of users who have the anime in their list.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: getNumScoringUsers()
.. _getNumScoringUsers:

    The number of users who rated the anime.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: getNsfwClassification()
.. _getNsfwClassification:

    Anime NSFW classification.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: getGenres()
.. _getGenres:

    The list of anime genres.

    **Return type:**
        `List <https://docs.python.org/3/library/stdtypes.html#list>`_ [Genre]
        .. TODO: Colocar hyperlink genre.

.. method:: getCreatedAt()
.. _getCreatedAt:

    Timestamp of anime creation in MyAnimeList database.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: getUpdatedAt()
.. _getUpdatedAt:

    Timestamp of anime update in MyAnimeList database.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: getMediaType()
.. _getMediaType:

    Anime media type.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: getStatus()
.. _getStatus:

    Airing status.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: getNumEpisodes()
.. _getNumEpisodes:

    The total number of episodes of this series. If unknown, it is 0.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: getStartSeason()
.. _getStartSeason:

    Anime start season.

    **Return type:**
        Season
        .. TODO: colocar hyperlink de Season

.. method:: getBroadcast()
.. _getBroadcast:

    Broadcast day of the week and start time (JST).

    **Return type:**
        Broadcast | `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_
        .. TODO: colocar hyperlink de Broadcast

.. method:: getSource()
.. _getSource:

    Original work.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: getAvgEpisodeDurationInSeconds()
.. _getAvgEpisodeDurationInSeconds:

    Average length of episode in seconds.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: getRating()
.. _getRating:

    Anime rating.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: getStudios()
.. _getStudios:

    List of studios that produced the anime.

    **Return type:**
        `List <https://docs.python.org/3/library/stdtypes.html#list>`_ [Studio]
        .. TODO: Colocar hyperlink Studio.

.. method:: getPictures()
.. _getPictures:

    List of anime pictures.

    .. important:: You cannot contain this field in a list.

    **Return type:**
        `List <https://docs.python.org/3/library/stdtypes.html#list>`_ [Picture] | `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_
        .. TODO: Colocar hyperlink Picture.

.. method:: getBackground()
.. _getBackground:

    The API strips BBCode tags from the result.

    .. important:: You cannot contain this field in a list.

    **Return type:**
        `List <https://docs.python.org/3/library/stdtypes.html#list>`_ [`str <https://docs.python.org/3/library/stdtypes.html#str>`_] | `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

.. method:: getRelatedAnimes()
.. _getRelatedAnimes:

    List of related animes.

    .. important:: You cannot contain this field in a list.

    **Return type:**
        `List <https://docs.python.org/3/library/stdtypes.html#list>`_ [RelatedNode] | `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_
        .. TODO: Colocar hyperlink RelatedNode.

.. method:: getRelatedMangas()
.. _getRelatedMangas:

    List of related mangas.

    .. important:: You cannot contain this field in a list.

    **Return type:**
        `List <https://docs.python.org/3/library/stdtypes.html#list>`_ [RelatedNode] | `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_
        .. TODO: Colocar hyperlink RelatedNode.

.. method:: getRecommendations()
.. _getRecommendations:

    Summary of recommended anime for those who like this anime.

    .. important:: You cannot contain this field in a list.

    **Return type:**
        `List <https://docs.python.org/3/library/stdtypes.html#list>`_ [Recommendation] | `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_
        .. TODO: Colocar hyperlink Recommendation.

.. method:: getStatistics()
.. _getStatistics:

    Anime statistics on MyAnimeList.

    .. important:: You cannot contain this field in a list.

    **Return type:**
        `List <https://docs.python.org/3/library/stdtypes.html#list>`_ [Statistics] | `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_
        .. TODO: Colocar hyperlink Statistics.

Title
-----

.. class:: models.

.. list-table::
    :widths: 10
    :header-rows: 1

    * - Methods
    * - :ref:` <>`

**Parameters:**
    -  () - 
    -  () - 

Methods
~~~~~~~

.. method:: ()
.. _:

    

    **Return type:**
        ` <>`_