class CustomList(list):
    def __init__(self):
        super().__init__()

    def __add__(self, other):
        result = CustomList()



        return result

    def append_zeros(self, amount: int):
        if amount < 0:
            raise ValueError('Negative argument')
        for i in range(amount):
            self.append(0)
