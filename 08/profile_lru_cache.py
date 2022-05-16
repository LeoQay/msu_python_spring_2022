import cProfile
import weakref
from lru_cache import LRUCache
from dataclasses import dataclass


@dataclass
class CommonStudent:
    year: int
    name: str
    average_score: float


class SlotStudent:
    __slots__ = [
        'year',
        'name',
        'average_score'
    ]


def with_weak_ref():
    pass


def with_slots():
    pass


def with_common():
    pass


def main():
    pass


if __name__ == "__main__":
    main()
