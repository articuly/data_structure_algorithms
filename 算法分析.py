# coding:utf-8
from cost_time import cost_time


@cost_time
def sum_n(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
    return s


@cost_time
def foo(n):
    s = 0
    for i in range(1, n + 1):
        tmp = i
        s = s + tmp
    return s


@cost_time
def sum_formula(n):
    return n * (n + 1) / 2


# sum_n比foo占用更少的资源，算法分析就是解决问题用的时间和空间
if __name__ == '__main__':
    for i in range(5):
        sum_n(1000000)
    print("------------")
    for i in range(5):
        foo(1000000)
    print("------------")
    for i in range(5):
        sum_formula(1000000)
    print("------------")
