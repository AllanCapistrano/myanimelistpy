from sys import path
path.append("../../") 

import unittest
from os import getenv
from dotenv import load_dotenv

from myanimelistpy.myanimelist import MyAnimeList
from myanimelistpy.anime import Anime
from myanimelistpy.enums.nsfwEnum import NsfwEnum

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
            ["HxH (2011)"],
            anime.getAlternativeTitle().getSynonyms(),
            "Should be a list of synonyms with 'HxH (2011)' as the first element."
        )
        self.assertEqual(
            "Hunter x Hunter",
            anime.getAlternativeTitle().getEnglish(),
            "Should be 'Hunter x Hunter'."
        )
        self.assertEqual(
            "HUNTER×HUNTER（ハンター×ハンター）",
            anime.getAlternativeTitle().getJapanese(),
            "Should be 'HUNTER×HUNTER（ハンター×ハンター）'."
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
        
        self.assertEqual(
            "2011-10-02", 
            anime.getStartDate(), 
            "Should be 2011-10-02."
        )
    
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
        
        self.assertEqual(
            "2014-09-24", 
            anime.getEndDate(), 
            "Should be 2014-09-24."
        )
    
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
        
        self.assertIn("Hunters devote themselves to", anime.getSynopsis())
        
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
        
        self.assertIsInstance(anime.getMean(), float)

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
        
        self.assertIsInstance(anime.getRank(), int)

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
        
        self.assertIsInstance(anime.getPopularity(), int)
    
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
        
        self.assertIsInstance(anime.getNumUserList(), int)
    
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
        
        self.assertIsInstance(anime.getNumScoringUsers(), int)
    
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

        self.assertEqual(NsfwEnum["white"].value, anime.getNsfwClassification())
    
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

        self.assertGreater(len(anime.getGenres()), 0)

        self.assertIsInstance(anime.getGenres()[0].getId(), int)
        self.assertIsInstance(anime.getGenres()[0].getName(), str)

        self.assertEqual(1, anime.getGenres()[0].getId(), "Should be 1.")
        self.assertEqual(
            "Action", 
            anime.getGenres()[0].getName(), 
            "Should be 'Action'."
        )

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
        
        self.assertIsInstance(anime.getCreatedAt(), str)
    
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
        
        self.assertIsInstance(anime.getUpdatedAt(), str)
    
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
        
        self.assertEqual("tv", anime.getMediaType(), "Should be 'tv'.")
    
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
            anime.getStatus(), 
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
        
        self.assertIsInstance(anime.getNumEpisodes(), int)
    
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
        
        self.assertEqual(
            "Fall", 
            anime.getStartSeason().getSeason(), 
            "Should be 'fall'."
        )
        self.assertEqual(
            2011, 
            anime.getStartSeason().getYear(), 
            "Should be 2011."
        )
    
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
        
        self.assertEqual(
            "sunday", 
            anime.getBroadcast().getDayOfTheWeek(), 
            "Should be 'sunday'.",
        )
        self.assertEqual(
            "10:55", 
            anime.getBroadcast().getStartTime(), 
            "Should be '10:55'.",
        )
    
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
        
        self.assertIsNone(anime.getBroadcast())
    
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
        
        self.assertEqual("Manga", anime.getSource(), "Should be 'Manga'.")
    
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
        
        self.assertEqual(
            1417, 
            anime.getAvgEpisodeDurationInSeconds(), 
            "Should be 1417."
        )
    
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
        
        self.assertEqual(
            "Teens 13 and Older", 
            anime.getRating(), 
            "Should be 'Teens 13 and Older'."
        )
    
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
        
        self.assertGreater(len(anime.getStudios()), 0)

        self.assertEqual(11, anime.getStudios()[0].getId(), "Should be 11.")
        self.assertEqual(
            "Madhouse", 
            anime.getStudios()[0].getName(), 
            "Should be 'Madhouse'."
        )
    
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

        self.assertIsNone(anime.getPictures())
    
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

        self.assertIsNone(anime.getBackground())
    
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

        self.assertIsNone(anime.getRelatedAnimes())
    
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

        self.assertIsNone(anime.getRelatedMangas())
    
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

        self.assertIsNone(anime.getRecommendations())
    
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

        self.assertIsNone(anime.getStatistics())

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