# coding:utf-8
import numpy as np
from cost_time import cost_time


@cost_time
def binary_search(lst, item):
    first = 0
    last = len(lst) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if lst[midpoint] == item:
            found = True
        else:
            if item < lst[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


# 递归版本
@cost_time
def binary_search2(lst, item):
    if len(lst) == 0:
        return False
    else:
        midpoint = len(lst) // 2

        if lst[midpoint] == item:
            return True
        else:
            if item < lst[midpoint]:
                return binary_search2(lst[:midpoint], item)
            else:
                return binary_search2(lst[midpoint + 1:], item)


if __name__ == '__main__':
    unordered_list = np.random.randint(1, 20001, size=10000).tolist()
    ordered_list = sorted(unordered_list)
    print(ordered_list)
    item = 255
    print(binary_search(ordered_list, item))
    print(binary_search2(ordered_list, item))
