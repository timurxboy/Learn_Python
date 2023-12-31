import threading
import time

a = 5
b = 5

a_lock = threading.Lock()
b_lock = threading.Lock()


def thread1calc():
    global a
    global b

    print('Thread1 acquiring lock a')
    a_lock.acquire()
    time.sleep(5)

    print('Thread1 acquiring lock b')
    a_lock.acquire()
    time.sleep(5)

    a += 5
    b += 5

    print('Thread1 releasing both lick')
    a_lock.release()
    b_lock.release()

    
def thread2calc():
    global a
    global b

    print('Thread2 acquiring lock a')
    a_lock.acquire()
    time.sleep(5)

    print('Thread2 acquiring lock b')
    a_lock.acquire()
    time.sleep(5)

    a += 10
    b += 10

    print('Thread2 releasing both lick')
    a_lock.release()
    b_lock.release()


