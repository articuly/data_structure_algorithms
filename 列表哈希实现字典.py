# coding:utf-8
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, self.size)

        if self.slots[hashvalue] is None:  # 空槽插入
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:  # 同键替换
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue, self.size)
                while self.slots[nextslot] is not None and self.slots[nextslot] != key:
                    # 槽非空且键不相同时，继续寻找下一个槽
                    nextslot = self.rehash(nextslot, self.size)

                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

    def get(self, key):
        startslot = self.hashfunction(key, self.size)
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, self.size)
                if position == startslot:  # 找了一遍，没找到则停止
                    stop = True
        return data

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


if __name__ == '__main__':
    h = HashTable()
    h[54] = 'cat'
    h[26] = 'dog'
    h[93] = 'lion'
    h[17] = 'tiger'
    h[77] = 'bird'
    h[31] = 'cow'
    h[44] = 'goat'
    h[55] = 'pig'
    h[20] = 'chicken'
    print(h.slots)
    print(h.data)
    print(h[20])
    print(h[17])
    print(h[44])
    print(h[55])
