# coding:utf-8
def bubble_sort(lst):
    for passnum in range(len(lst) - 1, 0, -1):
        for i in range(passnum):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
    return lst


def short_bubble_sort(lst):
    exchange = True
    passnum = len(lst) - 1

    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if lst[i] > lst[i + 1]:
                exchange = True
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
        passnum -= 1
    return lst


if __name__ == '__main__':
    lst = [2, 56, 34, 21, 77, 33, 12, 6, 99, 36]
    print(bubble_sort(lst))
    print(short_bubble_sort(lst))
