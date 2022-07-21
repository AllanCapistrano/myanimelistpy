
class Status:
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

        self.watching = watching
        self.completed = completed
        self.on_hold = on_hold
        self.dropped = dropped
        self.plan_to_watch = plan_to_watch