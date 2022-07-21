
class Picture:
    def __init__(self, large: str, medium: str) -> None:
        """ Constructor.

         Parameters
        -----------
        large: :class:`str`
            The URI of an anime's large picture.
        medium: :class:`str`
            The URI of an anime's medium picture.
        """

        self.large  = large
        self.medium = medium 