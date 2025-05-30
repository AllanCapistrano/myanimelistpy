class Studio:
    def __init__(self, id: int, name: str) -> None:
        """ Constructor

        Parameters
        -----------
        id: :class:`int`
            ID of the Anime Studio.
        name: :class:`str`
            Name of the Anime Studio.
        """

        self.__id   = id
        self.__name = name

    def get_id(self) -> int:
        """ Studio ID.

        Returns
        -----------
        :class:`int`
        """

        return self.__id

    def get_name(self) -> str:
        """ Studio name.

        Returns
        -----------
        :class:`str`
        """

        return self.__name
