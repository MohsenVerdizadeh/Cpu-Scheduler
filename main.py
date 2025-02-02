import queue
import threading
import time
from time import sleep

from configs import process_generate_count_per_second
from classes import Process


def clock(current_time, current_time_sem):
    while True:
        sleep(1)
        with current_time_sem:
            current_time += 1


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


def scheduler(input_queue, ready_queue):


if __name__ == "__main__":
    current_time = 0
    current_time_sem = threading.Semaphore(1)
    clock_thread = threading.Thread(target=clock, args=(current_time, current_time_sem), daemon=True)
    clock_thread.start()

    input_queue = queue.Queue()
    completed_process_count = 0
    proc_gen = threading.Thread(target=generate_process, args=(input_queue, completed_process_count), daemon=True)
    proc_gen.start()
    ready_queue = queue.PriorityQueue(20)
    ready_queue.
