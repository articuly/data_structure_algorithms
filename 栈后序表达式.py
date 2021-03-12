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


def postfix_eval(postfix_expr):
    stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token in string.digits:
            stack.push(int(token))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            result = calc(token, num1, num2)
            stack.push(result)
    return stack.pop()


def calc(op, n1, n2):
    if op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    elif op == '+':
        return n1 + n2
    else:
        return n1 - n2


if __name__ == '__main__':
    str1 = 'a * b + c'
    str2 = '( a + b ) * c'
    str3 = 'a * b + b * d'
    str4 = '( a + b ) * ( c + d )'
    print(infix_to_postfix(str1))
    print(infix_to_postfix(str2))
    print(infix_to_postfix(str3))
    print(infix_to_postfix(str4))
    expr1 = '5 6 * 4 +'
    expr2 = '9 3 + 2 *'
    expr3 = '1 2 * 3 4 * +'
    expr4 = '1 2 + 3 4 + *'
    print(postfix_eval(expr1))
    print(postfix_eval(expr2))
    print(postfix_eval(expr3))
    print(postfix_eval(expr4))
