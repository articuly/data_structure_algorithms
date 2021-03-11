# coding:utf-8
from 列表实现栈 import Stack


def bracket_check(string):
    s = Stack()
    balanced = True
    index = 0

    while index < len(string) and balanced:
        symbol = string[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if not s.is_empty():
                s.pop()
            else:
                balanced = False
        index += 1

    if balanced and s.is_empty():
        return True
    else:
        return False


if __name__ == '__main__':
    print(bracket_check('((()))'))
    print(bracket_check('(())())'))
    print(bracket_check('()())('))
    print(bracket_check('()()()'))
