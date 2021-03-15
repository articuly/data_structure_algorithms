# coding:utf-8
import random
from 列表实现队列 import Queue


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm  # 每分钟打印页数
        self.current_task = None
        self.time_remain = 0

    def tick(self):  # 打印运行
        if self.current_task is not None:
            self.time_remain -= 1
            if self.time_remain <= 0:
                self.current_task = None

    def busy(self):  # 打印忙
        if self.current_task is not None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remain = new_task.get_pages() * new_task.get_quality() * 60 / self.pagerate


class Task:
    def __init__(self, time, max_pages):
        self.timestamp = time
        self.pages = random.randrange(1, max_pages + 1)
        self.quality = random.randint(quality_range[0], quality_range[1] + 1)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def get_quality(self):
        return self.quality

    def wait_time(self, current_time):
        return current_time - self.timestamp


def simulation(num_seconds, ppm):
    printer = Printer(ppm)
    print_q = Queue()
    waiting_time = []

    for current_second in range(num_seconds):
        if new_print_task(student_num):
            task = Task(current_second, max_pages)
            print_q.push(task)
        if (not printer.busy()) and (not print_q.is_empty()):
            next_task = print_q.lpop()
            waiting_time.append(next_task.wait_time(current_second))
            printer.start_next(next_task)
        printer.tick()

    average_waiting = sum(waiting_time) / len(waiting_time)
    print('Average Wait {0:6.2f}s {1:3d} tasks remaining.'.format(average_waiting, print_q.size()))
    return average_waiting


def new_print_task(student_num):
    # 平均每180秒有一个打印任务
    task_per_second = 1800 / student_num
    num = random.randrange(1, task_per_second + 1)
    if num == task_per_second:
        return True
    else:
        return False


if __name__ == '__main__':
    quality_range = [1, 2]  # 打印质量，后者为前者消耗倍数
    student_num = 10  # 学生数量
    max_pages = 20  # 最大打印页数
    average_waiting_list = []
    for i in range(100):
        average_waiting_list.append(simulation(3600, 10))
    print(sum(average_waiting_list) / len(average_waiting_list))
