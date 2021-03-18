# coding:utf-8

# 类似我理牌的过程
def selection_sort(lst):
    for fillslot in range(len(lst) - 1, 0, -1):
        position_max = 0

        # 每轮找到最大位索引
        for location in range(1, fillslot + 1):
            if lst[location] > lst[position_max]:
                position_max = location

        temp = lst[fillslot]
        lst[fillslot] = lst[position_max]
        lst[position_max] = temp
    return lst


if __name__ == '__main__':
    lst = [2, 56, 34, 21, 77, 33, 12, 6, 99, 36]
    print(selection_sort(lst))
