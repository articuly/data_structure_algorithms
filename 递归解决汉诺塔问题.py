# coding:utf-8

def move_tower(height, A, B, C):
    if height >= 1:
        move_tower(height - 1, A, C, B)  # 把A塔上编号1~n-1的圆盘移动B上，以C显辅助塔
        move_disk(height, A, C)  # 把A塔上编号为n的圆盘移到C上
        move_tower(height - 1, B, A, C)  # 把B塔上1~n-1的圆盘移动C上，以A为辅助塔


def move_disk(disk_num, fp, tp):
    print("Moving disk {} from {} to {}".format(disk_num, fp, tp))


if __name__ == '__main__':
    move_tower(3, 'A', 'B', 'C')
