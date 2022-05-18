import sys
import cProfile
import io
import pstats
import weakref
from dataclasses import dataclass
from argparse import ArgumentParser
from memory_profiler import profile
from pandas import read_csv
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
        'score'
    ]

    def __init__(self, name, year, score):
        self.name = name
        self.year = year
        self.score = score


@profile
def common_profile(file):
    cache = LRUCache(100)
    for i in range(100):
        cache[i] = CommonStudent(**dict(file.iloc[i]))
    for i in range(50, 150):
        cache[i] = CommonStudent(**dict(file.iloc[i + 200]))
    for i in range(1000):
        cache[(500 + i) // 100] = CommonStudent(**dict(file.iloc[(i + 200) // 1000]))


@profile
def slots_profile(file):
    cache = LRUCache(100)
    for i in range(100):
        cache[i] = SlotStudent(**dict(file.iloc[i]))
    for i in range(50, 150):
        cache[i] = SlotStudent(**dict(file.iloc[i + 200]))
    for i in range(1000):
        cache[(500 + i) // 100] = SlotStudent(**dict(file.iloc[(i + 200) // 1000]))


@profile
def weak_ref_profile(file):
    cache = LRUCache(100)
    for i in range(100):
        cache[i] = weakref.ref(CommonStudent(**dict(file.iloc[i])))()
    for i in range(50, 150):
        cache[i] = weakref.ref(CommonStudent(**dict(file.iloc[i + 200])))()
    for i in range(1000):
        cache[(500 + i) // 100] = weakref.ref(CommonStudent(**dict(file.iloc[(i + 200) // 1000])))()


def c_profile_smth(func, *args, **kwargs):
    profiler = cProfile.Profile()
    profiler.enable()
    func(*args, **kwargs)
    profiler.disable()
    out = io.StringIO()
    p_stats = pstats.Stats(profiler, stream=out)
    p_stats.print_stats()
    print(out.getvalue())


def main(file_name, mode):
    file = read_csv(file_name)
    if mode == 1:
        c_profile_smth(common_profile, file)
    elif mode == 2:
        c_profile_smth(slots_profile, file)
    elif mode == 3:
        c_profile_smth(weak_ref_profile, file)


def get_args(argv):
    parser = ArgumentParser()
    parser.add_argument(dest='mode', type=int, default=1)
    return parser.parse_args(args=argv[1:]).__dict__


if __name__ == "__main__":
    arg = get_args(sys.argv)
    main('students.scv', arg['mode'])
