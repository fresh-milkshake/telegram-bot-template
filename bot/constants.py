import os
from pathlib import Path
from enum import IntEnum, auto


class AccessLevel(IntEnum):
    GUEST = auto()
    USER = auto()
    ADMIN = auto()

    @classmethod
    def ALL(cls):
        return list(cls)

    def __str__(self):
        return self.name

    def __lt__(self, other):
        if not isinstance(other, (AccessLevel, int)):
            raise TypeError(f"Cannot compare AccessLevel with {type(other)}")
        return self.value < (other.value if isinstance(other, AccessLevel) else other)

    def __le__(self, other):
        if not isinstance(other, (AccessLevel, int)):
            raise TypeError(f"Cannot compare AccessLevel with {type(other)}")
        return self.value <= (other.value if isinstance(other, AccessLevel) else other)

    def __gt__(self, other):
        if not isinstance(other, (AccessLevel, int)):
            raise TypeError(f"Cannot compare AccessLevel with {type(other)}")
        return self.value > (other.value if isinstance(other, AccessLevel) else other)

    def __ge__(self, other):
        if not isinstance(other, (AccessLevel, int)):
            raise TypeError(f"Cannot compare AccessLevel with {type(other)}")
        return self.value >= (other.value if isinstance(other, AccessLevel) else other)

    def __eq__(self, other):
        if not isinstance(other, (AccessLevel, int)):
            return False
        return self.value == (other.value if isinstance(other, AccessLevel) else other)

    def __ne__(self, other):
        return not self.__eq__(other)


DATABASE_NAME = "database.db"
# https://docs.python.org/2/library/sqlite3.html#sqlite3.connect
DATABASE_PRAGMAS = {
    "journal_mode": "wal",
    # "cache_size": -1 * 64000,  # 64MB
    # "foreign_keys": 1,
    # "ignore_check_constraints": 0,
    # "synchronous": 0,
}
UNKNOWN_STRING_VALUE = "Unknown"

TOKEN = os.getenv("TELEGRAM_TOKEN")

PROJECT_PATH = Path(__file__).resolve().parent.parent
LOGS_PATH = PROJECT_PATH / "logs"
DATABASE_PATH = PROJECT_PATH / DATABASE_NAME

DEFAULT_ACCESS_LEVEL = AccessLevel.GUEST