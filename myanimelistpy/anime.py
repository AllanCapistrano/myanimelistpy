from typing import List

from .node import Node
from .enums.nsfwEnum import NsfwEnum
from .picture import Picture
from .alternativeTitles import AlternativeTitles
from .genre import Genre
from .enums.mediaTypeEnum import MediaTypeEnum
from .enums.statusEnum import StatusEnum
from .startSeason import StartSeason
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
        # TODO: Documentation of the method

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
                    pass
                case "rank":
                    pass
                case "popularity":
                    pass
                case "num_list_users":
                    pass
                case "num_scoring_users":
                    pass
                case "nsfw":
                    pass
                case "genres":
                    pass
                case "created_at":
                    pass
                case "updated_at":
                    pass
                case "media_type":
                    pass
                case "status":
                    pass
                case "num_episodes":
                    pass
                case "start_season":
                    pass
                case "broadcast":
                    pass
                case "source":
                    pass
                case "average_episode_duration":
                    pass
                case "rating":
                    pass
                case "studios":
                    pass
                case "pictures":
                    pass
                case "background":
                    pass
                case "related_anime":
                    pass
                case "recommendations":
                    pass
                case "statistics":
                    pass