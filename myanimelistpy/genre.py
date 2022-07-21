
class Genre:
    def __init__(self, id: int, name: str) -> None:
        """ Constructor

        Parameters
        -----------
        id: :class:`int`
            ID of the genre.
        name: :class:`str`
            Name of the genre.
        """

        self.id   = id
        self.name = name