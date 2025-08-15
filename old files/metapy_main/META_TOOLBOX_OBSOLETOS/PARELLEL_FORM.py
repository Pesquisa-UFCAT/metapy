# SuperFastPython.com
# example of parallel map_async() with the process pool
from random import random
from time import sleep
from multiprocessing.pool import Pool

import multiprocessing

# task executed in a worker process
def task(identifier):
    # generate a value
    value = random()
    # report a message
    print(f'Task {identifier} executing with {value}', flush=True)
    # block for a moment
    sleep(value)
    # return the generated value
    oi = 'oi'
    wander = 'wander'
    return value, oi, wander
 
# protect the entry point
if __name__ == '__main__':
    # create and configure the process pool
    with Pool() as pool:
        # issues tasks to process pool
        wander = [['oi','oi'],['oi','oi'],['oi','oi'],['oi','oi'],['oi','oi'],['oi','oi'],['oi','oi'],['oi','oi'],['oi','oi'],['oi','oi']]
        result = pool.map_async(task, wander)
        # iterate results
        for result in result.get():
            print(f'Got result: {result[0]} and type{type(result)}', flush=True)
    # process pool is closed automatically