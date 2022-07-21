from sys import path
path.append("../../") 

import unittest
from os import getenv
from typing import List
from dotenv import load_dotenv

from myanimelistpy.myanimelist import MyAnimeList
from myanimelistpy.anime import Anime

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
        
        self.assertTrue(isinstance(anime_list.pop(), Anime))


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
        
        self.assertIn("Hunters devote themselves to", anime.synopsis, )

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