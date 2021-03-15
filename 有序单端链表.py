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


class OrderedLinkedList:
    def __init__(self):
        self.head = None
        self.__length = 0

    def is_empty(self):
        return self.head is None

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.next

        temp = Node(item)
        if previous is None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)
        self.__length += 1

    def size(self):
        return self.__length

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
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
    oll = OrderedLinkedList()
    print(oll.is_empty())
    oll.add(31)
    oll.add(77)
    oll.add(17)
    oll.add(93)
    oll.add(26)
    oll.add(54)
    print(oll.size())
    print(oll.search(26))
    print(oll.search(123))
    print(oll.index(26))
    print(oll.index(77))
    print(oll.pop())
    print(oll.size())
    print(oll.pop(3))
    print(oll.size())
