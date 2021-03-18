# coding:utf-8
def merge_sort(lst):
    print('Splitting', lst)
    if len(lst) > 1:
        mid = len(lst) // 2
        # 使用子列表，空间复杂度火n
        lefthalf = lst[:mid]
        righthalf = lst[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i, j, k = 0, 0, 0
        # 比较左右子列表，在合并过程中k从小变大，左右两边索引也在右移
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                lst[k] = lefthalf[i]
                i += 1
            else:
                lst[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            lst[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            lst[k] = righthalf[j]
            j += 1
            k += 1

    print('merging', lst)


if __name__ == '__main__':
    lst = [2, 56, 34, 21, 77, 33, 12, 6, 99, 36]
    merge_sort(lst)
