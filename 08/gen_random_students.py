import names
import random


def gen_score(a: float, b: float):
    while True:
        yield round(random.uniform(a, b), 2)


def gen_name():
    while True:
        yield names.get_full_name()


def gen_year(a: int, b: int):
    while True:
        yield random.randint(a, b)


if __name__ == "__main__":
    n = 1000
    with open('students.scv', 'w') as fp:
        print('name', 'year', 'score', sep=',', file=fp)
        name = gen_name()
        year = gen_year(1, 4)
        score = gen_score(2, 5)
        for _ in range(n):
            print(next(name), next(year), next(score), sep=',', file=fp)
