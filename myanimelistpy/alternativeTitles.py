
class AlternativeTitles:
    def __init__(self, synonyms: list, english: str, japanese: str) -> None:
        """ Constructor.

        Parameters
        -----------
        synonyms: :class:`list`
            A list of title synonyms.
        english: :class:`str`
            English version of the title.
        japanese: :class:`str`
            Japanese version of the title.
        """

        self.synonyms = synonyms
        self.english  = english
        self.japanese = japanese
        