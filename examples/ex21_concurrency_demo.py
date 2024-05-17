import time
from threading import Thread, current_thread


def do_mutli_stuff(args_list):
    for each_args in args_list:
        tx = Thread(target=the_task, args=each_args[:-1], name=each_args[-1])
        tx.start()


def task1():
    for i in range(15):
        print(f'task 1 is being executed - {i} in the thread {current_thread().name}')
        time.sleep(0.1)


def task2():
    for i in range(15):
        print(f'another task #2 is being executed - {i} in the thread {current_thread().name}')
        time.sleep(0.1)


def the_task(limit, message, duration):
    for i in range(limit):
        print(f'{message} - {i} in the thread {current_thread().name}')
        time.sleep(duration)


def main():
    print(f'start of main() in the thread {current_thread().name}')
    # task1()
    # task2()
    t1 = Thread(target=task1, name="task1")
    t2 = Thread(target=task2, name="task2")

    args_list = [(10, 'this is the customizable task', 0.25, 'task4'),
                 (10, 'this is the 2nd task being customized', 0.15, 'task5')]
    do_mutli_stuff(args_list)
    #  target(*args)
    #  the_task(10, 'this is the customizable task', 0.25)

    t1.start()
    t2.start()
    # t3.start()
    print(f'end of main() in the thread {current_thread().name}')


if __name__ == '__main__':
    main()
