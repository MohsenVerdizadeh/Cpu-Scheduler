import queue
import threading
import time
from time import sleep

from configs import process_generate_count_per_second
from classes import Process


# completed_process_count_sem = threading.Semaphore(1)
#
#
# def read_completed_process_count(completed_process_count):
#     global completed_process_count_sem
#     result = 0
#     with completed_process_count_sem:
#         result = completed_process_count_sem
#     return result


def generate_process(input_queue, completed_process_count):
    start_time = 0
    while completed_process_count < 100:
        for _ in range(process_generate_count_per_second):
            input_queue.put(Process(start_time))
        sleep(1)
        start_time += 1


if __name__ == "__main__":
    real_start_time = time.time()
    input_queue = queue.Queue()
    completed_process_count = 0
    proc_gen = threading.Thread(target=generate_process, args=(input_queue, completed_process_count), daemon=True)
    proc_gen.start()
    redy_queue =queue.PriorityQueue(20)
    redy_queue.

