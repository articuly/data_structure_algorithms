# coding:utf-8
import timeit
import random

for i in range(10000, 1000001, 20000):
    t = timeit.Timer('random.randrange({}) in x'.format(i), 'from __main__ import random, x')

    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j: None for j in range(i)}
    dct_time = t.timeit(number=1000)

    print("{0}, {1:10.4f}, {2:10.4f}".format(i, lst_time, dct_time))
