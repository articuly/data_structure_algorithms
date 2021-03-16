# coding:utf-8

def listsum(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + listsum(lst[1:])


if __name__ == '__main__':
    print(listsum([1, 2, 3, 4, 5, 6, 7, 8, 9]))
