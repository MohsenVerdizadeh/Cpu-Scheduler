import random


class Process:
    def __init__(self, arrival_time):
        self.arrival_time = arrival_time
        self.execution_time = random.randint(1, 10)
        self.deadline = self.execution_time + random.randint(1, 10)
        self.score = random.randint(1, 100)
        self.priority = random.randint(1, 100)

    def calculate_priority(self):
        self.priority = self.score / self.deadline
