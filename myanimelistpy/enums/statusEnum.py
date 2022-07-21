from enum import Enum

class Status(Enum):
    finished_airing  = 0
    currently_airing = 1
    not_yet_aired    = 2