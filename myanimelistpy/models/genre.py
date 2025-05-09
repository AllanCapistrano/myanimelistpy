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

        self.__id   = id
        self.__name = name

    def get_id(self) -> int:
        """ Genre ID.

        Returns
        -----------
        :class:`int`
        """

        return self.__id

    def get_name(self) -> str:
        """ Genre name.

        Returns
        -----------
        :class:`str`
        """

        return self.__name
