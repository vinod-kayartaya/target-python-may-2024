import time
from threading import Thread, current_thread, Lock


lock = Lock()


def task1():
    for i in range(5):
        print(f'{current_thread().name}: loop = 1, loop count = {i}')
        time.sleep(0.01)

    with lock:
        for i in range(5):
            print(f'{current_thread().name}: loop = 2, loop count = {i}')
            time.sleep(0.01)

    for i in range(5):
        print(f'{current_thread().name}: loop = 3, loop count = {i}')
        time.sleep(0.01)


def main():
    print("start of main()")

    Thread(target=task1, name="TASK#1").start()
    Thread(target=task1, name="TASK#2").start()

    print("end of main()")


if __name__ == '__main__':
    main()

