import threading

from multithreading.count_three_sum import read_ints, count_three_sum
from multithreading.decorators import measure_time


@measure_time
def run_in_parallel():
    t1 = threading.Thread(target=count_three_sum, daemon=True, args=(ints, 't1'))
    t2 = threading.Thread(target=count_three_sum, daemon=True, args=(ints, 't2'))

    t1.start()
    t2.start()

    print("\nGoing to wait for threads ")

    t1.join()
    t2.join()

@measure_time
def run_sequentially(ints):
    count_three_sum(ints)
    count_three_sum(ints)


if __name__ == '__main__':
    print('started main')

    ints = read_ints("1Kints.txt")

    run_in_parallel(ints)
    run_sequentially(ints)

    print('ended main')
