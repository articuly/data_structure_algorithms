# coding:utf-8
from 列表实现双端队列 import Deque


def palchechker(string):
    d = Deque()

    for ch in string:
        d.push(ch)

    still_equal = True

    while d.size() > 1 and still_equal:
        first = d.lpop()
        last = d.pop()
        if first != last:
            still_equal = False

    return still_equal


if __name__ == '__main__':
    print(palchechker('print'))
    print(palchechker('hanah'))
