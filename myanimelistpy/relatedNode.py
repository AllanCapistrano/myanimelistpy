from .node import Node
from .picture import Picture
from .enums.relationTypeEnum import RelationType

class RelatedNode(Node):
    def __init__(
        self, 
        id: int,
        title: str,
        main_picture: Picture,
        relation_type: RelationType
    ) -> None:
        """ Constructor.

        Parameters
        -----------
        id: :class:`int`
            ID of the anime or manga.
        title: :class:`str`
            Title of the anime or manga.
        main_picture: :class:`Picture`
            Main picture of the anime or manga.
        relation_type: :class:`RelationType`
            Relation type of the anime or manga.
        """

        super().__init__(id, title, main_picture)
        
        self.relation_type = relation_type