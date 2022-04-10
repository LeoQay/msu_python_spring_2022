class CustomList(list):
    """
    Works only with numeric values, int or float or similar
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.change_len = 0
        self.self_up = False
        self.oth_up = False

    def reset_fields(self):
        self.change_len = 0
        self.self_up = False
        self.oth_up = False

    def __str__(self):
        result = super().__str__()
        return f'Custom List: {result}, sum={sum(self)}'

    def __add__(self, other):
        return self.do_op(other, lambda a, b: a + b)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self.do_op(other, lambda a, b: a - b)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __rlt__(self, other):
        return sum(self) < sum(other)

    def __rle__(self, other):
        return sum(self) <= sum(other)

    def __req__(self, other):
        return sum(self) == sum(other)

    def __rne__(self, other):
        return sum(self) != sum(other)

    def __rgt__(self, other):
        return sum(self) > sum(other)

    def __rge__(self, other):
        return sum(self) >= sum(other)

    def do_op(self, other, operation):
        result = CustomList()

        other = CustomList(other)

        change_len = len(self) - len(other)
        self_up = False
        oth_up = False

        if change_len > 0:
            oth_up = True
            other.append_zeros(change_len)
        elif change_len < 0:
            self_up = True
            change_len *= -1
            self.append_zeros(change_len)

        for self_val, other_val in zip(self, other):
            result.append(operation(self_val, other_val))

        if oth_up:
            other.pop_back(change_len)
        elif self_up:
            self.pop_back(change_len)

        self.reset_fields()

        return result

    def append_zeros(self, amount: int):
        if amount < 0:
            raise ValueError('Negative argument')
        for _ in range(amount):
            self.append(0)

    def pop_back(self, amount: int):
        if amount < 0:
            raise ValueError('Negative argument')
        for _ in range(amount):
            self.pop(-1)


if __name__ == '__main__':
    cus1 = CustomList([1, 2, 3, 5])
    cus2 = CustomList([2, 3, 4])
    print([1, 23] > cus1)
    print(cus1 + cus2 - cus1)
    print(cus1)
    print(cus2)
