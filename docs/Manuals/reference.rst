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

.. method:: get_anime_list(anime_name, limit = 100, offset = 0, fields = [])
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

.. method:: get_anime_list_in_dict(anime_name, limit = 100, offset = 0, fields = [])
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

.. method:: get_anime_list_in_json(anime_name, limit = 100, offset = 0, fields = [])
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

.. method:: services.validate_fields(fields)
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
    * - :ref:`get_synonyms() <get_synonyms>`
    * - :ref:`get_english() <get_english>`
    * - :ref:`get_japanese() <get_japanese>`

**Parameters:**
    - synonyms (`List <https://docs.python.org/3/library/stdtypes.html#list>`_ [`str <https://docs.python.org/3/library/stdtypes.html#str>`_]) - A list of title synonyms.
    - english (`str <https://docs.python.org/3/library/stdtypes.html#str>`_) - English version of the title.
    - japanese (`str <https://docs.python.org/3/library/stdtypes.html#str>`_) - Japanese version of the title.

Methods
~~~~~~~

.. method:: get_synonyms()
.. _getSynonyms:

    List of synonyms.

    **Return type:**
        `List <https://docs.python.org/3/library/stdtypes.html#list>`_ [`str <https://docs.python.org/3/library/stdtypes.html#str>`_]

.. method:: get_english()
.. _getEnglish:

    English version.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: get_japanese()
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
    * - :ref:`get_id() <getIdAnime>`
      - :ref:`get_title() <getTitleAnime>`
    * - :ref:`get_main_picture <getMainPictureAnime>`
      - :ref:`get_start_date() <get_start_date>`
    * - :ref:`get_alternative_title() <get_alternative_title>`
      - :ref:`get_synopsis() <get_synopsis>`
    * - :ref:`get_end_date() <get_end_date>`
      - :ref:`get_rank() <get_rank>`
    * - :ref:`get_mean_score() <get_mean_score>`
      - :ref:`get_num_user_list() <get_num_user_list>`
    * - :ref:`get_popularity() <get_popularity>`
      - :ref:`get_nsfw_classification() <get_nsfw_classification>`
    * - :ref:`get_num_scoring_users() <get_num_scoring_users>`
      - :ref:`get_created_at() <get_created_at>`
    * - :ref:`get_genres() <get_genres>`
      - :ref:`get_media_type() <get_media_type>`
    * - :ref:`get_updated_at() <get_updated_at>`
      - :ref:`get_num_episodes() <get_num_episodes>`
    * - :ref:`get_status() <get_status>`
      - :ref:`get_broadcast() <get_broadcast>`
    * - :ref:`get_start_season() <get_start_season>`
      - :ref:`get_avg_episode_duration_in_seconds() <get_avg_episode_duration_in_seconds>`
    * - :ref:`get_source() <get_source>`
      - :ref:`get_studios() <get_studios>`
    * - :ref:`get_rating() <get_rating>`
      - :ref:`get_background() <get_background>`
    * - :ref:`get_pictures() <get_pictures>`
      - :ref:`get_related_mangas() <get_related_mangas>`
    * - :ref:`get_related_animes() <get_related_animes>`
      - :ref:`get_statistics() <get_statistics>`
    * - :ref:`get_recommendations() <get_recommendations>`
      - 

**Parameters:**
    - node (`dict <https://docs.python.org/3/library/stdtypes.html#dict>`_) - The JSON object anime.
    - fields (`List <https://docs.python.org/3/library/stdtypes.html#list>`_ [`str <https://docs.python.org/3/library/stdtypes.html#str>`_]) - The fields used for the request.

Methods
~~~~~~~

.. method:: get_id()
    :noindex:
.. _getIdAnime:

    Anime ID.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: get_title()
    :noindex:
.. _getTitleAnime:

    Anime title.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: get_main_picture()
    :noindex:
.. _getMainPictureAnime:

    Anime main picture.

    **Return type:**
        :ref:`Picture <picture>`

.. method:: get_alternative_title()
.. _getAlternativeTitle:

    The alternative title of the anime.

    **Return type:**
        :ref:`AlternativeTitles <AlternativeTitles>`

.. method:: get_start_date()
.. _getStartDate:

    The anime start date. Format ``YYYY-mm-dd``.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: get_end_date()
