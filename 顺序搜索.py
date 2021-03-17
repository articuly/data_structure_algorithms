# coding:utf-8
import numpy as np
from cost_time import cost_time


@cost_time
def sequential_search(lst, item):
    pos = 0
    found = False
    while pos < len(lst) and not found:
        if lst[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found


@cost_time
def ordered_sequential_search(lst, item):
    pos = 0
    found = False
    stop = False
    while pos < len(lst) and not found and not stop:
        if lst[pos] == item:
            found = True
        else:
            if lst[pos] > item:
                stop = True
            else:
                pos += 1
    return found


if __name__ == '__main__':
    unordered_list = np.random.randint(1, 1001, size=10000).tolist()
    ordered_list = sorted(unordered_list)
    item = 255
    print(sequential_search(unordered_list, item))
    print(ordered_sequential_search(ordered_list, item))
