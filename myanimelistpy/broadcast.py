from .enums.dayWeekEnum import DayWeek

class Broadcast:
    def __init__(self, day_of_the_week: DayWeek, start_time: str) -> None:
        """ Constructor

        Parameters
        -----------
        day_of_the_week: :class:`DayWeek`
            Day of the week broadcast in Japan time.
        start_time: :class:`str`
            Time in hours format that is broadcasted.
        """
        
        self.day_of_the_week = day_of_the_week
        self.start_time = start_time