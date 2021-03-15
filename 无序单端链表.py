# coding:utf-8

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class UnorderedLinkedList:
    def __init__(self):
        self.head = None
        self.__length = 0

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        self.__length += 1

    def append(self, item):
        temp = Node(item)
        current = self.head
        while current.next is not None:
            current = current.next
        current.set_next(temp)
        self.__length += 1

    def size(self):
        return self.__length

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.next
        return found

    def index(self, item):
        current = self.head
        pos = 0
        while current is not None:
            if current.get_data() == item:
                if pos < self.__length:
                    return pos
            else:
                pos += 1
                current = current.next
        return -1

    def insert(self, pos, item):
        if pos == 0:
            self.add(item)
        elif pos >= self.__length:
            self.append(item)
        else:
            temp = Node(item)
            previous = None
            current = self.head
            for i in range(pos):
                previous = current
                current = current.next
            previous.set_next(temp)
            temp.set_next(current)
            self.__length += 1

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:  # 在第一个找到删除的元素
            self.head = current.get_next()
            self.__length -= 1
        else:
            previous.set_next(current.get_next())
            self.__length -= 1

    def pop(self, pos=None):
        current = self.head
        previous = None
        if pos is not None:
            for i in range(pos):
                previous = current
                current = current.next

            if previous is None:
                temp = self.head.get_data()
                self.head = current.get_next()
                self.__length -= 1
                return temp
            else:
                temp = current.get_data()
                previous.set_next(current.get_next())
                self.__length -= 1
                return temp

        else:
            for i in range(self.__length - 1):
                previous = current
                current = current.next
            temp = current.get_data()
            previous.set_next(current.get_next())
            self.__length -= 1
            return temp


if __name__ == '__main__':
    ull = UnorderedLinkedList()
    print(ull.is_empty())
    ull.add(31)
    ull.add(77)
    ull.add(17)
    ull.add(93)
    ull.add(26)
    ull.add(54)
    ull.append(123)
    ull.append(234)
    print(ull.size())
    print(ull.search(12))
    print(ull.search(123))
    print(ull.index(123))
    print(ull.index(77))
    ull.insert(3, 33)
    ull.remove(234)
    print(ull.pop())
    print(ull.size())
    print(ull.pop(3))
    print(ull.size())
