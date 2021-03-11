# coding:utf-8

from 列表实现栈 import Stack


def divide_by2(dec_number):
    s = Stack()

    while dec_number > 0:
        rem = dec_number % 2
        s.push(rem)
        dec_number = dec_number // 2

    bin_str = ''
    while not s.is_empty():
        bin_str += str(s.pop())

    return bin_str


def base_converter(dec_number, base):
    digits = '0123456789ABCDEF'

    s = Stack()

    while dec_number > 0:
        rem = dec_number % base
        s.push(rem)
        dec_number = dec_number // base

    new_str = ''
    while not s.is_empty():
        new_str += digits[s.pop()]

    return new_str


if __name__ == '__main__':
    print(divide_by2(5))
    print(divide_by2(6))
    print(base_converter(14, 12))
    print(base_converter(17, 16))
    print(base_converter(13, 16))
    print(base_converter(13, 8))
