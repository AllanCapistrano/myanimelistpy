from sys import path
path.append("../../") 

import unittest
from os import getenv
from dotenv import load_dotenv

from myanimelistpy.myanimelist import MyAnimeList
from myanimelistpy.anime import Anime
from myanimelistpy.enums.nsfwEnum import NsfwEnum
from myanimelistpy.picture import Picture

class TestMyAnimeList(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        load_dotenv()
        CLIENT_ID = getenv("CLIENT_ID")

        self.my_anime_list = MyAnimeList(client_id=CLIENT_ID)
        self.anime_name    = "Hunter x Hunter"
        self.limit         = "4"
        self.offset        = 0
        

    def test_getAnimeList_length(self):
        """ Check the length of the anime list.
        """
        
        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset
        )

        self.assertEqual(4, len(anime_list), "Should be 4.")

    def test_getAnimeList_object_type(self):
        """ Check the type of objects in the anime list.
        """

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset
        )
        
        self.assertIsInstance(anime_list.pop(), Anime)

    def test_getAnimeList_alternative_titles_field(self):
        """ Check if the 'alternative_titles' field used for the request are 
        correct.
        """

        fields = [
            "alternative_titles",
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]

        self.assertEqual(
            anime.alternative_titles.synonyms,
            ["HxH (2011)"],
            "Should be a list of synonyms with 'HxH (2011)' as the first element."
        )

    def test_getAnimeList_start_date_field(self):
        """ Check if the 'start_date' field used for the request are 
        correct.
        """

        fields = [
            "start_date",
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertEqual("2011-10-02", anime.start_date, "Should be 2011-10-02.")
    
    def test_getAnimeList_end_date_field(self):
        """ Check if the 'end_date' field used for the request are 
        correct.
        """

        fields = [
            "end_date",
            "synopsis"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertEqual("2014-09-24", anime.end_date, "Should be 2014-09-24.")
    
    def test_getAnimeList_synopsis_field(self):
        """ Check if the 'synopsis' field used for the request are 
        correct.
        """

        fields = [
            "synopsis"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertIn("Hunters devote themselves to", anime.synopsis)
        
    def test_getAnimeList_mean_field(self):
        """ Check if the 'mean' field used for the request are 
        correct.
        """

        fields = [
            "mean"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertIsInstance(anime.mean, float)

    def test_getAnimeList_rank_field(self):
        """ Check if the 'rank' field used for the request are 
        correct.
        """

        fields = [
            "rank"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertIsInstance(anime.rank, int)

    def test_getAnimeList_popularity_field(self):
        """ Check if the 'popularity' field used for the request are 
        correct.
        """

        fields = [
            "popularity"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertIsInstance(anime.popularity, int)
    
    def test_getAnimeList_num_list_users_field(self):
        """ Check if the 'num_list_users' field used for the request are 
        correct.
        """

        fields = [
            "num_list_users"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertIsInstance(anime.num_list_users, int)
    
    def test_getAnimeList_num_scoring_users_field(self):
        """ Check if the 'num_scoring_users' field used for the request are 
        correct.
        """

        fields = [
            "num_scoring_users"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertIsInstance(anime.num_scoring_users, int)
    
    def test_getAnimeList_nsfw_field(self):
        """ Check if the 'nsfw' field used for the request are 
        correct.
        """

        fields = [
            "nsfw"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]

        self.assertEqual(NsfwEnum["white"], anime.nsfw)
    
    def test_getAnimeList_genres_field(self):
        """ Check if the 'genres' field used for the request are 
        correct.
        """

        fields = [
            "genres"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]

        self.assertEqual(4, len(anime.genres), "Should be 4.")

        self.assertIsInstance(anime.genres[0].id, int)
        self.assertIsInstance(anime.genres[0].name, str)

        self.assertEqual(1, anime.genres[0].id, "Should be 1.")
        self.assertEqual("Action", anime.genres[0].name, "Should be 'Action'.")

    def test_getAnimeList_created_at_field(self):
        """ Check if the 'created_at' field used for the request are 
        correct.
        """

        fields = [
            "created_at"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertIsInstance(anime.created_at, str)
    
    def test_getAnimeList_updated_at_field(self):
        """ Check if the 'updated_at' field used for the request are 
        correct.
        """

        fields = [
            "updated_at"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertIsInstance(anime.updated_at, str)
    
    def test_getAnimeList_media_type_field(self):
        """ Check if the 'media_type' field used for the request are 
        correct.
        """

        fields = [
            "media_type"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertEqual("tv", anime.media_type, "Should be 'tv'.")
    
    def test_getAnimeList_status_field(self):
        """ Check if the 'status' field used for the request are 
        correct.
        """

        fields = [
            "status"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertEqual(
            "Finished airing", 
            anime.status.value, 
            "Should be 'Finished airing'."
        )
    
    def test_getAnimeList_num_episodes_field(self):
        """ Check if the 'num_episodes' field used for the request are 
        correct.
        """

        fields = [
            "num_episodes"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertIsInstance(anime.num_episodes, int)
    
    def test_getAnimeList_start_season_field(self):
        """ Check if the 'start_season' field used for the request are 
        correct.
        """

        fields = [
            "start_season"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertEqual("Fall", anime.start_season.season.value, "Should be 'fall'.")
        self.assertEqual(2011, anime.start_season.year, "Should be 2011.")
    
    def test_getAnimeList_broadcast_field(self):
        """ Check if the 'broadcast' field used for the request are 
        correct.
        """

        fields = [
            "broadcast"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertEqual("sunday", anime.broadcast.day_of_the_week.name, "Should be 'sunday'.")
        self.assertEqual("10:55", anime.broadcast.start_time, "Should be '10:55'.")
    
    def test_getAnimeList_no_broadcast(self):
        """ Checks if a non-broadcast anime is returning correctly
        """

        fields = [
            "broadcast"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[3]
        
        self.assertIsNone(anime.broadcast)
    
    def test_getAnimeList_source_field(self):
        """ Check if the 'source' field used for the request are 
        correct.
        """

        fields = [
            "source"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertEqual("Manga", anime.source.value, "Should be 'Manga'.")
    
    def test_getAnimeList_average_episode_duration_field(self):
        """ Check if the 'average_episode_duration' field used for the request are 
        correct.
        """

        fields = [
            "average_episode_duration"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertEqual(1417, anime.average_episode_duration, "Should be 1417.")
    
    def test_getAnimeList_rating_field(self):
        """ Check if the 'rating' field used for the request are 
        correct.
        """

        fields = [
            "rating"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertEqual("pg_13", anime.rating.name, "Should be 'pg_13'.")
    
    def test_getAnimeList_studios_field(self):
        """ Check if the 'studios' field used for the request are 
        correct.
        """

        fields = [
            "studios"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertEqual(1, len(anime.studios), "Should be 1.")
        self.assertEqual(11, anime.studios[0].id, "Should be 11.")
        self.assertEqual("Madhouse", anime.studios[0].name, "Should be 'Madhouse'.")
    
    def test_getAnimeList_pictures_field(self):
        """ Check if the 'pictures' field used for the request are 
        correct.
        """

        fields = [
            "pictures"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]

        self.assertIsNone(anime.pictures)
    
    def test_getAnimeList_background_field(self):
        """ Check if the 'background' field used for the request are 
        correct.
        """

        fields = [
            "background"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]

        self.assertIsNone(anime.background)
    
    def test_getAnimeList_related_anime_field(self):
        """ Check if the 'related_anime' field used for the request are 
        correct.
        """

        fields = [
            "related_anime"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]

        self.assertIsNone(anime.related_anime)
    
    def test_getAnimeList_related_manga_field(self):
        """ Check if the 'related_manga' field used for the request are 
        correct.
        """

        fields = [
            "related_manga"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]

        self.assertIsNone(anime.related_manga)
    
    def test_getAnimeList_recommendations_field(self):
        """ Check if the 'recommendations' field used for the request are 
        correct.
        """

        fields = [
            "recommendations"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]

        self.assertIsNone(anime.recommendations)
    
    def test_getAnimeList_statistics_field(self):
        """ Check if the 'statistics' field used for the request are 
        correct.
        """

        fields = [
            "statistics"
        ]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]

        self.assertIsNone(anime.statistics)

    def test_getAnimeList_invalid_field(self):
        """ Check if invalid fields will throw an exception.
        """

        fields = ["synopsis", "ranky"]

        with self.assertRaises(ValueError):
            self.my_anime_list.getAnimeList(
                anime_name = self.anime_name, 
                limit      = self.limit,
                offset     = self.offset,
                fields     = fields
            )

        

if __name__ == "__main__":
    unittest.main()