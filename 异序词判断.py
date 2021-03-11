# coding:utf-8

from cost_time import cost_time
import random


# 清点法，复杂度n^2/2
@cost_time
def anagram_solution1(str1, str2):
    lst2 = list(str2)
    pos1 = 0
    still_ok = True

    while pos1 < len(str1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(lst2) and not found:
            if str1[pos1] == lst2[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        if found:
            lst2[pos2] = None
        else:
            still_ok = False
        pos1 = pos1 + 1

    return still_ok


# 排序法，复杂度(2n^2~2nlogn)+2n
@cost_time
def anagram_solution2(str1, str2):
    lst1 = list(str1)
    lst2 = list(str2)
    lst1.sort()
    lst2.sort()
    pos = 0
    matches = True

    while pos < len(str1) and matches:
        if lst1[pos] == lst2[pos]:
            pos += 1
        else:
            matches = False

    return matches


# 计数法，复杂度2n+26
@cost_time
def anagram_solution3(str1, str2):
    lst1 = [0] * 26
    lst2 = [0] * 26

    for i in range(len(str1)):
        pos = ord(str1[i]) - ord('a')
        lst1[pos] += 1

    for i in range(len(str2)):
        pos = ord(str2[i]) - ord('a')
        lst2[pos] += 1

    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if lst1[j] == lst2[j]:
            j += 1
        else:
            still_ok = False

    return still_ok


if __name__ == '__main__':
    str_list = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    str1 = ''
    for i in range(20000):
        str1 += random.choice(str_list)
    lst2 = list(str1)
    random.shuffle(lst2)
    str2 = ''.join(lst2)
    print(str1, str2)

    for i in range(3):
        anagram_solution1(str1, str2)  # 7s for 10000, 27s for 20000
    print('------------')
    for i in range(3):
        anagram_solution2(str1, str2)  # less than 1s
    print('------------')
    for i in range(3):
        anagram_solution3(str1, str2)  # les than 1s
    print('------------')
