import time
# from threading import Thread
from multiprocessing import Process, Pool

# GIL - global interpreter lock

COUNT = 500_000_000

def countdown(n):
    while n > 0:
        n -= 1

# start = time.time()
# countdown(COUNT)
# end = time.time()

# print('Done in:', end - start)


t1 = Process(target=countdown, args=(COUNT//2,))
t2 = Process(target=countdown, args=(COUNT//2,))

start = time.time()

t1.start()
t2.start()
t1.join()
t2.join()

end = time.time()

print('Done in:', end - start)