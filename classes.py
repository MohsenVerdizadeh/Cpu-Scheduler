import random


class Process:
    def __init__(self, arrival_time):
        self.arrival_time = arrival_time
        self.execution_time = random.randint(1, 10)
        self.deadline = self.execution_time + random.randint(1, 10)
        self.score = random.randint(1, 100)
