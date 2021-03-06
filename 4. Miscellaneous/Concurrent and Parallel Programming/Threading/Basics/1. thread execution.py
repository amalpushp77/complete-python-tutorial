# https://realpython.com/intro-to-python-threading/

import logging
import threading
import time


start = time.perf_counter()


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    log_format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=log_format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")

    #x.join()

    logging.info("Main    : all done")
    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')