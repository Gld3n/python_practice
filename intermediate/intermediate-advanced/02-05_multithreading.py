from threading import Thread

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