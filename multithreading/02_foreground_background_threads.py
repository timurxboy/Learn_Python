import threading
import time

from multithreading.count_three_sum import read_ints, count_three_sum

if __name__ == '__main__':
    print('started main')

    ints = read_ints('1Kints.txt')
    t1 = threading.Thread(target=count_three_sum, args=(ints,), daemon=True)

    t1.start()
    # input('How are you')
    time.sleep(3)
    print('ended main')
