# coding:utf-8
import timeit

popzero = timeit.Timer('x.pop(0)', 'from __main__ import x')
popend = timeit.Timer('x.pop()', 'from __main__ import x')

print('pop(0)    pop()')
for i in range(10000, 1000001, 20000):
    x = list(range(i))
    pz = popzero.timeit(number=1000)
    x = list(range(i))
    pe = popend.timeit(number=1000)
    print('%15.5f, %15.5f' % (pz, pe))
