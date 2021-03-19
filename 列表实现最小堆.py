# coding:utf-8
class HeapList:
    def __init__(self):
        self.heap = [0]
        self.current_size = 0

    def insert(self, item):
        self.heap.append(item)
        self.current_size += 1
        self.shift_up(self.current_size)

    def shift_up(self, i):
        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:  # 父节点大于子节点，则交换
                self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]
            i //= 2

    def del_min(self):
        val = self.heap[1]
        self.heap[1] = self.heap[self.current_size]  # 最后元素换到最顶
        self.current_size -= 1
        self.heap.pop()
        self.shift_down(1)
        return val

    def shift_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap[i] > self.heap[mc]:  # 父节点大于子节点，则交换
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:  # 只有左子节点
            return i * 2
        else:
            if self.heap[i * 2] < self.heap[i * 2 + 1]:  # 比较左右子节点
                return i * 2
            else:
                return i * 2 + 1

    def build_heap(self, lst):
        i = len(lst) // 2
        self.current_size = len(lst)
        self.heap = [0] + lst
        while i > 0:
            self.shift_down(i)
            i -= 1


if __name__ == '__main__':
    lst = [9, 5, 6, 2, 3]
    h = HeapList()
    h.build_heap(lst)
    print(h.heap)