.. _getEndDate:

    The anime end date. Format ``YYYY-mm-dd``.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: get_synopsis()
.. _getSynopsis:

    Anime synopsis.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: get_mean_score()
.. _getMean:

    Mean score.

    **Return type:**
        `float <https://docs.python.org/3/library/functions.html#float>`_

.. method:: get_rank()
.. _getRank:

    Anime rank.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: get_popularity()
.. _getPopularity:

    Anime popularity.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: get_num_user_list()
.. _getNumUserList:

    The number of users who have the anime in their list.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: get_num_scoring_users()
.. _getNumScoringUsers:

    The number of users who rated the anime.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: get_nsfw_classification()
.. _getNsfwClassification:

    Anime NSFW classification.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: get_genres()
.. _getGenres:

    The list of anime genres.

    **Return type:**
        `List <https://docs.python.org/3/library/stdtypes.html#list>`_ [:ref:`Genre <genre>`]

.. method:: get_created_at()
.. _getCreatedAt:

    Timestamp of anime creation in MyAnimeList database.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: get_updated_at()
.. _getUpdatedAt:

    Timestamp of anime update in MyAnimeList database.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: get_media_type()
.. _getMediaType:

    Anime media type.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: get_status()
.. _getStatus:

    Airing status.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: get_num_episodes()
.. _getNumEpisodes:

    The total number of episodes of this series. If unknown, it is 0.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: get_start_season()
.. _getStartSeason:

    Anime start season.

    **Return type:**
        :ref:`Season <Season>`

.. method:: get_broadcast()
.. _getBroadcast:

    Broadcast day of the week and start time (JST).

    **Return type:**
        :ref:`Broadcast <broadcast>` | `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

.. method:: get_source()
.. _getSource:

    Original work.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: get_avg_episode_duration_in_seconds()
.. _getAvgEpisodeDurationInSeconds:

    Average length of episode in seconds.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: get_rating()
.. _getRating:

    Anime rating.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: get_studios()
.. _getStudios:

    List of studios that produced the anime.

    **Return type:**
        `List <https://docs.python.org/3/library/stdtypes.html#list>`_ [:ref:`Studio <studio>`]

.. method:: get_pictures()
.. _getPictures:

    List of anime pictures.

    .. important:: You cannot contain this field in a list.

    **Return type:**
        `List <https://docs.python.org/3/library/stdtypes.html#list>`_ [:ref:`Picture <picture>`] | `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

.. method:: get_background()
.. _getBackground:

    The API strips BBCode tags from the result.

    .. important:: You cannot contain this field in a list.

    **Return type:**
        `List <https://docs.python.org/3/library/stdtypes.html#list>`_ [`str <https://docs.python.org/3/library/stdtypes.html#str>`_] | `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

.. method:: get_related_animes()
.. _getRelatedAnimes:

    List of related animes.

    .. important:: You cannot contain this field in a list.

    **Return type:**
        `List <https://docs.python.org/3/library/stdtypes.html#list>`_ [:ref:`RelatedNode <relatedNode>`] | `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

.. method:: get_related_mangas()
.. _getRelatedMangas:

    List of related mangas.

    .. important:: You cannot contain this field in a list.

    **Return type:**
        `List <https://docs.python.org/3/library/stdtypes.html#list>`_ [:ref:`RelatedNode <relatedNode>`] | `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

.. method:: get_recommendations()
.. _getRecommendations:

    Summary of recommended anime for those who like this anime.

    .. important:: You cannot contain this field in a list.

    **Return type:**
        `List <https://docs.python.org/3/library/stdtypes.html#list>`_ [:ref:`Recommendation <recommendation>`] | `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

.. method:: get_statistics()
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
    * - :ref:`get_day_of_the_week() <get_day_of_the_week>`
    * - :ref:`get_start_time() <get_start_time>`

**Parameters:**
    - day_of_the_week (:ref:`DayWeekEnum <dayWeekEnum>`) - Day of the week broadcast in Japan time.
    - start_time (`str <https://docs.python.org/3/library/stdtypes.html#str>`_) - Time in hours format that is broadcasted.
    
Methods
~~~~~~~

.. method:: get_day_of_the_week()
.. _getDayOfTheWeek:

    Broadcast day of the week.    

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: get_start_time()
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
    * - :ref:`get_id() <getIdGenre>`
    * - :ref:`get_name() <getNameGenre>`

