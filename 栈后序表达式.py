# coding:utf-8
from 列表实现栈 import Stack
import string

"""
中序运算表达式转后序表达式
str1 = 'a * b + c' => ab*c+
str2 = '( a + b ) * c' => ab+c*
str3 = 'a * b + b * d' => ab*cd*+
"""


def infix_to_postfix(infix_expr):
    # 定义运算优先级
    prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    # 存放操作过程的栈
    stack = Stack()
    # 保存后序表达式的列表
    postfix_list = []
    # 默认用空格分开表达式
    token_list = infix_expr.split()

    for token in token_list:
        if token in (string.ascii_uppercase + string.ascii_lowercase):
            postfix_list.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            top = stack.pop()
            while top != '(':
                postfix_list.append(top)
                top = stack.pop()
        else:
            while (not stack.is_empty()) and (prec[stack.peek()] >= prec[token]):
                postfix_list.append(stack.pop())
            stack.push(token)

    while not stack.is_empty():
        postfix_list.append(stack.pop())

    return ' '.join(postfix_list)


if __name__ == '__main__':
    str1 = 'a * b + c'
    str2 = '( a + b ) * c'
    str3 = 'a * b + b * d'
    str4 = '( a + b ) * ( c + d )'
    print(infix_to_postfix(str1))
    print(infix_to_postfix(str2))
    print(infix_to_postfix(str3))
    print(infix_to_postfix(str4))
