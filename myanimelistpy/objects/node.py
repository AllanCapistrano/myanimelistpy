from .picture import Picture
from ..enums.relationTypeEnum import RelationTypeEnum

class Node:
    def __init__(self, 
        id: int,
        title: str, 
        main_picture: Picture, 
    ) -> None:
        """ Constructor

        Parameters
        -----------
        id: :class:`int`
            ID of the anime or manga.
        title: :class:`str`
            Title of the anime or manga.
        main_picture: :class:`Picture`
            Main picture of the anime or manga.
        """

        self.__id           = id
        self.__title        = title
        self.__main_picture = main_picture

    def getId(self) -> int:
        """ Anime or manga ID.

        Returns
        -----------
        :class:`int`
        """
        
        return self.__id

    def getTitle(self) -> str:
        """ Anime or manga ID.

        Returns
        -----------
        :class:`int`
        """
        
        return self.__title

    def getMainPicture(self) -> Picture:
        """ Anime or manga main picture.

        Returns
        -----------
        :class:`int`
        """
        
        return self.__main_picture