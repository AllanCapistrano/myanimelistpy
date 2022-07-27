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
        `List <https://docs.python.org/3/library/stdtypes.html#list>`_ [:ref:`Anime <anime>`]

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

    For example, this means that you should not make your own :ref:`Anime <anime>` instances 
    nor should you modify the :ref:`Anime <anime>` instance yourself.

AlternativeTitles
-----------------
.. _AlternativeTitles:

.. class:: models.alternativeTitles.AlternativeTitles(synonyms, english, japanese)

.. list-table::
    :widths: 10
    :header-rows: 1

    * - Methods
    * - :ref:`getSynonyms() <getSynonyms>`
    * - :ref:`getEnglish() <getEnglish>`
    * - :ref:`getJapanese() <getJapanese>`

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

.. class:: models.anime.Anime(node, fields)

.. list-table::
    :widths: 10 10
    :header-rows: 1

    * - Methods
      - Methods
    * - :ref:`getId() <getIdAnime>`
      - :ref:`getTitle() <getTitleAnime>`
    * - :ref:`getMainPicture <getMainPictureAnime>`
      - :ref:`getStartDate() <getStartDate>`
    * - :ref:`getAlternativeTitle() <getAlternativeTitle>`
      - :ref:`getSynopsis() <getSynopsis>`
    * - :ref:`getEndDate() <getEndDate>`
      - :ref:`getRank() <getRank>`
    * - :ref:`getMean() <getMean>`
      - :ref:`getNumUserList() <getNumUserList>`
    * - :ref:`getPopularity() <getPopularity>`
      - :ref:`getNsfwClassification() <getNsfwClassification>`
    * - :ref:`getNumScoringUsers() <getNumScoringUsers>`
      - :ref:`getCreatedAt() <getCreatedAt>`
    * - :ref:`getGenres() <getGenres>`
      - :ref:`getMediaType() <getMediaType>`
    * - :ref:`getUpdatedAt() <getUpdatedAt>`
      - :ref:`getNumEpisodes() <getNumEpisodes>`
    * - :ref:`getStatus() <getStatus>`
      - :ref:`getBroadcast() <getBroadcast>`
    * - :ref:`getStartSeason() <getStartSeason>`
      - :ref:`getAvgEpisodeDurationInSeconds() <getAvgEpisodeDurationInSeconds>`
    * - :ref:`getSource() <getSource>`
      - :ref:`getStudios() <getStudios>`
    * - :ref:`getRating() <getRating>`
      - :ref:`getBackground() <getBackground>`
    * - :ref:`getPictures() <getPictures>`
      - :ref:`getRelatedMangas() <getRelatedMangas>`
    * - :ref:`getRelatedAnimes() <getRelatedAnimes>`
      - :ref:`getStatistics() <getStatistics>`
    * - :ref:`getRecommendations() <getRecommendations>`
      - 

**Parameters:**
    - node (`dict <https://docs.python.org/3/library/stdtypes.html#dict>`_) - The JSON object anime.
    - fields (`List <https://docs.python.org/3/library/stdtypes.html#list>`_ [`str <https://docs.python.org/3/library/stdtypes.html#str>`_]) - The fields used for the request.

Methods
~~~~~~~

.. method:: getId()
    :noindex:
.. _getIdAnime:

    Anime ID.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: getTitle()
    :noindex:
.. _getTitleAnime:

    Anime title.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: getMainPicture()
    :noindex:
.. _getMainPictureAnime:

    Anime main picture.

    **Return type:**
        :ref:`Picture <picture>`

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
        `List <https://docs.python.org/3/library/stdtypes.html#list>`_ [:ref:`Genre <genre>`]

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
        :ref:`Season <Season>`

.. method:: getBroadcast()
.. _getBroadcast:

    Broadcast day of the week and start time (JST).

    **Return type:**
        :ref:`Broadcast <broadcast>` | `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

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
        `List <https://docs.python.org/3/library/stdtypes.html#list>`_ [:ref:`Studio <studio>`]

.. method:: getPictures()
.. _getPictures:

    List of anime pictures.

    .. important:: You cannot contain this field in a list.

    **Return type:**
        `List <https://docs.python.org/3/library/stdtypes.html#list>`_ [:ref:`Picture <picture>`] | `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

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
        `List <https://docs.python.org/3/library/stdtypes.html#list>`_ [:ref:`RelatedNode <relatedNode>`] | `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

.. method:: getRelatedMangas()
.. _getRelatedMangas:

    List of related mangas.

    .. important:: You cannot contain this field in a list.

    **Return type:**
        `List <https://docs.python.org/3/library/stdtypes.html#list>`_ [:ref:`RelatedNode <relatedNode>`] | `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

.. method:: getRecommendations()
.. _getRecommendations:

    Summary of recommended anime for those who like this anime.

    .. important:: You cannot contain this field in a list.

    **Return type:**
        `List <https://docs.python.org/3/library/stdtypes.html#list>`_ [:ref:`Recommendation <recommendation>`] | `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

