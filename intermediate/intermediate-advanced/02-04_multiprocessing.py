from multiprocessing import Process
from os import cpu_count
import time

def greet():
    process = 0
    for i in range(100):
        print(f"Hello Messi from process: {process}")
        process += 1
        time.sleep(0.1)

if __name__ == '__main__':
    processes = []
    num_processes = cpu_count()

    # create processes
    for _ in range(num_processes):
        process = Process(target=greet)
        processes.append(process)
        
    # start processes
    for p in processes:
        p.start()
        
    # join processes
    for p in processes:
        p.join()
        
    print("Hello from main")