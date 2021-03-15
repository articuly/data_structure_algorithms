# coding:utf-8

class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def lpush(self, i):
        self.items.insert(0, i)

    def lpop(self):
        return self.items.pop(0)


if __name__ == '__main__':
    d = Deque()
    print(d.is_empty())
    d.push(4)
    d.push('dog')
    d.lpush('cat')
    d.lpush(True)
    print(d.size())
    print(d.is_empty())
    d.push(8.4)
    print(d.pop())
    print(d.lpop())
