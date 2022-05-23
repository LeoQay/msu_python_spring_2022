import cffi


ffi = cffi.FFI()
lib = ffi.dlopen('/home/leonid/PycharmProjects/msu_python_spring_2022/10/mullib.so')
ffi.cdef('''void mul(int * a, int * b, int * res, int n, int m, int k);''')
ffi.cdef('''void set(int * ptr, int val);''')
ffi.cdef('''int get(int * ptr);''')


class Matrix:
    def __init__(self, py_list):
        self.lines = len(py_list)
        self.cols = len(py_list[0])
        ar = []
        for 


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    c_arr = ffi.new('int[]', arr)
    res = [0, 0, 0, 0]
    c_res = ffi.new('int[]', res)
    lib.mul(c_arr, c_arr, c_res, 2, 2, 2)

