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
        id: int,
        title: str,
        main_picture: Picture,
        alternative_titles: AlternativeTitles,
        start_date: str,
        end_date: str,
        synopsis: str,
        mean: float,
        rank: int,
        popularity: int,
        num_list_users: int,
        num_scoring_users: int,
        nsfw: NsfwEnum,
        genres: List[Genre],
        created_at: str,
        updated_at: str,
        media_type: MediaTypeEnum,
        status: StatusEnum,
        num_episodes: int,
        start_season: StartSeason,
        broadcast: Broadcast,
        source: SourceEnum,
        average_episode_duration: int,
        rating: RatingEnum,
        studios: List[AnimeStudio],
        pictures: Picture = None,
        background: str = None,
        related_anime: RelatedNode = None,
        related_manga: RelatedNode = None,
        recommendations: Recommendation = None,
        statistics: Statistics = None
    ) -> None:
        """ Constructor.

        Parameters
        -----------
        # TODO
        """

        super().__init__(id, title, main_picture)

        self.alternative_titles       = alternative_titles
        self.start_date               = start_date
        self.end_date                 = end_date
        self.synopsis                 = synopsis
        self.mean                     = mean
        self.rank                     = rank
        self.popularity               = popularity
        self.num_list_users           = num_list_users
        self.num_scoring_users        = num_scoring_users
        self.nsfw                     = nsfw
        self.genres                   = genres
        self.created_at               = created_at
        self.updated_at               = updated_at
        self.media_type               = media_type
        self.status                   = status
        self.num_episodes             = num_episodes
        self.start_season             = start_season
        self.broadcast                = broadcast
        self.source                   = source
        self.average_episode_duration = average_episode_duration
        self.rating                   = rating
        self.studios                  = studios
        self.pictures                 = pictures # Cannot contain this field in a list.
        self.background               = background # Cannot contain this field in a list.
        self.related_anime            = related_anime # Cannot contain this field in a list.
        self.related_manga            = related_manga # Cannot contain this field in a list.
        self.recommendations          = recommendations # Cannot contain this field in a list.
        self.statistics               = statistics # Cannot contain this field in a list.