**Parameters:**
    - id (`int <https://docs.python.org/3/library/functions.html#int>`_) - ID of the genre.
    - name (`str <https://docs.python.org/3/library/stdtypes.html#str>`_) - Name of the genre.

Methods
~~~~~~~

.. method:: get_id()
.. _getIdGenre:

    Genre ID.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: get_name()
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
    * - :ref:`get_id() <getIdNode>`
    * - :ref:`get_title() <get_title>`
    * - :ref:`get_main_picture() <get_main_picture>`

**Parameters:**
    - id (`int <https://docs.python.org/3/library/functions.html#int>`_) - 
    - title (`str <https://docs.python.org/3/library/stdtypes.html#str>`_) - 
    - main_picture () - 

Methods
~~~~~~~

.. method:: get_id()
    :noindex:
.. _getIdNode:

    Anime or manga ID.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: get_title()
.. _getTitle:

    Anime or manga title.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: get_main_picture()
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
    * - :ref:`get_large() <get_large>`
    * - :ref:`get_medium() <get_medium>`

**Parameters:**
    - large (`str <https://docs.python.org/3/library/stdtypes.html#str>`_) - The URI of an anime's large picture.
    - medium (`str <https://docs.python.org/3/library/stdtypes.html#str>`_) - The URI of an anime's medium picture.

Methods
~~~~~~~

.. method:: get_large()
.. _getLarge:

    Large size picture.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: get_medium()
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
    * - :ref:`get_id() <getIdRecommendation>`
    * - :ref:`get_title() <getTitleRecommendation>`
    * - :ref:`get_main_picture() <getMainPictureRecommendation>`
    * - :ref:`get_num_recommendations() <get_num_recommendations>`

**Parameters:**
    - id (`int <https://docs.python.org/3/library/functions.html#int>`_) - ID of the anime.
    - title (`str <https://docs.python.org/3/library/stdtypes.html#str>`_) - Title of the anime.
    - main_picture (:ref:`Picture <picture>`) -  Main picture of the anime.
    - num_recommendations (`int <https://docs.python.org/3/library/functions.html#int>`_) - Number of recommendations of the anime.

Methods
~~~~~~~

.. method:: get_id()
    :noindex:
.. _getIdRecommendation:

    Anime ID.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: get_title()
    :noindex:
.. _getTitleRecommendation:

    Anime title.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: get_main_picture()
    :noindex:
.. _getMainPictureRecommendation:

    Anime main picture.

    **Return type:**
        :ref:`Picture <picture>`

.. method:: get_num_recommendations()
.. _getNumRecommendations:

    Number of recommendations.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

RelatedNode
-----------
.. _RelatedNode:

.. class:: models.relatedNode.RelatedNode(id, title, main_picture, relation_type)

.. list-table::
    :widths: 10
    :header-rows: 1

    * - Methods
    * - :ref:`get_id() <getIdRelatedNode>`
    * - :ref:`get_title() <getTitleRelatedNode>`
    * - :ref:`get_main_picture() <getMainPictureRelatedNode>`
    * - :ref:`get_relation_type() <get_relation_type>`

**Parameters:**
    - id (`int <https://docs.python.org/3/library/functions.html#int>`_) - ID of the anime or manga.
    - title (`str <https://docs.python.org/3/library/stdtypes.html#str>`_) - Title of the anime or manga.
    - main_picture (:ref:`Picture <picture>`) - Main picture of the anime or manga.
    - relation_type (:ref:`RelationTypeEnum <RelationTypeEnum>`) - Relation type of the anime or manga.

Methods
~~~~~~~

.. method:: get_id()
    :noindex:
.. _getIdRelatedNode:

    Anime or manga ID.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: get_title()
    :noindex:
.. _getTitleRelatedNode:

    Anime or manga title.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

.. method:: get_main_picture()
    :noindex:
.. _getMainPictureRelatedNode:

    Anime or manga main picture.

    **Return type:**
        :ref:`Picture <picture>`

.. method:: get_relation_type()
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
    * - :ref:`get_year() <get_year>`
    * - :ref:`get_season() <get_season>`


**Parameters:**
    - year (`int <https://docs.python.org/3/library/functions.html#int>`_) - Year of season.
    - season (:ref:`SeasonEnum <SeasonEnum>`) - Season name.

