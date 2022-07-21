from typing import List
from myanimelistpy.enums.dayWeekEnum import DayWeekEnum
from myanimelistpy.enums.relationTypeEnum import RelationTypeEnum

from myanimelistpy.enums.seasonEnum import SeasonEnum
from myanimelistpy.status import Status

from .node import Node
from .enums.nsfwEnum import NsfwEnum
from .picture import Picture
from .alternativeTitles import AlternativeTitles
from .genre import Genre
from .enums.mediaTypeEnum import MediaTypeEnum
from .enums.statusEnum import StatusEnum
from .season import Season
from .broadcast import Broadcast
from .enums.sourceEnum import SourceEnum
from .enums.ratingEnum import RatingEnum
from .animeStudio import AnimeStudio
from .relatedNode import RelatedNode
from .recommendation import Recommendation
from .statistics import Statistics

class Anime(Node):
    def __init__(
        self,
        node: dict,
        fields: List[str]
    ) -> None:
        """ Constructor.

        Parameters
        -----------
        node: :class:`dict`
            The JSON object anime.
        fields: :class:`List[str]`
            The fields used for the request.
        """

        super().__init__(
            id           = node["id"], 
            title        = node["title"], 
            main_picture = node["main_picture"]
        )

        self.alternative_titles       = None
        self.start_date               = None
        self.end_date                 = None
        self.synopsis                 = None
        self.mean                     = None
        self.rank                     = None
        self.popularity               = None
        self.num_list_users           = None
        self.num_scoring_users        = None
        self.nsfw                     = None
        self.genres                   = None
        self.created_at               = None
        self.updated_at               = None
        self.media_type               = None
        self.status                   = None
        self.num_episodes             = None
        self.start_season             = None
        self.broadcast                = None
        self.source                   = None
        self.average_episode_duration = None
        self.rating                   = None
        self.studios                  = None
        self.pictures                 = None # Cannot contain this field in a list.
        self.background               = None # Cannot contain this field in a list.
        self.related_anime            = None # Cannot contain this field in a list.
        self.related_manga            = None # Cannot contain this field in a list.
        self.recommendations          = None # Cannot contain this field in a list.
        self.statistics               = None # Cannot contain this field in a list.

        self.setFields(node=node, fields=fields)

    def setFields(self, node: dict, fields: List[str]) -> None:
        """ Set the class attributes values using the fields.

        Parameters
        -----------
        node: :class:`dict`
            The JSON 'node' object sent by the MyAnimeList API.
        fields: :class:`List[str]`
            The fields used in the request.
        """

        for field in fields:
            match field:
                case "alternative_titles":
                    alternative_titles: dict = node["alternative_titles"]

                    synonyms: List[str] = alternative_titles["synonyms"]
                    english: str        = alternative_titles["en"]
                    japanese: str       = alternative_titles["ja"]

                    self.alternative_titles = AlternativeTitles(
                        synonyms = synonyms,
                        english  = english,
                        japanese = japanese
                    )

                    pass
                case "start_date":
                    self.start_date: str = node["start_date"]

                    pass
                case "end_date":
                    self.end_date: str = node["end_date"]

                    pass
                case "synopsis":
                    self.synopsis: str = node["synopsis"]

                    pass
                case "mean":
                    self.mean: float = node["mean"]

                    pass
                case "rank":
                    self.rank: int = node["rank"]

                    pass
                case "popularity":
                    self.popularity: int = node["popularity"]

                    pass
                case "num_list_users":
                    self.num_list_users: int = node["num_list_users"]

                    pass
                case "num_scoring_users":
                    self.num_scoring_users: int = node["num_scoring_users"]

                    pass
                case "nsfw":
                    nsfw_type: str = node["nsfw"]

                    self.nsfw: NsfwEnum = NsfwEnum[nsfw_type]

                    pass
                case "genres":
                    genres_json: List[dict] = node["genres"]
                    genres: List[Genre]     = []

                    for genre in genres_json:
                        genres.append(Genre(id=genre["id"], name=genre["name"]))

                    self.genres: List[Genre] = genres

                    pass
                case "created_at":
                    self.created_at: str = node["created_at"]

                    pass
                case "updated_at":
                    self.updated_at: str = node["updated_at"]

                    pass
                case "media_type":
                    self.media_type: MediaTypeEnum = node["media_type"]

                    pass
                case "status":
                    status_type: str = node["status"]

                    self.status: StatusEnum = StatusEnum[status_type]

                    pass
                case "num_episodes":
                    self.num_episodes: int = node["num_episodes"]

                    pass
                case "start_season":
                    start_season: dict = node["start_season"]
                    season_type: str   = start_season["season"]

                    self.start_season: Season = Season(
                        year   = start_season["year"],
                        season = SeasonEnum[season_type]
                    )

                    pass
                case "broadcast":
                    try:
                        broadcast: dict    = node["broadcast"]
                        day_week_type: str = broadcast["day_of_the_week"]
                    
                        self.broadcast: Broadcast = Broadcast(
                            day_of_the_week = DayWeekEnum[day_week_type],
                            start_time      = broadcast["start_time"]
                        )
                    except:
                        self.broadcast = None

                    pass
                case "source":
                    source_type: str = node["source"]

                    self.source: SourceEnum = SourceEnum[source_type]

                    pass
                case "average_episode_duration":
                    self.average_episode_duration: int = node[
                        "average_episode_duration"
                    ]

                    pass
                case "rating":
                    rating_type: str = "r_plus" if node["rating"] == "r+" else node["rating"]

                    self.rating: RatingEnum = RatingEnum[rating_type]

                    pass
                case "studios":
                    studios_json: List[dict]   = node["studios"]
                    studios: List[AnimeStudio] = []

                    for studio in studios_json:
                        studios.append(
                            AnimeStudio(
                                id   = studio["id"], 
                                name = studio["name"]
                            )
                        )

                    self.studios: List[AnimeStudio] = studios

                    pass
                case "pictures":
                    try:
                        pictures_json: List[dict] = node["pictures"]
                        pictures: List[Picture] = []

                        for picture in pictures_json:
                            pictures.append(
                                Picture(
                                    medium = picture["medium"],
                                    large  = picture["large"]
                                )
                            )

                        self.pictures: Picture = pictures
                    except:
                        self.pictures = None

                    pass
                case "background":
                    try:
                        self.background: str = node["background"]
                    except:
                        self.background = None

                    pass
                case "related_anime":
                    try:
                        related_animes_json: List[dict]   = node["related_anime"]
                        related_animes: List[RelatedNode] = []

                        for node_related_anime in related_animes_json:
                            related_anime: dict = node_related_anime["node"]
                            main_picture: dict  = related_anime["main_picture"]
                            relation_type: str  = related_anime["relation_type"]
                            
                            related_animes.append(
                                RelatedNode(
                                    id           = related_anime["id"],
                                    title        = related_anime["title"],
                                    main_picture = Picture(
                                        medium = main_picture["medium"],
                                        large  = main_picture["large"]
                                    ),
                                    relation_type = RelationTypeEnum[
                                        relation_type
                                    ]
                                )
                            )
                        
                        self.related_anime: List[RelatedNode] = related_animes
                    except:
                        self.related_anime = None

                    pass
                case "related_manga":
                    try:
                        related_mangas_json: List[dict]   = node["related_manga"]
                        related_mangas: List[RelatedNode] = []

                        for node_related_manga in related_mangas_json:
                            related_manga: dict = node_related_manga["node"]
                            main_picture: dict  = related_manga["main_picture"]
                            relation_type: str  = related_manga["relation_type"]
                            
                            related_mangas.append(
                                RelatedNode(
                                    id           = related_manga["id"],
                                    title        = related_manga["title"],
                                    main_picture = Picture(
                                        medium = main_picture["medium"],
                                        large  = main_picture["large"]
                                    ),
                                    relation_type = RelationTypeEnum[
                                        relation_type
                                    ]
                                )
                            )

                        self.related_manga: List[RelatedNode] = related_mangas
                    except:
                        self.related_manga = None

                    pass
                case "recommendations":
                    try:
                        recommendations_json: List[dict] = node[
                            "recommendations"
                        ]
                        recommendations: List[Recommendation] = []

                        for node_recommendation in recommendations_json:
                            recommendation: Recommendation = node_recommendation["node"]
                            main_picture: Picture = recommendation["main_picture"]

                            recommendations.append(
                                Recommendation(
                                    id           = recommendation["id"],
                                    title        = recommendation["title"],
                                    main_picture = Picture(
                                        medium = main_picture["medium"],
                                        large  = main_picture["large"]
                                    ),
                                    num_recommendations = recommendation[
                                        "num_recommendations"
                                    ]
                                )
                            )
                    except:
                        self.recommendations = None

                    pass
                case "statistics":
                    try:
                        statistics: dict = node["statistics"]
                        status: dict     = statistics["status"]

                        self.statistics: Statistics = Statistics(
                            status = Status(
                                watching      = status["watching"],
                                completed     = status["completed"],
                                on_hold       = status["on_hold"],
                                dropped       = status["dropped"],
                                plan_to_watch = status["plan_to_watch"]
                            ),
                            num_list_users = statistics["num_list_users"]
                        )
                    except:
                        self.statistics = None

                    pass