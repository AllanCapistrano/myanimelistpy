from sys import path
path.append("../../") 

import unittest
from os import getenv
from dotenv import load_dotenv

from myanimelistpy.myanimelist import MyAnimeList
from myanimelistpy.models.anime import Anime

class TestGetAnimeList(unittest.TestCase):
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
        
        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset
        )

        self.assertEqual(4, len(anime_list), "Should be 4.")

    def test_getAnimeList_object_type(self):
        """ Check the type of objects in the anime list.
        """

        anime_list = self.my_anime_list.get_anime_list(
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

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]

        self.assertEqual(
            ["HxH (2011)"],
            anime.get_alternative_title().get_synonyms(),
            "Should be a list of synonyms with 'HxH (2011)' as the first element."
        )
        self.assertEqual(
            "Hunter x Hunter",
            anime.get_alternative_title().get_english(),
            "Should be 'Hunter x Hunter'."
        )
        self.assertEqual(
            "HUNTER×HUNTER（ハンター×ハンター）",
            anime.get_alternative_title().get_japanese(),
            "Should be 'HUNTER×HUNTER（ハンター×ハンター）'."
        )

    def test_getAnimeList_start_date_field(self):
        """ Check if the 'start_date' field used for the request are 
        correct.
        """

        fields = [
            "start_date",
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertEqual(
            "2011-10-02", 
            anime.get_start_date(), 
            "Should be 2011-10-02."
        )
    
    def test_getAnimeList_end_date_field(self):
        """ Check if the 'end_date' field used for the request are 
        correct.
        """

        fields = [
            "end_date"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertEqual(
            "2014-09-24", 
            anime.get_end_date(), 
            "Should be 2014-09-24."
        )
    
    def test_getAnimeList_synopsis_field(self):
        """ Check if the 'synopsis' field used for the request are 
        correct.
        """

        fields = [
            "synopsis"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertIn("Hunters devote themselves to", anime.get_synopsis())
        
    def test_getAnimeList_mean_field(self):
        """ Check if the 'mean' field used for the request are 
        correct.
        """

        fields = [
            "mean"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertIsInstance(anime.get_mean_score(), float)

    def test_getAnimeList_rank_field(self):
        """ Check if the 'rank' field used for the request are 
        correct.
        """

        fields = [
            "rank"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertIsInstance(anime.get_rank(), int)

    def test_getAnimeList_popularity_field(self):
        """ Check if the 'popularity' field used for the request are 
        correct.
        """

        fields = [
            "popularity"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertIsInstance(anime.get_popularity(), int)
    
    def test_getAnimeList_num_list_users_field(self):
        """ Check if the 'num_list_users' field used for the request are 
        correct.
        """

        fields = [
            "num_list_users"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertIsInstance(anime.get_num_user_list(), int)
    
    def test_getAnimeList_num_scoring_users_field(self):
        """ Check if the 'num_scoring_users' field used for the request are 
        correct.
        """

        fields = [
            "num_scoring_users"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertIsInstance(anime.get_num_scoring_users(), int)
    
    def test_getAnimeList_nsfw_field(self):
        """ Check if the 'nsfw' field used for the request are 
        correct.
        """

        fields = [
            "nsfw"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]

        self.assertEqual(
            "This work is safe for work", 
            anime.get_nsfw_classification(),
            "Should be 'This work is safe for work'."
        )
    
    def test_getAnimeList_genres_field(self):
        """ Check if the 'genres' field used for the request are 
        correct.
        """

        fields = [
            "genres"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]

        self.assertGreater(len(anime.get_genres()), 0)

        self.assertIsInstance(anime.get_genres()[0].get_id(), int)
        self.assertIsInstance(anime.get_genres()[0].get_name(), str)

        self.assertEqual(1, anime.get_genres()[0].get_id(), "Should be 1.")
        self.assertEqual(
            "Action", 
            anime.get_genres()[0].get_name(), 
            "Should be 'Action'."
        )

    def test_getAnimeList_created_at_field(self):
        """ Check if the 'created_at' field used for the request are 
        correct.
        """

        fields = [
            "created_at"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertIsInstance(anime.get_created_at(), str)
    
    def test_getAnimeList_updated_at_field(self):
        """ Check if the 'updated_at' field used for the request are 
        correct.
        """

        fields = [
            "updated_at"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertIsInstance(anime.get_updated_at(), str)
    
    def test_getAnimeList_media_type_field(self):
        """ Check if the 'media_type' field used for the request are 
        correct.
        """

        fields = [
            "media_type"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertEqual("tv", anime.get_media_type(), "Should be 'tv'.")
    
    def test_getAnimeList_status_field(self):
        """ Check if the 'status' field used for the request are 
        correct.
        """

        fields = [
            "status"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertEqual(
            "Finished airing", 
            anime.get_status(), 
            "Should be 'Finished airing'."
        )
    
    def test_getAnimeList_num_episodes_field(self):
        """ Check if the 'num_episodes' field used for the request are 
        correct.
        """

        fields = [
            "num_episodes"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertIsInstance(anime.get_num_episodes(), int)
    
    def test_getAnimeList_start_season_field(self):
        """ Check if the 'start_season' field used for the request are 
        correct.
        """

        fields = [
            "start_season"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertEqual(
            "Fall", 
            anime.get_start_season().get_season(), 
            "Should be 'Fall'."
        )
        self.assertEqual(
            2011, 
            anime.get_start_season().get_year(), 
            "Should be 2011."
        )
    
    def test_getAnimeList_broadcast_field(self):
        """ Check if the 'broadcast' field used for the request are 
        correct.
        """

        fields = [
            "broadcast"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertEqual(
            "sunday", 
            anime.get_broadcast().get_day_of_the_week(), 
            "Should be 'sunday'.",
        )
        self.assertEqual(
            "10:55", 
            anime.get_broadcast().get_start_time(), 
            "Should be '10:55'.",
        )
    
    def test_getAnimeList_no_broadcast(self):
        """ Checks if a non-broadcast anime is returning correctly
        """

        fields = [
            "broadcast"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[3]
        
        self.assertIsNone(anime.get_broadcast())
    
    def test_getAnimeList_source_field(self):
        """ Check if the 'source' field used for the request are 
        correct.
        """

        fields = [
            "source"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertEqual("Manga", anime.get_source(), "Should be 'Manga'.")
    
    def test_getAnimeList_average_episode_duration_field(self):
        """ Check if the 'average_episode_duration' field used for the request are 
        correct.
        """

        fields = [
            "average_episode_duration"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertEqual(
            1417, 
            anime.get_avg_episode_duration_in_seconds(), 
            "Should be 1417."
        )
    
    def test_getAnimeList_rating_field(self):
        """ Check if the 'rating' field used for the request are 
        correct.
        """

        fields = [
            "rating"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertEqual(
            "Teens 13 and Older", 
            anime.get_rating(), 
            "Should be 'Teens 13 and Older'."
        )
    
    def test_getAnimeList_studios_field(self):
        """ Check if the 'studios' field used for the request are 
        correct.
        """

        fields = [
            "studios"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]
        
        self.assertGreater(len(anime.get_studios()), 0)

        self.assertEqual(11, anime.get_studios()[0].get_id(), "Should be 11.")
        self.assertEqual(
            "Madhouse", 
            anime.get_studios()[0].get_name(), 
            "Should be 'Madhouse'."
        )
    
    def test_getAnimeList_pictures_field(self):
        """ Check if the 'pictures' field used for the request are 
        correct.
        """

        fields = [
            "pictures"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]

        self.assertIsNone(anime.get_pictures())
    
    def test_getAnimeList_background_field(self):
        """ Check if the 'background' field used for the request are 
        correct.
        """

        fields = [
            "background"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]

        self.assertIsNone(anime.get_background())
    
    def test_getAnimeList_related_anime_field(self):
        """ Check if the 'related_anime' field used for the request are 
        correct.
        """

        fields = [
            "related_anime"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]

        self.assertIsNone(anime.get_related_animes())
    
    def test_getAnimeList_related_manga_field(self):
        """ Check if the 'related_manga' field used for the request are 
        correct.
        """

        fields = [
            "related_manga"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]

        self.assertIsNone(anime.get_related_mangas())
    
    def test_getAnimeList_recommendations_field(self):
        """ Check if the 'recommendations' field used for the request are 
        correct.
        """

        fields = [
            "recommendations"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]

        self.assertIsNone(anime.get_recommendations())
    
    def test_getAnimeList_statistics_field(self):
        """ Check if the 'statistics' field used for the request are 
        correct.
        """

        fields = [
            "statistics"
        ]

        anime_list = self.my_anime_list.get_anime_list(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: Anime = anime_list[0]

        self.assertIsNone(anime.get_statistics())

    def test_getAnimeList_invalid_field(self):
        """ Check if invalid fields will throw an exception.
        """

        fields = ["synopsis", "ranky"]

        with self.assertRaises(ValueError):
            self.my_anime_list.get_anime_list(
                anime_name = self.anime_name, 
                limit      = self.limit,
                offset     = self.offset,
                fields     = fields
            )

if __name__ == "__main__":
    unittest.main()