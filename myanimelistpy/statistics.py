from .status import Status

class Statistics:
    def __init__(self, num_list_users: int, status: Status) -> None:
        """ Constructor

        Parameters
        -----------
        num_list_users: :class:`int`
            Number of users who added the anime to their list.
        status: :class:`Status`
            Users list status.
        """

        self.num_list_users = num_list_users
        self.status = status
        