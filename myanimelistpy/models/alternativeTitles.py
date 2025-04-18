from typing import List


class AlternativeTitles:
    def __init__(self, synonyms: List[str], english: str, japanese: str) -> None:
        """ Constructor.

        Parameters
        -----------
        synonyms: :class:`List[str]`
            A list of title synonyms.
        english: :class:`str`
            English version of the title.
        japanese: :class:`str`
            Japanese version of the title.
        """

        self.__synonyms = synonyms
        self.__english  = english
        self.__japanese = japanese

    def get_synonyms(self) -> List[str]:
        """ List of synonyms.

        Returns
        -----------
        :class:`List[str]`
        """

        return self.__synonyms

    def get_english(self) -> str:
        """ English version.
        
        Returns
        -----------
        :class:`str`
        """

        return self.__english

    def get_japanese(self) -> str:
        """ Japanese version.
        
        Returns
        -----------
        :class:`str`
        """

        return self.__japanese
