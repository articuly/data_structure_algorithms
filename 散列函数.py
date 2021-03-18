# coding:utf-8
# 字体串构建散列函数
def str_hash(string, table_size):
    s = 0
    for pos in range(len(string)):
        print(ord(string[pos]))
        s += ord(string[pos])
    return s % table_size


if __name__ == '__main__':
    str1 = 'ABCDEF'
    table_size = 11
    print(str_hash(str1, table_size))
