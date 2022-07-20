from services.validateFields import validateFields

class MyAnimeList:
    def __init__(self, client_id: str) -> None:
        """ Constructor.
        """
        
        self.client_id = client_id

    def getAnimeList(
        self, 
        animeName: str, 
        limit: int = 100, 
        offset: int = 0,
        fields: list = []
    ):
        validateFields(fields=fields)
        
        try:
            if(len(fields) > 0):
                validateFields(fields=fields)
        except Exception as error:
            print(error)
