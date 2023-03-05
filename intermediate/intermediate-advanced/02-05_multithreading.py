from threading import Thread, Lock, current_thread
from queue import Queue
import time


def greet():
    thread = 0
    for i in range(100):
        # print(f"Hello Messi from thread: {thread}")
        thread += 1

if __name__ == '__main__':
    threads = []
    num_threads = 10

    # create threads
    for _ in range(num_threads):
        thread = Thread(target=greet)
        threads.append(thread)
        
    # start threads
    for t in threads:
        t.start()
        
    # join threads: wait for them to finish
    for t in threads:
        t.join()
        
    # main process will execute after all the joined threads finish    
    print("Hello from main")
    
    
#! the last example contains a race condition. To avoid it, Lock package is used

db_value = 0

def increase(lock):
    global db_value
    
    # locking the state so the threads cannot switch or read from the same var simultanously 
    lock.acquire()
    db_copy = db_value
    
    # db processing simulation...
    
    db_copy += 1
    time.sleep(0.1)
    db_value = db_copy
    
    # not releasing could -and most likely will- cause a deadlock  
    lock.release()
    
if __name__ == "__main__":
    lock = Lock()
    print(f"Start value: {db_value}")
    
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print(f"End value: {db_value}")
    
    
#! there's an even better and thread-safe method to use threads: Queues

def worker(q, lock):
    while True:
        val = q.get()
        with lock:
            print(f"{current_thread().name} got: {val}")
            time.sleep(0.1)
        q.task_done()
    
if __name__ == "__main__":
    q = Queue()
    lock = Lock()
    n_threads = 10
    
    for t in range(n_threads):
        thread = Thread(target=worker, args=(q, lock))
        #* a daemon thread will die when the main thread die
        thread.daemon = True
        thread.start()
        
    for i in range(1, 21):
        q.put(i)
        
    q.join()
    
    print("End main")