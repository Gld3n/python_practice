from multiprocessing import Process, Value, Array, Lock, current_process
from os import cpu_count
import time

def greet(name):
    for i in range(10):
        print(f"Hello {name} from process: {current_process().name}")
        time.sleep(0.1)

if __name__ == '__main__':
    processes = []
    num_processes = cpu_count()

    # create processes
    for _ in range(num_processes):
        process = Process(target=greet, args=("Robert",))
        processes.append(process)
        
    # start processes
    for p in processes:
        p.start()
        
    # join processes
    for p in processes:
        p.join()
        
    print("Hello from main")
    
    
#! last example contains a RC. For this we use Lock as well as the threading package 
""" 
* With processes the shared values are accessed with the Value or Array modules since
* they don't live in the same memory space as the threads. 
*** Value example 
"""

def add(n, lock):
    for _ in range(100):
        time.sleep(0.01)
        with lock:
            n.value += 1

if __name__ == '__main__':
    shared_value = Value('i', 0)
    lock = Lock()
    
    print(f"\nShared number at the beginning: {shared_value.value}")

    p1 = Process(target=add, args=(shared_value, lock))
    p2 = Process(target=add, args=(shared_value, lock))

    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print(f"\nShared number at the end: {shared_value.value}")


#*** Array example
def add2(n_array, lock):
    for _ in range(100):
        time.sleep(0.01)
        for i in range(len(n_array)):
            with lock:
                n_array[i] += 1

if __name__ == '__main__':
    lock = Lock()
    shared_array = Array('i', [0, 100, 200])
    
    print(f"\nShared array at the beginning: {shared_array[:]}")

    p1 = Process(target=add2, args=(shared_array, lock))
    p2 = Process(target=add2, args=(shared_array, lock))

    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print(f"\nShared array at the end: {shared_array[:]}")
    
    
#! Queues can also be used with Processes, and they're built-in in the multiprocessing
#! package unlike the multithreading one

from multiprocessing import Queue

def squared(nums, q):
    for n in nums:
        q.put(n*n)
        
def make_negative(nums, q):
    for n in nums:
        q.put(-1*n)

if __name__ == '__main__':
    nums = range(1, 11)
    q = Queue()

    p1 = Process(target=squared, args=(nums, q))
    p2 = Process(target=make_negative, args=(nums, q))

    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    while not q.empty():
        print(q.get())