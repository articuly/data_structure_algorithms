# coding:utf-8
from 有向权重图类 import Graph


def build_graph(file):
    d = []
    g = Graph()
    wfile = open(file, 'r')
    # 创建词桶
    for line in wfile:
        word = line[:-1]
        pass


def _mul(x, y):
    return x * y


def _add(x, y):
    return x + y


if __name__ == '__main__':
    m = _mul
    a = _add
    d = {'mul': m, 'add': a}
    print(d['mul'](12, 13))
    print(d['add'](12, 13))
