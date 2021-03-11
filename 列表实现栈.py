# coding:utf-8

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# 方法二，会比前一种慢一些
class Stack2:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, i):
        self.items.insert(0, i)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    s = Stack()
    print(s.is_empty())
    s.push('apple')
    s.push(120)
    s.push('101')
    print(s.peek())
    print(s.size())
    print(s.is_empty())
    print(s.pop())
    print(s.pop())
    print(s.size())
    print(s.pop())
    print(s.is_empty())
