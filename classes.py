import heapq
import math
import random
import threading


class Process:

    def __init__(self, id, arrival_time):
        self.id = id
        self.arrival_time = arrival_time
        self.execution_time = random.randint(1, 10)
        self.deadline = self.arrival_time + self.execution_time + random.randint(1, 10)
        self.score = random.randint(1, 100)
        self.priority = 0
        self.calculate_priority(arrival_time)

    def __str__(self):
        return f"Process {self.id}: arrival_time: {self.arrival_time}, execution_time: {self.execution_time}, deadline: {self.deadline}, score: {self.score}"

    def calculate_priority(self, current_time):
        time_remaining = max(self.deadline - current_time, 1)
        self.priority = self.score / time_remaining

    def update_priority(self, current_time):
        self.calculate_priority(current_time)

    def __lt__(self, other):
        return self.priority > other.priority  # Prioritize highest score-to-deadline ratio


class PQ:
    def __init__(self, size=math.inf):
        self.min_heap = []  # Stores (priority, process) -> Min-Heap (worst process)
        self.max_heap = []  # Stores (-priority, process) -> Max-Heap (best process)
        self.size = size
        self.sem = threading.Semaphore(1)

    def get_size(self):
        with self.sem:
            return len(self.min_heap)

    def put(self, process):
        with self.sem:
            heapq.heappush(self.min_heap, (process.priority, process))
            heapq.heappush(self.max_heap, (-process.priority, process))

    def replace_if_better(self, new_process):
        with self.sem:
            if not self.full():
                heapq.heappush(self.min_heap, (new_process.priority, new_process))
                heapq.heappush(self.max_heap, (-new_process.priority, new_process))
                return None
            else:
                worst_priority, worst_process = self.min_heap[0]
                if new_process.priority > worst_priority:
                    result = self.pop_worst()
                    heapq.heappush(self.min_heap, (new_process.priority, new_process))
                    heapq.heappush(self.max_heap, (-new_process.priority, new_process))
                    return result
                else:
                    return new_process

    def pop_best(self):
        """Remove and return the best (highest priority) process."""
        with self.sem:
            if self.max_heap:
                best_priority, best_process = heapq.heappop(self.max_heap)
                self.min_heap = [(p.priority, p) for _, p in self.max_heap]  # Rebuild min-heap
                heapq.heapify(self.min_heap)
                return best_process
            return None

    def pop_worst(self):
        """Remove and return the worst process."""
        if self.min_heap:
            worst_priority, worst_process = heapq.heappop(self.min_heap)
            self.max_heap = [(-p.priority, p) for _, p in self.min_heap]  # Rebuild max-heap
            heapq.heapify(self.max_heap)
            return worst_process
        return None

    def update_priorities(self, current_time):
        """Remove expired processes and update priorities."""
        with self.sem:
            self.min_heap = [(p.priority, p) for _, p in self.min_heap if p.deadline >= current_time + p.execution_time]
            self.max_heap = [(-p.priority, p) for _, p in self.max_heap if
                             p.deadline >= current_time + p.execution_time]

            for _, process in self.min_heap:
                process.update_priority(current_time)

            heapq.heapify(self.min_heap)  # Re-sort min-heap
            heapq.heapify(self.max_heap)  # Re-sort max-heap

    def empty(self):
        with self.sem:
            return len(self.min_heap) == 0

    def full(self):
        return len(self.min_heap) >= self.size


class VarWithLock:
    def __init__(self, value=0):
        self.value = value
        self.sem = threading.Semaphore(1)

    def increment(self, val=1):
        with self.sem:
            self.value += val

    def get(self):
        with self.sem:
            return self.value