.. method:: getStatistics()
.. _getStatistics:

    Anime statistics on MyAnimeList.

    .. important:: You cannot contain this field in a list.

    **Return type:**
        `List <https://docs.python.org/3/library/stdtypes.html#list>`_ [:ref:`Statistics <statistics>`] | `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

Broadcast
---------

.. class:: models.broadcast.Broadcast(day_of_the_week, start_time)
.. _Broadcast:

.. list-table::
    :widths: 10
    :header-rows: 1

    * - Methods
    * - :ref:`getDayOfTheWeek() <getDayOfTheWeek>`
    * - :ref:`getStartTime() <getStartTime>`

**Parameters:**
    - day_of_the_week (:ref:`DayWeekEnum <dayWeekEnum>`) - Day of the week broadcast in Japan time.
    - start_time (`str <https://docs.python.org/3/library/stdtypes.html#str>`_) - Time in hours format that is broadcasted.
    
Methods
~~~~~~~

.. method:: getDayOfTheWeek()
.. _getDayOfTheWeek:

    Broadcast day of the week.    

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: getStartTime()
.. _getStartTime:

    Anime start time in JST.

     **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

Genre
-----
.. _Genre:

.. class:: models.genre.Genre(id, name)

.. list-table::
    :widths: 10
    :header-rows: 1

    * - Methods
    * - :ref:`getId() <getIdGenre>`
    * - :ref:`getName() <getNameGenre>`

**Parameters:**
    - id (`int <https://docs.python.org/3/library/functions.html#int>`_) - ID of the genre.
    - name (`str <https://docs.python.org/3/library/stdtypes.html#str>`_) - Name of the genre.

Methods
~~~~~~~

.. method:: getId()
.. _getIdGenre:

    Genre ID.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: getName()
.. _getNameGenre:

    Genre name.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

Node
----
.. _Node:

.. class:: models.node.Node(id, title, main_picture)

.. list-table::
    :widths: 10
    :header-rows: 1

    * - Methods
    * - :ref:`getId() <getIdNode>`
    * - :ref:`getTitle() <getTitle>`
    * - :ref:`getMainPicture() <getMainPicture>`

**Parameters:**
    - id (`int <https://docs.python.org/3/library/functions.html#int>`_) - 
    - title (`str <https://docs.python.org/3/library/stdtypes.html#str>`_) - 
    - main_picture () - 

Methods
~~~~~~~

.. method:: getId()
    :noindex:
.. _getIdNode:

    Anime or manga ID.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: getTitle()
.. _getTitle:

    Anime or manga title.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: getMainPicture()
.. _getMainPicture:

    Anime or manga main picture.

    **Return type:**
        :ref:`Picture <picture>`

Picture
-------
.. _Picture:

.. class:: models.picture.Picture(large, medium)

.. list-table::
    :widths: 10
    :header-rows: 1

    * - Methods
    * - :ref:`getLarge() <getLarge>`
    * - :ref:`getMedium() <getMedium>`

**Parameters:**
    - large (`str <https://docs.python.org/3/library/stdtypes.html#str>`_) - The URI of an anime's large picture.
    - medium (`str <https://docs.python.org/3/library/stdtypes.html#str>`_) - The URI of an anime's medium picture.

Methods
~~~~~~~

.. method:: getLarge()
.. _getLarge:

    Large size picture.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: getMedium()
.. _getMedium:

    Medium size picture.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

Recommendation
--------------
.. _Recommendation:

.. class:: models.recommendation.Recommendation(id, title, main_picture, num_recommendations)

.. list-table::
    :widths: 10
    :header-rows: 1

    * - Methods
    * - :ref:`getId() <getIdRecommendation>`
    * - :ref:`getTitle() <getTitleRecommendation>`
    * - :ref:`getMainPicture() <getMainPictureRecommendation>`
    * - :ref:`getNumRecommendations() <getNumRecommendations>`

**Parameters:**
    - id (`int <https://docs.python.org/3/library/functions.html#int>`_) - ID of the anime.
    - title (`str <https://docs.python.org/3/library/stdtypes.html#str>`_) - Title of the anime.
    - main_picture (:ref:`Picture <picture>`) -  Main picture of the anime.
    - num_recommendations (`int <https://docs.python.org/3/library/functions.html#int>`_) - Number of recommendations of the anime.

Methods
~~~~~~~

.. method:: getId()
    :noindex:
.. _getIdRecommendation:

    Anime ID.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: getTitle()
    :noindex:
.. _getTitleRecommendation:

    Anime title.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: getMainPicture()
    :noindex:
.. _getMainPictureRecommendation:

    Anime main picture.

    **Return type:**
        :ref:`Picture <picture>`

.. method:: getNumRecommendations()
.. _getNumRecommendations:

    Number of recommendations.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

