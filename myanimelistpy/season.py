from .enums.seasonEnum import SeasonEnum

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
        
        self.year = year
        self.season = season