Methods
~~~~~~~

.. method:: get_year()
.. _getYear:

    Year of season.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: get_season()
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
    * - :ref:`get_status() <getStatusStatistics>`


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

.. method:: get_status()
    :noindex:
.. _getStatusStatistics:

    Anime status in the users list.

    **Return type:**
        :ref:`StatisticsStatus <StatisticsStatus>`

StatisticsStatus
----------------
.. _StatisticsStatus:

.. class:: models.statisticsStatus.StatisticsStatus(watching, completed, on_hold, dropped, plan_to_watch)

.. list-table::
    :widths: 10
    :header-rows: 1

    * - Methods
    * - :ref:`get_num_watching() <get_num_watching>`
    * - :ref:`get_num_completed() <get_num_completed>`
    * - :ref:`get_num_on_hold() <get_num_on_hold>`
    * - :ref:`get_num_dropped() <get_num_dropped>`
    * - :ref:`get_num_plan_to_watch() <get_num_plan_to_watch>`


**Parameters:**
    - watching (`int <https://docs.python.org/3/library/functions.html#int>`_) - Number of users who are watching.
    - completed (`int <https://docs.python.org/3/library/functions.html#int>`_) - Number of users who completed.
    - on_hold (`int <https://docs.python.org/3/library/functions.html#int>`_) - Number of users who are on hold.
    - dropped (`int <https://docs.python.org/3/library/functions.html#int>`_) - Number of users who dropped.
    - plan_to_watch (`int <https://docs.python.org/3/library/functions.html#int>`_) - Number of users who are plan to watch.

Methods
~~~~~~~

.. method:: get_num_watching()
.. _getNumWatching:

    The number of users who are watching the anime.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: get_num_completed()
.. _getNumCompleted:

    The number of users who are completed the anime.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: get_num_on_hold()
.. _getNumOnHold:

    The number of users who are waiting for the anime.


    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: get_num_dropped()
.. _getNumDropped:

    The number of users who are dropped the anime.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: get_num_plan_to_watch()
.. _getNumPlanToWatch:

    The number of users who plan to watch the anime.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

Studio
------
.. _Studio:

.. class:: models.studio.Studio(id, name)

.. list-table::
    :widths: 10
    :header-rows: 1

    * - Methods
    * - :ref:`get_id() <getIdStudio>`
    * - :ref:`get_name() <getNameStudio>`


**Parameters:**
    - id (`int <https://docs.python.org/3/library/functions.html#int>`_) - ID of the Anime Studio.
    - name (`str <https://docs.python.org/3/library/stdtypes.html#str>`_) - Name of the Anime Studio.

Methods
~~~~~~~

.. method:: get_id()
    :noindex:
.. _getIdStudio:

    Studio ID.

    **Return type:**
        `int <https://docs.python.org/3/library/functions.html#int>`_

.. method:: get_name()
    :noindex:
.. _getNameStudio:

    Studio name.

    **Return type:**
        `str <https://docs.python.org/3/library/stdtypes.html#str>`_

Enumerations
++++++++++++

The library provides some enumerations to avoid the API from being stringly 
typed in case the strings change in the future.

All enumerations are subclasses of `enum.Enum <https://docs.python.org/3/library/enum.html#enum.Enum>`_.

.. warning:: 
    The enumerations listed below are not intended to be used by users and are 
    also read-only.

AiringStatusEnum
----------------
.. _AiringStatusEnum:

.. c:enum:: enums.airingStatusEnum.AiringStatusEnum

.. list-table::
    :widths: 10 10
    :header-rows: 1

    * - Key
      - Value
    * - finished_airing
      - Finished airing
    * - currently_airing
      - Currently airing
    * - not_yet_aired
      - Not yet aired

DayWeekEnum
-----------
.. _DayWeekEnum:

.. c:enum:: enums.dayWeekEnum.DayWeekEnum

.. list-table::
    :widths: 10 10
    :header-rows: 1

    * - Key
      - Value
    * - sunday
      - 0
    * - monday
      - 1
    * - tuesday
      - 2
    * - wednesday
      - 3
    * - thursday
      - 4
    * - friday
      - 5
    * - saturday
      - 6

FieldsEnum
----------
.. _FieldsEnum:

.. c:enum:: enums.fieldsEnum.FieldsEnum

