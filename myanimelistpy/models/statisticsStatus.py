class StatisticsStatus:
    def __init__(
        self,
        watching: int,
        completed: int,
        on_hold: int,
        dropped: int,
        plan_to_watch: int,
    ) -> None:
        """ Constructor

        Parameters
        -----------
        watching: :class:`int`
            Number of users who are watching.
        completed: :class:`int`
            Number of users who completed.
        on_hold: :class:`int`
            Number of users who are on hold.
        dropped: :class:`int`
            Number of users who dropped.
        plan_to_watch: :class:`int`
            Number of users who are plan to watch.
        """

        self.__watching      = watching
        self.__completed     = completed
        self.__on_hold       = on_hold
        self.__dropped       = dropped
        self.__plan_to_watch = plan_to_watch

    def get_num_watching(self) -> int:
        """ The number of users who are watching the anime.

        Returns
        -----------
        :class:`int`
        """

        return self.__watching

    def get_num_completed(self) -> int:
        """ The number of users who are completed the anime.

        Returns
        -----------
        :class:`int`
        """

        return self.__completed

    def get_num_on_hold(self) -> int:
        """ The number of users who are waiting for the anime.

        Returns
        -----------
        :class:`int`
        """

        return self.__on_hold

    def get_num_dropped(self) -> int:
        """ The number of users who are dropped the anime.

        Returns
        -----------
        :class:`int`
        """

        return self.__dropped

    def get_num_plan_to_watch(self) -> int:
        """ The number of users who plan to watch the anime.

        Returns
        -----------
        :class:`int`
        """

        return self.__plan_to_watch
