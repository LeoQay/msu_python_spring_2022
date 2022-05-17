import cProfile
import io
import pstats
from memory_profiler import profile
import weakref
from pandas import read_csv
from dataclasses import dataclass
from lru_cache import LRUCache


@dataclass
class CommonStudent:
    name: str
    year: int
    score: float


class SlotStudent:
    __slots__ = [
        'name',
        'year',
        'average_score'
    ]


@profile
def with_weak_ref(file_name):
    pass


@profile
def with_slots(file_name):
    pass


@profile
def with_common(file_name):
    file = read_csv(file_name)
    cache = LRUCache(100)
    for i in range(100):
        cache[i] = CommonStudent(**dict(file.iloc[i]))
    for i in range(50, 150):
        cache[i] = CommonStudent(**dict(file.iloc[i + 200]))
    for i in range(1000):
        cache[(500 + i) // 100] = CommonStudent(**dict(file.iloc[(i + 200) // 1000]))


def c_profile_smth(func, *args, **kwargs):
    pr = cProfile.Profile()
    pr.enable()
    func(*args, **kwargs)
    pr.disable()
    out = io.StringIO()
    ps = pstats.Stats(pr, stream=out)
    ps.print_stats()
    print(out.getvalue())


def main(file_name):
    c_profile_smth(with_common, file_name)


if __name__ == "__main__":
    main('students.scv')
