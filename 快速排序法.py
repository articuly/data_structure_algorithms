# coding:utf-8
def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist) - 1)


def quick_sort_helper(lst, first, last):
    if first < last:
        split_point = partition(lst, first, last)
        quick_sort_helper(lst, first, split_point - 1)
        quick_sort_helper(lst, split_point + 1, last)


def partition(lst, first, last):
    pivotvalue = lst[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:
        while leftmark <= rightmark and lst[leftmark] <= pivotvalue:
            leftmark += 1
        while leftmark <= rightmark and lst[rightmark] >= pivotvalue:
            rightmark -= 1
        if rightmark < leftmark:
            done = True
        else:
            temp = lst[leftmark]
            lst[leftmark] = lst[rightmark]
            lst[rightmark] = temp

    temp = lst[first]
    lst[first] = lst[rightmark]
    lst[rightmark] = temp

    return rightmark


if __name__ == '__main__':
    lst = [2, 56, 34, 21, 77, 33, 12, 6, 99, 36]
    quick_sort(lst)
    print(lst)
