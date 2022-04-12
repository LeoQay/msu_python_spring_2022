class CustomList(list):
    """
    Works only with numeric values, int or float or similar
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)

    def __str__(self):
        return f"{super().__str__()}, sum={sum(self)}"

    def __add__(self, other):
        return self.do_op(other, lambda a, b: a + b)

    def __radd__(self, other):
        return self.do_op(other, lambda a, b: b + a)

    def __sub__(self, other):
        return self.do_op(other, lambda a, b: a - b)

    def __rsub__(self, other):
        return self.do_op(other, lambda a, b: b - a)

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
        return sum(other) < sum(self)

    def __rle__(self, other):
        return sum(other) <= sum(self)

    def __req__(self, other):
        return sum(other) == sum(self)

    def __rne__(self, other):
        return sum(other) != sum(self)

    def __rgt__(self, other):
        return sum(other) > sum(self)

    def __rge__(self, other):
        return sum(other) >= sum(self)

    def do_op(self, other, operation):
        result = CustomList()

        min_len = min(len(self), len(other))
        max_len = max(len(self), len(other))

        for i in range(min_len):
            result.append(operation(self[i], other[i]))

        if len(self) > len(other):
            for i in range(min_len, max_len):
                result.append(operation(self[i], 0))
        elif len(self) < len(other):
            for i in range(min_len, max_len):
                result.append(operation(0, other[i]))

        return result
