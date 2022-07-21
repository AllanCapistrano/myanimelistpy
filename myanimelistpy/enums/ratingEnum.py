from enum import Enum

class Rating(Enum):
    g      = "G - All Ages"
    pg     = "PG - Children"
    pg_13  = "pg_13 - Teens 13 and Older"
    r      = "R - 17+ (violence & profanity)"
    r_plus = "R+ - Profanity & Mild Nudity" # r+
    rx     = "Rx - Hentai"