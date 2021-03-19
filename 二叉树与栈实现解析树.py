# coding:utf-8
from 列表实现栈 import Stack
from 二叉树类 import BinaryTree
import operator


# 形成解析树
def build_parse_tree(expr):
    lst = expr.split()
    s = Stack()
    t = BinaryTree("")
    s.push(t)
    current_tree = t

    for i in lst:
        if i == '(':
            current_tree.insert_left('')
            s.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in '+-*/)':
            current_tree.set_root_value(eval(i))
            parent = s.pop()
            current_tree = parent
        elif i in '+-*/':
            current_tree.set_root_value(i)
            current_tree.insert_right('')
            s.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = s.pop()
        else:
            raise ValueError('Unknown Operator:' + i)
    return t


# 计算解析树的表达式
def evaluate(parse_tree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    left = parse_tree.get_left_child()
    right = parse_tree.get_right_child()

    if left and right:
        fn = opers[parse_tree.get_root_value()]
        return fn(evaluate(left), evaluate(right))
    else:
        return parse_tree.get_root_value()


# 用后序遍历法求解析的值
def postordereval(tree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    left = None
    right = None

    if tree:
        left = postordereval(tree.get_left_child())
        right = postordereval(tree.get_right_child())
        if left and right:
            return opers[tree.get_root_value()](left, right)
        else:
            return tree.get_root_value()


# 用中序遍历法还原表达式
def print_expr(tree):
    string = ''
    if tree:
        if tree.get_left_child():
            string = '(' + print_expr(tree.get_left_child())
        else:
            string = print_expr(tree.get_right_child())
        string += str(tree.get_root_value())
        if tree.get_right_child():
            string += print_expr(tree.get_right_child()) + ')'
        else:
            string += print_expr(tree.get_right_child())
    return string


if __name__ == '__main__':
    ex = '( 3 + ( 4 * 5 )'
    t = build_parse_tree(ex)
    print(evaluate(t))
    print(postordereval(t))
    print(print_expr(t))
