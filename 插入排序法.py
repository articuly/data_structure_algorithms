# coding:utf-8

def insertion_sort(lst):
    for index in range(1, len(lst)):
        current = lst[index]
        position = index

        while position > 0 and lst[position - 1] > current:
            lst[position] = lst[position - 1]  # 右移一们
            position -= 1

        lst[position] = current  # 当前值归位
    return lst


if __name__ == '__main__':
    lst = [2, 56, 34, 21, 77, 33, 12, 6, 99, 36]
    print(insertion_sort(lst))
