# coding:utf-8

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val, parent=current_node)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):  # 相当于搜索
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):  # 语句为：x in Tree
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            node_remove = self._get(key, self.root)
            if node_remove:
                self.remove(node_remove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, current_node):
        if current_node.is_leaf():  # 叶子节点，看是左叶还是右叶
            if current_node == current_node.parent.left:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None

        elif current_node.has_both_children():  # 有两个子节点，找后代节点替换
            success = current_node.find_successor()
            success.splice_out()
            current_node.key = success.key
            current_node.payload = success.payload

        else:  # 只有一个子节点
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:  # 当前是根节点
                    current_node.replace_node_data(current_node.left_child.key, current_node.left_child.payload,
                                                   current_node.left_child.left_child,
                                                   current_node.left_child.right_child)
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:  # 当前是根节点
                    current_node.replace_node_data(current_node.right_child.key, current_node.right_child.payload,
                                                   current_node.right_child.left_child,
                                                   current_node.right_child.right_child)


class AVLTree(BinarySearchTree):
    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val, parent=current_node)
                self.update_balance(current_node.left_child)
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val, parent=current_node)
                self.update_balance(current_node.right_child)

    def update_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.reblance(node)
            return
        if node.parent is not None:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def reblance(self, node):
        if node.balance_factor < 0:  # 右倾
            if node.right_child.balance_factor > 0:  # 左倾
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        elif node.balance_factor > 0:
            if node.left_child.balance_factor < 0:
                self.rotate_left(node.left_child)
                self.rotate_right(node)
            else:
                self.rotate_right(node)

    def rotate_left(self, root):
        new_root = root.right_child
        root.right_child = new_root.left_child
        if new_root.left_child is not None:
            new_root.left_child.parent = root
        new_root.parent = root.parent
        if root.is_root():
            self.root = new_root
        else:
            if root.is_left_child():
                root.parent.left_child = new_root
            else:
                root.parent.right_child = new_root

        new_root.left_child = root
        root.pare = new_root
        root.balance_factor = root.balance_factor + 1 - min(new_root.block_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(root.balance_factor, 0)


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.pay_load = val
        # 像链表指明关系
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def __iter__(self):
        if self:
            if self.has_left_child():
                for el in self.left_child:  # 递归调用生成器
                    yield el
            yield self.key
            if self.has_right_child():  # 递归调用生成器
                for el in self.right_child:
                    yield el

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):  # 叶子节点无子节点
        return not (self.left_child or self.right_child)

    def has_any_children(self):
        return self.left_child or self.right_child

    def has_both_children(self):
        return self.left_child and self.right_child

    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.pay_load = value
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def find_successor(self):
        success = None
        if self.has_right_child():
            success = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    success = self.parent
                else:
                    self.parent.right_child = None
                    success = self.parent.find_successor()
                    self.parent.right_child = self
        return success

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current

    def split_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent
