from .picture import Picture
from .enums.relationTypeEnum import RelationType

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

        self.id           = id
        self.title        = title
        self.main_picture = main_picture