.. list-table::
    :widths: 10 10 10 10
    :header-rows: 1

    * - Key
      - Value
      - Key
      - Value
    * - id
      - 0
      - media_type
      - 16
    * - title
      - 1
      - status
      - 17
    * - main_picture
      - 2
      - num_episodes
      - 18
    * - alternative_title
      - 3
      - start_season
      - 19
    * - start_date
      - 4
      - broadcast
      - 20
    * - end_date
      - 5
      - source
      - 21
    * - synopsis
      - 6
      - average_episode_duration
      - 22
    * - mean
      - 7
      - rating
      - 23
    * - rank
      - 8
      - studios
      - 24
    * - popularity
      - 9
      - pictures
      - 25
    * - num_list_users
      - 10
      - background
      - 26
    * - num_scoring_users
      - 11
      - related_anime
      - 27
    * - nsfw
      - 12
      - related_manga
      - 28
    * - genres
      - 13
      - recommendations
      - 29
    * - created_at
      - 14
      - statistics
      - 30
    * - updated_at
      - 15
      -
      -

.. note:: 
    The keys ``pictures``, ``background``, ``related_anime``, ``related_manga``, 
    ``recommendations``, and ``statistics`` cannot be in the **fields** parameter of
    :ref:`get_anime_list() <getAnimeList>`, :ref:`get_anime_list_in_dict() <getAnimeListInDict>` and 
    :ref:`get_anime_list_in_json() <getAnimeListInJSON>` methods.


MediaTypeEnum
-------------
.. _MediaTypeEnum:

.. c:enum:: enums.mediaTypeEnum.MediaTypeEnum

.. list-table::
    :widths: 10 10
    :header-rows: 1

    * - Key
      - Value
    * - unknown
      - 0
    * - tv
      - 1
    * - ova
      - 2
    * - movie
      - 3
    * - special
      - 4
    * - ona
      - 5
    * - music
      - 6

NsfwEnum
--------
.. _NsfwEnum:

.. c:enum:: enums.nsfwEnum.NsfwEnum

.. list-table::
    :widths: 3 10
    :header-rows: 1

    * - Key
      - Value
    * - white
      - This work is safe for work
    * - gray
      - This work may be not safe for work
    * - black
      - This work is not safe for work

RatingEnum
----------
.. _RatingEnum:

.. c:enum:: enums.ratingEnum.RatingEnum

.. list-table::
    :widths: 3 10
    :header-rows: 1

    * - Key
      - Value
    * - g
      - All Age
    * - pg
      - Children
    * - pg_13
      - Teens 13 and Older
    * - r
      - 17+ (violence & profanity)
    * - r_plus
      - Profanity & Mild Nudity
    * - rx
      - Hentai

RelationTypeEnum
----------------
.. _RelationTypeEnum:

.. c:enum:: enums.relationTypeEnum.RelationTypeEnum

.. list-table::
    :widths: 10 10
    :header-rows: 1

    * - Key
      - Value
    * - sequel
      - Sequel
    * - prequel
      - Prequel
    * - alternative_setting
      - Alternative Setting
    * - alternative_version
      - Alternative Version
    * - side_story
      - Side Story
    * - parent_story
      - Parent Story
    * - summary
      - Summary
    * - full_story
      - Full Story

SeasonEnum
----------
.. _SeasonEnum:

.. c:enum:: enums.seasonEnum.SeasonEnum

.. list-table::
    :widths: 10 10
    :header-rows: 1

    * - Key
      - Value
    * - winter
      - Winter
    * - spring
      - Spring
    * - summer
      - Summer
    * - fall
      - Fall

SourceEnum
----------
.. _SourceEnum:

.. c:enum:: enums.sourceEnum.SourceEnum

.. list-table::
    :widths: 10 10
    :header-rows: 1

    * - Key
      - Value
    * - other
      - Other
    * - original
      - Original
    * - manga
      - Manga
    * - four_koma_manga
      - 4 Koma manga
    * - web_manga
      - Web manga
    * - digital_manga
      - Digital manga
    * - novel
      - Novel
    * - light_novel
      - Light novel
    * - visual_novel
      - Visual novel
    * - game
      - Game
    * - card_game
      - Card game
    * - book
      - Book
    * - picture_book
      - Picture book
    * - radio
      - Radio
    * - music
      - Music