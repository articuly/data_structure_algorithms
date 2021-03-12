# coding:utf-8

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, i):
        self.items.append(i)

    def lpop(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    q = Queue()
    print(q.is_empty())
    q.push('apple')
    q.push(123)
    q.push('car')
    print(q.size())
    print(q.is_empty())
    print(q.lpop())
    print(q.lpop())
    print(q.size())
    print(q.lpop())
    print(q.is_empty())
