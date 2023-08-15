import threading
import time

from multithreading.count_three_sum import read_ints

should_stop = False


def count_three_sum(ints):
    print('started count_three_sum')

    n = len(ints)
    counter = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if should_stop:
                    print('Task was Cancelled')
                    counter = -1
                    return counter

                if ints[i] + ints[j] + ints[k] == 0:
                    counter += 1
                    print(f'Triple found:{ints[i], ints[j], ints[k]}')

    print(f'ended count_three_sum. Triplets counter={counter}')
    return counter

if __name__ == '__main__':
    print('Starter main')

    ints = read_ints('1Kints.txt')

    p = threading.Thread(target=count_three_sum, args=(ints,))
    p.start()

    time.sleep(5)
    should_stop = True


    print('ended main')
