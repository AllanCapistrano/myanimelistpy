from typing import List

from ..enums.fields import Fields

def validateFields(fields: List[str]) -> bool:
    """ Validate the fields provided.

    Parameters
    -----------
    fields: :class:`list`
        Fields list.

    Returns
    -----------
    bool: :class:`bool`
    """
    
    for field in fields:
        flag = False

        for index in range(len(Fields)):
            if(field == Fields(index).name):
                flag = True

        if(not flag):
            raise ValueError(f"'{field}' is not a valid field!")

    return True