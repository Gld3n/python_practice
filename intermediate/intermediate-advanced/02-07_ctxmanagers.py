from threading import Lock, Thread, current_thread
from time import sleep
from random import randint

def add_with_sqrd(a, b, lock):
    #! ctx manager
    with lock:
        result = a*a + b*b
        print(f"### ({a}*{a}) + ({b}*{b}) = {result} - from {current_thread().name} ###")
        sleep(0.1)

if __name__ == "__main__":
    lock = Lock()
    threads = []
    n_threads = 9
    
    for i in range(n_threads):
        thread = Thread(target=add_with_sqrd, args=(randint(20, 40), 
                                                    randint(20, 40),
                                                    lock))
        threads.append(thread)
        
    for t in threads:
        t.start()

    for t in threads:
        t.join()
        
    print("The end.")
    
#TODO: Learn more about context managers