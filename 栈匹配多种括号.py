# coding:utf-8
from 列表实现栈 import Stack


def brackets_checker(string):
    s = Stack()
    balanced = True
    index = 0

    while index < len(string) and balanced:
        symbol = string[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if not s.is_empty():
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
            else:
                balanced = False
        index += 1

    if balanced and s.is_empty():
        return True
    else:
        return False


def matches(open, close):
    opens = '([{'
    closes = ')]}'
    return opens.index(open) == closes.index(close)


if __name__ == '__main__':
    print(brackets_checker('(){}[]'))
    print(brackets_checker('{{[()]}}'))
    print(brackets_checker('{[]}(())[]'))
    print(brackets_checker('[()][{{}}]]'))
