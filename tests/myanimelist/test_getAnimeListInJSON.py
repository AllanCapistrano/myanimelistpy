from sys import path
path.append("../../") 

import unittest
from os import getenv
from dotenv import load_dotenv

from myanimelistpy.myanimelist import MyAnimeList

class TestGetAnimeListInJSON(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        load_dotenv()
        CLIENT_ID = getenv("CLIENT_ID")

        self.my_anime_list = MyAnimeList(client_id=CLIENT_ID)
        self.anime_name    = "Hunter x Hunter"
        self.limit         = "4"
        self.offset        = 0

    def test_getAnimeListInJSON_object_type(self):
        """ Check the type of objects in the anime list.
        """

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset
        )
        
        self.assertIsInstance(anime_list_in_json, str)

    def test_getAnimeListInJSON_alternative_titles_field(self):
        """ Check if the 'alternative_titles' field used for the request are 
        correct.
        """

        fields = [
            "alternative_titles",
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        self.assertNotEqual(-1, anime_list_in_json.find("alternative_titles"))

    def test_getAnimeListInJSON_start_date_field(self):
        """ Check if the 'start_date' field used for the request are 
        correct.
        """

        fields = [
            "start_date",
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )
        
        self.assertNotEqual(-1, anime_list_in_json.find("start_date"))

    def test_getAnimeListInJSON_end_date_field(self):
        """ Check if the 'end_date' field used for the request are 
        correct.
        """

        fields = [
            "end_date"
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )
        
        self.assertNotEqual(-1, anime_list_in_json.find("end_date"))

    def test_getAnimeListInJSON_synopsis_field(self):
        """ Check if the 'synopsis' field used for the request are 
        correct.
        """

        fields = [
            "synopsis"
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )
        
        self.assertNotEqual(-1, anime_list_in_json.find("synopsis"))
        
    def test_getAnimeListInJSON_mean_field(self):
        """ Check if the 'mean' field used for the request are 
        correct.
        """

        fields = [
            "mean"
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )
        
        self.assertNotEqual(-1, anime_list_in_json.find("mean"))

    def test_getAnimeListInJSON_rank_field(self):
        """ Check if the 'rank' field used for the request are 
        correct.
        """

        fields = [
            "rank"
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )
        
        self.assertNotEqual(-1, anime_list_in_json.find("rank"))

    def test_getAnimeListInJSON_popularity_field(self):
        """ Check if the 'popularity' field used for the request are 
        correct.
        """

        fields = [
            "popularity"
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )
        
        self.assertNotEqual(-1, anime_list_in_json.find("popularity"))
    
    def test_getAnimeListInJSON_num_list_users_field(self):
        """ Check if the 'num_list_users' field used for the request are 
        correct.
        """

        fields = [
            "num_list_users"
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )
        
        self.assertNotEqual(-1, anime_list_in_json.find("num_list_users"))
    
    def test_getAnimeListInJSON_num_scoring_users_field(self):
        """ Check if the 'num_scoring_users' field used for the request are 
        correct.
        """

        fields = [
            "num_scoring_users"
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )
        
        self.assertNotEqual(-1, anime_list_in_json.find("num_scoring_users"))
    
    def test_getAnimeListInJSON_nsfw_field(self):
        """ Check if the 'nsfw' field used for the request are 
        correct.
        """

        fields = [
            "nsfw"
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        self.assertNotEqual(-1, anime_list_in_json.find("nsfw"))
    
    def test_getAnimeListInJSON_genres_field(self):
        """ Check if the 'genres' field used for the request are 
        correct.
        """

        fields = [
            "genres"
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        self.assertNotEqual(-1, anime_list_in_json.find("genres"))

    def test_getAnimeListInJSON_created_at_field(self):
        """ Check if the 'created_at' field used for the request are 
        correct.
        """

        fields = [
            "created_at"
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )
        
        self.assertNotEqual(-1, anime_list_in_json.find("created_at"))
    
    def test_getAnimeListInJSON_updated_at_field(self):
        """ Check if the 'updated_at' field used for the request are 
        correct.
        """

        fields = [
            "updated_at"
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )
        
        self.assertNotEqual(-1, anime_list_in_json.find("updated_at"))
    
    def test_getAnimeListInJSON_media_type_field(self):
        """ Check if the 'media_type' field used for the request are 
        correct.
        """

        fields = [
            "media_type"
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )
        
        self.assertNotEqual(-1, anime_list_in_json.find("media_type"))
    
    def test_getAnimeListInJSON_status_field(self):
        """ Check if the 'status' field used for the request are 
        correct.
        """

        fields = [
            "status"
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )
        
        self.assertNotEqual(-1, anime_list_in_json.find("status"))
    
    def test_getAnimeListInJSON_num_episodes_field(self):
        """ Check if the 'num_episodes' field used for the request are 
        correct.
        """

        fields = [
            "num_episodes"
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )
        
        self.assertNotEqual(-1, anime_list_in_json.find("num_episodes"))
    
    def test_getAnimeListInJSON_start_season_field(self):
        """ Check if the 'start_season' field used for the request are 
        correct.
        """

        fields = [
            "start_season"
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )
        
        self.assertNotEqual(-1, anime_list_in_json.find("start_season"))
    
    def test_getAnimeListInJSON_broadcast_field(self):
        """ Check if the 'broadcast' field used for the request are 
        correct.
        """

        fields = [
            "broadcast"
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )
        
        self.assertNotEqual(-1, anime_list_in_json.find("broadcast"))
    
    def test_getAnimeListInJSON_source_field(self):
        """ Check if the 'source' field used for the request are 
        correct.
        """

        fields = [
            "source"
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )
        
        self.assertNotEqual(-1, anime_list_in_json.find("source"))
    
    def test_getAnimeListInJSON_average_episode_duration_field(self):
        """ Check if the 'average_episode_duration' field used for the request are 
        correct.
        """

        fields = [
            "average_episode_duration"
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )
        
        self.assertNotEqual(-1, anime_list_in_json.find("average_episode_duration"))
    
    def test_getAnimeListInJSON_rating_field(self):
        """ Check if the 'rating' field used for the request are 
        correct.
        """

        fields = [
            "rating"
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )
        
        self.assertNotEqual(-1, anime_list_in_json.find("rating"))
    
    def test_getAnimeListInJSON_studios_field(self):
        """ Check if the 'studios' field used for the request are 
        correct.
        """

        fields = [
            "studios"
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )
        
        self.assertNotEqual(-1, anime_list_in_json.find("studios"))
    
    def test_getAnimeListInJSON_pictures_field(self):
        """ Check if the 'pictures' field used for the request are 
        correct.
        """

        fields = [
            "pictures"
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        self.assertEqual(-1, anime_list_in_json.find("pictures"))
    
    def test_getAnimeListInJSON_background_field(self):
        """ Check if the 'background' field used for the request are 
        correct.
        """

        fields = [
            "background"
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        self.assertEqual(-1, anime_list_in_json.find("background"))
    
    def test_getAnimeListInJSON_related_anime_field(self):
        """ Check if the 'related_anime' field used for the request are 
        correct.
        """

        fields = [
            "related_anime"
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        self.assertEqual(-1, anime_list_in_json.find("related_anime"))
    
    def test_getAnimeListInJSON_related_manga_field(self):
        """ Check if the 'related_manga' field used for the request are 
        correct.
        """

        fields = [
            "related_manga"
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        self.assertEqual(-1, anime_list_in_json.find("related_manga"))
    
    def test_getAnimeListInJSON_recommendations_field(self):
        """ Check if the 'recommendations' field used for the request are 
        correct.
        """

        fields = [
            "recommendations"
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        self.assertEqual(-1, anime_list_in_json.find("recommendations"))
          
    def test_getAnimeListInJSON_statistics_field(self):
        """ Check if the 'statistics' field used for the request are 
        correct.
        """

        fields = [
            "statistics"
        ]

        anime_list_in_json = self.my_anime_list.get_anime_list_in_json(
            anime_name = self.anime_name, 
            limit      = self.limit,
            offset     = self.offset,
            fields     = fields
        )

        self.assertEqual(-1, anime_list_in_json.find("statistics"))

    def test_getAnimeListInJSON_invalid_field(self):
        """ Check if invalid fields will throw an exception.
        """

        fields = ["synopsis", "ranky"]

        with self.assertRaises(ValueError):
            self.my_anime_list.get_anime_list_in_json(
                anime_name = self.anime_name, 
                limit      = self.limit,
                offset     = self.offset,
                fields     = fields
            )

if __name__ == "__main__":
    unittest.main()