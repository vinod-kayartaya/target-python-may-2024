import threading
import time


def the_task(limit, the_sums):
    total = 0
    for i in range(limit):
        time.sleep(0.01)
        total += i

    print('appending the total', total)
    the_sums.append(total)


def main():
    the_sums = []
    print('start of main()')

    t1 = threading.Thread(target=the_task, args=(10, the_sums))
    t2 = threading.Thread(target=the_task, args=(15, the_sums))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print(the_sums)
    print('end of main()')


if __name__ == '__main__':
    main()

