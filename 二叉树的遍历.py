# coding:utf-8
from 二叉树类 import BinaryTree


def preorder(tree):
    if tree is not None:
        print(tree.get_root_value())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


def postorder(tree):
    if tree is not None:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_value())


def inorder(tree):
    if tree is not None:
        inorder(tree.get_left_child())
        print(tree.get_root_value())
        inorder(tree.get_right_child())
