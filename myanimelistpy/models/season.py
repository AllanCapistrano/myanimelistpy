from ..enums.seasonEnum import SeasonEnum

class Season:
    def __init__(self, year: int, season: SeasonEnum) -> None:
        """ Constructor.
        
        Parameters
        -----------
        year: :class:`int`
            Anime release year.
        season: :class:`SeasonEnum`
            Anime release season.
        """

        self.__year = year
        self.__season = season

    def get_year(self) -> int:
        """ Year of season.

        Returns
        -----------
        :class:`int`
        """

        return self.__year

    def get_season(self) -> str:
        """ Season name.

        Returns
        -----------
        :class:`str`
        """

        return self.__season.value
