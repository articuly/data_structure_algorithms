# coding:utf-8
from 列表实现栈 import Stack


def base_convert(num, base):
    convert_str = '0123456789ABCDEF'
    if num < base:
        return convert_str[num]
    else:
        return base_convert(num // base, base) + convert_str[num % base]


def base_convert_stack(num, base):
    convert_str = '0123456789ABCDEF'

    if num < base:
        stack.push(convert_str[num])
    else:
        stack.push(convert_str[num % base])
        base_convert_stack(num // base, base)


if __name__ == '__main__':
    print(base_convert(5, 2))
    print(base_convert(6, 2))
    print(base_convert(10, 2))
    print(base_convert(14, 12))
    print(base_convert(17, 16))
    print(base_convert(13, 16))
    print(base_convert(13, 8))

    stack = Stack()
    base_convert_stack(10, 2)
    new_str = ''
    while not stack.is_empty():
        new_str += stack.pop()
    print(new_str)
