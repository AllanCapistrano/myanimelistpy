from sys import path
path.append("../") 

import unittest
from os import getenv
from dotenv import load_dotenv

from myanimelistpy.myanimelist import MyAnimeList

class TestMyAnimeList(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        load_dotenv()
        CLIENT_ID = getenv("CLIENT_ID")
        
        self.my_anime_list = MyAnimeList(client_id=CLIENT_ID)

    def test_getAnimeList(self):
        """ Check that the `getAnimeList` method is working correctly.
        """
        
        expected = "Ok!" # Temp

        anime_name = "Hunter x Hunter"
        limit = "4"
        offset = 0
        fields = ["synopsis", "rank"]

        anime_list = self.my_anime_list.getAnimeList(
            anime_name = anime_name, 
            limit      = limit,
            offset     = offset,
            fields     = fields
        )

        self.assertEqual(
            anime_list,
            expected,
            "Should be Ok!" # Temp
        )

    def test_getAnimeList_invalid_field(self):
        """ Check if invalid fields will throw an exception.
        """

        anime_name = "Hunter x Hunter"
        limit = "4"
        offset = 0
        fields = ["synopsis", "ranky"]

        with self.assertRaises(ValueError):
            self.my_anime_list.getAnimeList(
                anime_name = anime_name, 
                limit      = limit,
                offset     = offset,
                fields     = fields
            )

        

if __name__ == "__main__":
    unittest.main()