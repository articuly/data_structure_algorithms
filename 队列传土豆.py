# coding:utf-8

from 列表实现队列 import Queue


def hot_potato(namelist, num):
    q = Queue()
    for name in namelist:
        q.push(name)

    while q.size() > 1:
        for i in range(num):
            q.push(q.lpop())
        # q.lpop()
        print(q.lpop())  # 去除的那个
    return q.lpop()  # 剩下那个


if __name__ == '__main__':
    names = ['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad']
    print(hot_potato(names, 7))
