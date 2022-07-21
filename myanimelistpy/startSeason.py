from .enums.seasonEnum import Season

class StartSeason:
    def __init__(self, year: int, season: Season) -> None:
        """ Constructor.
        
        Parameters
        -----------
        year: :class:`int`
            Anime release year.
        season: :class:`Season`
            Anime release season.
        """
        
        self.year = year
        self.season = season