from sys import path
path.append("../../") 

import unittest
from os import getenv
from dotenv import load_dotenv

from myanimelistpy.myanimelist import MyAnimeList

class TestGetAnimeListInDict(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        load_dotenv()
        CLIENT_ID = getenv("CLIENT_ID")

        self.my_anime_list = MyAnimeList(client_id=CLIENT_ID)
        self.anime_name    = "Hunter x Hunter"
        self.limit         = "4"
        self.offset        = 0

    def test_getAnimeListInDict_length(self):
        """ Check the length of the anime list.
        """
        
        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset
        )

        self.assertEqual(4, len(anime_list), "Should be 4.")
    
    def test_getAnimeListInDict_object_type(self):
        """ Check the type of objects in the anime list.
        """

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset
        )
        
        self.assertIsInstance(anime_list, list)

    def test_getAnimeListInDict_alternative_titles_field(self):
        """ Check if the 'alternative_titles' field used for the request are 
        correct.
        """

        fields = [
            "alternative_titles",
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]

        self.assertEqual(
            ["HxH (2011)"],
            anime["alternative_titles"]["synonyms"],
            "Should be a list of synonyms with 'HxH (2011)' as the first element."
        )
        self.assertEqual(
            "Hunter x Hunter",
            anime["alternative_titles"]["en"],
            "Should be 'Hunter x Hunter'."
        )
        self.assertEqual(
            "HUNTER×HUNTER（ハンター×ハンター）",
            anime["alternative_titles"]["ja"],
            "Should be 'HUNTER×HUNTER（ハンター×ハンター）'."
        )

    def test_getAnimeListInDict_start_date_field(self):
        """ Check if the 'start_date' field used for the request are 
        correct.
        """

        fields = [
            "start_date",
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]
        
        self.assertEqual(
            "2011-10-02", 
            anime["start_date"], 
            "Should be 2011-10-02."
        ),

    def test_getAnimeListInDict_end_date_field(self):
        """ Check if the 'end_date' field used for the request are 
        correct.
        """

        fields = [
            "end_date"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]
        
        self.assertEqual(
            "2014-09-24", 
            anime["end_date"], 
            "Should be 2014-09-24."
        )

    def test_getAnimeListInDict_synopsis_field(self):
        """ Check if the 'synopsis' field used for the request are 
        correct.
        """

        fields = [
            "synopsis"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]
        
        self.assertIn("Hunters devote themselves to", anime["synopsis"])
        
    def test_getAnimeListInDict_mean_field(self):
        """ Check if the 'mean' field used for the request are 
        correct.
        """

        fields = [
            "mean"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]
        
        self.assertIsInstance(anime["mean"], float)

    def test_getAnimeListInDict_rank_field(self):
        """ Check if the 'rank' field used for the request are 
        correct.
        """

        fields = [
            "rank"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]
        
        self.assertIsInstance(anime["rank"], int)

    def test_getAnimeListInDict_popularity_field(self):
        """ Check if the 'popularity' field used for the request are 
        correct.
        """

        fields = [
            "popularity"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]
        
        self.assertIsInstance(anime["popularity"], int)
    
    def test_getAnimeListInDict_num_list_users_field(self):
        """ Check if the 'num_list_users' field used for the request are 
        correct.
        """

        fields = [
            "num_list_users"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]
        
        self.assertIsInstance(anime["num_list_users"], int)
    
    def test_getAnimeListInDict_num_scoring_users_field(self):
        """ Check if the 'num_scoring_users' field used for the request are 
        correct.
        """

        fields = [
            "num_scoring_users"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]
        
        self.assertIsInstance(anime["num_scoring_users"], int)
    
    def test_getAnimeListInDict_nsfw_field(self):
        """ Check if the 'nsfw' field used for the request are 
        correct.
        """

        fields = [
            "nsfw"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]

        self.assertEqual(
            "white", 
            anime["nsfw"],
            "Should be 'white'."
        )
    
    def test_getAnimeListInDict_genres_field(self):
        """ Check if the 'genres' field used for the request are 
        correct.
        """

        fields = [
            "genres"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]

        self.assertGreater(len(anime["genres"]), 0)

        self.assertIsInstance(anime["genres"][0]["id"], int)
        self.assertIsInstance(anime["genres"][0]["name"], str)

        self.assertEqual(1, anime["genres"][0]["id"], "Should be 1.")
        self.assertEqual(
            "Action", 
            anime["genres"][0]["name"], 
            "Should be 'Action'."
        )

    def test_getAnimeListInDict_created_at_field(self):
        """ Check if the 'created_at' field used for the request are 
        correct.
        """

        fields = [
            "created_at"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]
        
        self.assertIsInstance(anime["created_at"], str)
    
    def test_getAnimeListInDict_updated_at_field(self):
        """ Check if the 'updated_at' field used for the request are 
        correct.
        """

        fields = [
            "updated_at"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]
        
        self.assertIsInstance(anime["updated_at"], str)
    
    def test_getAnimeListInDict_media_type_field(self):
        """ Check if the 'media_type' field used for the request are 
        correct.
        """

        fields = [
            "media_type"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]
        
        self.assertEqual("tv", anime["media_type"], "Should be 'tv'.")
    
    def test_getAnimeListInDict_status_field(self):
        """ Check if the 'status' field used for the request are 
        correct.
        """

        fields = [
            "status"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]
        
        self.assertEqual(
            "finished_airing", 
            anime["status"], 
            "Should be 'finished_airing'."
        )
    
    def test_getAnimeListInDict_num_episodes_field(self):
        """ Check if the 'num_episodes' field used for the request are 
        correct.
        """

        fields = [
            "num_episodes"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]
        
        self.assertIsInstance(anime["num_episodes"], int)
    
    def test_getAnimeListInDict_start_season_field(self):
        """ Check if the 'start_season' field used for the request are 
        correct.
        """

        fields = [
            "start_season"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]
        
        self.assertEqual(
            "fall", 
            anime["start_season"]["season"], 
            "Should be 'fall'."
        )
        self.assertEqual(
            2011, 
            anime["start_season"]["year"], 
            "Should be 2011."
        )
    
    def test_getAnimeListInDict_broadcast_field(self):
        """ Check if the 'broadcast' field used for the request are 
        correct.
        """

        fields = [
            "broadcast"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]
        
        self.assertEqual(
            "sunday", 
            anime["broadcast"]["day_of_the_week"], 
            "Should be 'sunday'.",
        )
        self.assertEqual(
            "10:55", 
            anime["broadcast"]["start_time"], 
            "Should be '10:55'.",
        )
    
    def test_getAnimeListInDict_no_broadcast(self):
        """ Checks if a non-broadcast anime is returning correctly
        """

        fields = [
            "broadcast"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[3]
        
        with self.assertRaises(KeyError):
            anime["broadcast"]
    
    def test_getAnimeListInDict_source_field(self):
        """ Check if the 'source' field used for the request are 
        correct.
        """

        fields = [
            "source"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]
        
        self.assertEqual("manga", anime["source"], "Should be 'manga'.")
    
    def test_getAnimeListInDict_average_episode_duration_field(self):
        """ Check if the 'average_episode_duration' field used for the request are 
        correct.
        """

        fields = [
            "average_episode_duration"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]
        
        self.assertEqual(
            1417, 
            anime["average_episode_duration"], 
            "Should be 1417."
        )
    
    def test_getAnimeListInDict_rating_field(self):
        """ Check if the 'rating' field used for the request are 
        correct.
        """

        fields = [
            "rating"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]
        
        self.assertEqual(
            "pg_13", 
            anime["rating"], 
            "Should be 'pg_13'."
        )
    
    def test_getAnimeListInDict_studios_field(self):
        """ Check if the 'studios' field used for the request are 
        correct.
        """

        fields = [
            "studios"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]
        
        self.assertGreater(len(anime["studios"]), 0)

        self.assertEqual(11, anime["studios"][0]["id"], "Should be 11.")
        self.assertEqual(
            "Madhouse", 
            anime["studios"][0]["name"], 
            "Should be 'Madhouse'."
        )
    
    def test_getAnimeListInDict_pictures_field(self):
        """ Check if the 'pictures' field used for the request are 
        correct.
        """

        fields = [
            "pictures"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]

        with self.assertRaises(KeyError):
            anime["pictures"]
    
    def test_getAnimeListInDict_background_field(self):
        """ Check if the 'background' field used for the request are 
        correct.
        """

        fields = [
            "background"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]

        with self.assertRaises(KeyError):
            anime["background"]
    
    def test_getAnimeListInDict_related_anime_field(self):
        """ Check if the 'related_anime' field used for the request are 
        correct.
        """

        fields = [
            "related_anime"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]

        with self.assertRaises(KeyError):
            anime["related_anime"]
    
    def test_getAnimeListInDict_related_manga_field(self):
        """ Check if the 'related_manga' field used for the request are 
        correct.
        """

        fields = [
            "related_manga"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]

        with self.assertRaises(KeyError):
            anime["related_manga"]
    
    def test_getAnimeListInDict_recommendations_field(self):
        """ Check if the 'recommendations' field used for the request are 
        correct.
        """

        fields = [
            "recommendations"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]

        with self.assertRaises(KeyError):
            anime["recommendations"]
          
    def test_getAnimeListInDict_statistics_field(self):
        """ Check if the 'statistics' field used for the request are 
        correct.
        """

        fields = [
            "statistics"
        ]

        anime_list = self.my_anime_list.get_anime_list_in_dict(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        anime: dict = anime_list[0]["node"]

        with self.assertRaises(KeyError):
            anime["statistics"]

    def test_getAnimeListInDict_invalid_field(self):
        """ Check if invalid fields will throw an exception.
        """

        fields = ["synopsis", "ranky"]

        with self.assertRaises(ValueError):
            self.my_anime_list.get_anime_list_in_dict(
                anime_name = self.anime_name, 
                limit      = self.limit,
                offset     = self.offset,
                fields     = fields
            )

if __name__ == "__main__":
    unittest.main()