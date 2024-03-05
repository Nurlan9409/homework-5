import time
from datetime import datetime

def task_4():
    time.sleep(7)
    return "Task 4 "


def task_3():
    time.sleep(2)
    return "Task 3 "


def task_2():
    time.sleep(5)
    return "Task 2 "


def task_1():
    time.sleep(2)
    return "Task 1 "


def main():
    print(task_4())
    print(task_1())
    print(task_3())
    print(task_2())


if __name__ == "__main__":
    print(datetime.now().time())
    main()
    print(datetime.now().time())
