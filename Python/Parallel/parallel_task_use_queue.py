from multiprocessing import Pool, TimeoutError
from multiprocessing import Queue
from multiprocessing import Process, Lock

import time
import os



def init_task_queue(task_queue):
    # task_queue.put(task)
    print("total {} tasks".format(task_queue.qsize()))

    
def init_resource():
    resource = dict()
    return resource


def write_result(result_list, accumulate_count, output_path):
    pass


# 消费者
def consumer(rst_queue, output_path, task_count):
    block_count = 0
    task_done = 0
    data_block = list()
    while True:
        if rst_queue.qsize() == 0:
            print("no result in rst_task, sleep, queue size: {}".format(rst_queue.qsize()))
            time.sleep(1)
            continue
        example = rst_queue.get()
        if example is None:
            task_done += 1
            print("find one producer done. +1 total: {}".format(task_done))
            if task_done == task_count:
                break
            continue
        data_block.append(example)
        block_count += 1
        if block_count % count_per_file == 0:
            write_result(data_block, block_count, output_path)
            data_block = list()
    if len(data_block) > 0:
        write_result(data_block, block_count, output_path)
    print("consumer {} return.".format(os.getpid()))

    
def produce_example(task_arg, resource):
    # 根据自己的需求，实现
    return None


# 生产者
def producer(task_queue, rst_queue, resource):
    while True:
        if task_queue.empty():
            rst_queue.put(None)
            print("producer task {} done. return".format(os.getpid()))
            break
        task_arg = task_queue.get()
        for example in produce_example(task_arg, resource):
            rst_queue.put(example)
    print("producer {} done. return".format(os.getpid()))


def run():
    # 定义任务队列，公共资源
    task_count = 5
    task_queue = Queue()
    rst_queue = Queue(3000)

    # 初始化任务队列 / 加载公共资源
    init_task_queue(task_queue)
    resource = init_resource()

    # 消费者
    consumer_proc = Process(target=consumer, args=(rst_queue, output_path, task_count))

    # start producer  worker
    workers = list()
    for i in range(task_count):
        producer_proc = Process(target=producer, args=(task_queue, rst_queue, resource, ))
        workers.append(producer_proc)

    for worker in workers:
        worker.start()

    consumer_proc.start()
    consumer_proc.join()
    
        
        
if __name__ == '__main__':
    run()
