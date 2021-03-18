# coding:utf-8

def shell_sort(lst):
    sublistcount = len(lst) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gap_insertion_sort(lst, startposition, sublistcount)

        print('After increments of size', sublistcount, 'The list is ', lst)
        sublistcount = sublistcount // 2
    return lst


def gap_insertion_sort(lst, start, gap):
    for i in range(start + gap, len(lst), gap):
        current = lst[i]
        position = i

        while position >= gap and lst[position - gap] > current:
            lst[position] = lst[position - gap]
            position = position - gap
        lst[position] = current


if __name__ == '__main__':
    lst = [2, 56, 34, 21, 77, 33, 12, 6, 99, 36]
    print(shell_sort(lst))
