import threading
from time import sleep

from configs import *
from classes import *

terminal_sem = threading.Semaphore(1)
file_sem = threading.Semaphore(1)


def clock(current_time):
    while True:
        sleep(1)
        current_time.increment()


def generate_process(input_queue, hit_count, current_time, proc_count):
    sleep(0.3)
    write("Process generator started.")
    while hit_count.get() < hit_count_bound:
        for _ in range(process_generate_count_per_second):
            proc_count.increment()
            process = Process(proc_count.get(), current_time.get())
            input_queue.put(process)
            write_file("log/process.txt", str(process) + " created")
        sleep(1)


def scheduler(input_queue, ready_queue, hit_count, current_time):
    sleep(0.31)
    write("Scheduler started.")
    while hit_count.get() < hit_count_bound or not input_queue.empty():
        if not input_queue.empty():
            new_process = input_queue.pop_best()
            worse_process = ready_queue.replace_if_better(new_process)
            if worse_process is not None:
                input_queue.put(worse_process)
            ready_queue.update_priorities(current_time.get())


def cpu_work(ready_queue, hit_count, score, current_time):
    sleep(0.33)
    write("CPU started.")
    while hit_count.get() < hit_count_bound or not ready_queue.empty():
        if not ready_queue.empty():
            process = ready_queue.pop_best()
            sleep(process.execution_time)
            hit_count.increment()
            score.increment(process.score)
            write_file("log/hit_process.txt", str(process) + ", End Time :  " + str(current_time.get()))


def write(message):
    with terminal_sem:
        print(message)


def write_file(file_path, message):
    with file_sem:
        with open(file_path, "a") as file:
            file.write(message + "\n")


if __name__ == "__main__":
    current_time = VarWithLock()
    clock_thread = threading.Thread(target=clock, args=(current_time,), daemon=True)
    clock_thread.start()

    input_queue = PQ()
    hit_count = VarWithLock()
    proc_count = VarWithLock()
    score = VarWithLock()
    proc_gen = threading.Thread(target=generate_process, args=(input_queue, hit_count, current_time, proc_count),
                                daemon=True)

    proc_gen.start()

    ready_queue = PQ(ready_queue_size)
    scheduler_thread = threading.Thread(target=scheduler,
                                        args=(input_queue, ready_queue, hit_count, current_time),
                                        daemon=True)
    scheduler_thread.start()

    cores = []
    for _ in range(cpu_count):
        t = threading.Thread(target=cpu_work, args=(ready_queue, hit_count, score, current_time))
        cores.append(t)
        t.start()
    for t in cores:
        t.join()

    write_file("log/result.txt",
               f"Hit Count : {hit_count.get()} , Process Count : {proc_count.get()} , Total Hit Ratio : {hit_count.get() / proc_count.get()} -----------> Total Score : {score.get()}.")
