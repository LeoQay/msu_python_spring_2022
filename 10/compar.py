import cffi


ffi = cffi.FFI()
lib = ffi.dlopen('/home/leonid/PycharmProjects/msu_python_spring_2022/10/mullib.so')
ffi.cdef('''void mul(int * a, int * b, int * res, int n, int m, int k);''')


class Matrix:
    def __init__(self, py_obj=None):
        self.shape = (0, 0)
        if py_obj is None or len(py_obj) == 0 or len(py_obj[0]) == 0:
            self.arr = None
            return
        self.shape = (len(py_obj), len(py_obj[0]))
        for line in py_obj:
            if len(line) != self.shape[1]:
                raise ValueError('Wrong number of columns')
        self.arr = ffi.new('int[]', [elem for line in py_obj for elem in line])

    def __getitem__(self, item):
        for ind in range(2):
            if not (0 <= item[ind] < self.shape[ind]):
                raise KeyError('Wrong key')
        return self.arr[item[0] * self.shape[1] + item[1]]

    def __mul__(self, other):
        if self.shape[1] != other.shape[0]:
            raise ValueError('Incompatible shapes')
        if self.shape[0] == 0 or other.shape[0] == 0:
            return Matrix()
        result = Matrix.fill((self.shape[0], other.shape[1]))
        lib.mul(self.arr, other.arr, result.arr, self.shape[0], self.shape[1], other.shape[1])
        return result

    def to_list(self):
        return [[self[ind, jnd] for jnd in range(self.shape[1])] for ind in range(self.shape[0])]

    def __str__(self):
        return str(self.to_list())

    @staticmethod
    def fill(shape, value=0):
        if type(value) != int:
            raise TypeError('Value must be int')
        if shape[0] == 0 or shape[1] == 0:
            shape = (0, 0)
        return Matrix([[value for _ in range(shape[1])] for _ in range(shape[0])])


if __name__ == "__main__":
    a = Matrix([[1, 2], [3, 4]])
    b = a * a
    print(b)

