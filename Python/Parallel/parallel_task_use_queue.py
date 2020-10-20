from multiprocessing import Pool, TimeoutError
from multiprocessing import Queue
from multiprocessing import Process, Lock

import time
import os



# 任务队列，公共资源
task_queue = Queue()
rst_queue = Queue()
resource = dict()
lock = Lock()


for i in range(10):
    task_queue.put(i)
    resource[i] = i*i

# 消费
def consumer():
    #lock.acquire()
    #try:
    #finally:
    #    lock.release()
    with open("/tmp/result.txt", "w+") as ofd:
        while True:
            if rst_queue.empty():
                print("no result in rst_task, sleep ...")
                time.sleep(2)
                continue
            task_arg, result = rst_queue.get()
            ofd.write("{}\t{}\n".format(task_arg, result))
            print("consumer pid = {} result = {} now result queue size: {}".format(os.getpid(),
                    result, rst_queue.qsize()))

# 生产
def producer():
    while True:
        if task_queue.empty():
            print("all task done. break")
            break
        time.sleep(1)
        task_arg = task_queue.get()
        result = resource[task_arg]
        rst_queue.put((task_arg, result))
        print("producer pid = {} result = {} now result queue size: {}".format(os.getpid(),
            result, rst_queue.qsize()))

if __name__ == '__main__':
    # 消费进程

    consumer_proc = Process(target=consumer)
    consumer_proc.start()
    # start 4 worker processes
    for i in range(4):
        producer_proc = Process(target=producer)
        producer_proc.start()
        #producer_proc.join()

    consumer_proc.join()
