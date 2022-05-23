#include <stdlib.h>


struct Matrix
{
	int * arr;
	size_t n;
	size_t m;
};


void mul(int * a, int * b, int * res, int n, int m, int k)
{
	int * ptr = res;
	for (int l = 0; l < n; ++l)
	{
		for (int p = 0; p < k; ++p, ++ptr)
		{
			int sum = 0;
			int * ptr_a = a + m * l;
			int * ptr_b = b + p;
			for (int i = 0; i < m; ++i, ++ptr_a, ptr_b += k)
			{
				sum += (*ptr_a) * (*ptr_b);
			}
			*ptr = sum;
		}
	}
}


void set(int * ptr, int val)
{
    *ptr = val;
}

int get(int * ptr)
{
    return *ptr;
}



void mat_mul(struct Matrix a, struct Matrix b, struct Matrix c)
{
        mul(a.arr, b.arr, c.arr, a.n, a.m, b.m);
}


