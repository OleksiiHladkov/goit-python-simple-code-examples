import concurrent.futures
from threading import Thread, Event
import logging
from random import randint
from time import time, sleep


def greeting(name):
    event.wait()
    logging.debug(f'greeting for: {name}')
    sleep(randint(0, 3))
    return f"Hello {name}"

def func(delay):
    timer = time()
    sleep(delay)
    logging.debug(f'Done {time() - timer}')
    event.set()

event = Event()

arguments = (
    "Bill",
    "Jill",
    "Till",
    "Sam",
    "Tom",
    "John",
)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    
    t1 = Thread(target=func, args=(2,))
    # t2 = Thread(target=func, args=(2,))
    t1.start()
    # t2.start()

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(greeting, arguments))

    logging.debug(results)
