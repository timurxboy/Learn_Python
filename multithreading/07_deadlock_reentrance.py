import threading

lock_obj = threading.RLock()

print('Acquaire 1nd time')
lock_obj.acquire()

print('Acquaire 2nd time')
lock_obj.acquire()

print('Releasing')
lock_obj.release()
