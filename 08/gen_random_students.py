import random
import names


def gen_score(left: float, right: float):
    while True:
        yield round(random.uniform(left, right), 2)


def gen_name():
    while True:
        yield names.get_full_name()


def gen_year(left: int, right: int):
    while True:
        yield random.randint(left, right)


if __name__ == "__main__":
    AMOUNT = 1000
    with open('students.scv', 'w', encoding='utf-8') as fp:
        print('name', 'year', 'score', sep=',', file=fp)
        name = gen_name()
        year = gen_year(1, 4)
        score = gen_score(2, 5)
        for _ in range(AMOUNT):
            print(next(name), next(year), next(score), sep=',', file=fp)