RelatedNode
-----
.. _RelatedNode:

.. class:: models.relatedNode.RelatedNode(id, title, main_picture, relation_type)

.. list-table::
    :widths: 10
    :header-rows: 1

    * - Methods
    * - :ref:`getId() <getIdRelatedNode>`
    * - :ref:`getTitle() <getTitleRelatedNode>`
    * - :ref:`getMainPicture() <getMainPictureRelatedNode>`
    * - :ref:`getRelationType() <getRelationType>`

**Parameters:**
    - id (`int <https://docs.python.org/3/library/functions.html#int>`_) - ID of the anime or manga.
    - title (`str <https://docs.python.org/3/library/stdtypes.html#str>`_) - Title of the anime or manga.
    - main_picture (:ref:`Picture <picture>`) - Main picture of the anime or manga.
    - relation_type (:ref:`RelationTypeEnum <RelationTypeEnum>`) - Relation type of the anime or manga.

Methods
~~~~~~~

.. method:: getId()
    :noindex:
.. _getIdRelatedNode:

    Anime or manga ID.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: getTitle()
    :noindex:
.. _getTitleRelatedNode:

    Anime or manga title.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: getMainPicture()
    :noindex:
.. _getMainPictureRelatedNode:

    Anime or manga main picture.

    **Return type:**
        :ref:`Picture <picture>`

.. method:: getRelationType()
.. _getRelationType:

    Anime or manga relation type.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

Season
------
.. _Season:

.. class:: models.season.Season(year, season)

.. list-table::
    :widths: 10
    :header-rows: 1

    * - Methods
    * - :ref:`getYear() <getYear>`
    * - :ref:`getSeason() <getSeason>`


**Parameters:**
    - year (`int <https://docs.python.org/3/library/functions.html#int>`_) - Year of season.
    - season (:ref:`SeasonEnum <SeasonEnum>`) - Season name.

Methods
~~~~~~~

.. method:: getYear()
.. _getYear:

    Year of season.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: getSeason()
.. _getSeason:

    Season name.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

Statistics
----------
.. _Statistics:

.. class:: models.statistics.Statistics(num_list_users, status)

.. list-table::
    :widths: 10
    :header-rows: 1

    * - Methods
    * - :ref:`getNumUserLis() <getNumUserLis>`
    * - :ref:`getStatus() <getStatusStatistics>`


**Parameters:**
    - num_list_users (`int <https://docs.python.org/3/library/functions.html#int>`_) - Number of users who added the anime to their list.
    - status (:ref:`StatisticsStatus <StatisticsStatus>`) - Users list status.

Methods
~~~~~~~

.. method:: getNumUserLis()
.. _getNumUserLis:

    The number of users who have the anime in their list.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: getStatus()
    :noindex:
.. _getStatusStatistics:

    Anime status in the users list.

    **Return type:**
        :ref:`StatisticsStatus <StatisticsStatus>`

StatisticsStatus
-----
.. _StatisticsStatus:

.. class:: models.statisticsStatus.StatisticsStatus(watching, completed, on_hold, dropped, plan_to_watch)

.. list-table::
    :widths: 10
    :header-rows: 1

    * - Methods
    * - :ref:`getNumWatching() <getNumWatching>`
    * - :ref:`getNumCompleted() <getNumCompleted>`
    * - :ref:`getNumOnHold() <getNumOnHold>`
    * - :ref:`getNumDropped() <getNumDropped>`
    * - :ref:`getNumPlanToWatch() <getNumPlanToWatch>`


**Parameters:**
    - watching (`int <https://docs.python.org/3/library/functions.html#int>`_) - Number of users who are watching.
    - completed (`int <https://docs.python.org/3/library/functions.html#int>`_) - Number of users who completed.
    - on_hold (`int <https://docs.python.org/3/library/functions.html#int>`_) - Number of users who are on hold.
    - dropped (`int <https://docs.python.org/3/library/functions.html#int>`_) - Number of users who dropped.
    - plan_to_watch (`int <https://docs.python.org/3/library/functions.html#int>`_) - Number of users who are plan to watch.

Methods
~~~~~~~

.. method:: getNumWatching()
.. _getNumWatching:

    The number of users who are watching the anime.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: getNumCompleted()
.. _getNumCompleted:

    The number of users who are completed the anime.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: getNumOnHold()
.. _getNumOnHold:

    The number of users who are waiting for the anime.


    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: getNumDropped()
.. _getNumDropped:

    The number of users who are dropped the anime.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: getNumPlanToWatch()
.. _getNumPlanToWatch:

    The number of users who plan to watch the anime.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

Title
-----
.. _Title:

.. class:: models.

.. list-table::
    :widths: 10
    :header-rows: 1

    * - Methods
    * - :ref:`() <>`


**Parameters:**
    -  () - 
    -  () - 

Methods
~~~~~~~

.. method:: ()
.. _:

    

    **Return type:**
        ` <>`_