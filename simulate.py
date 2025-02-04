import json
import multiprocessing
import matplotlib.pyplot as plt
from simulate_main import main


def run(lock):
    main(lock)


if __name__ == "__main__":
    with open("simulate_data.txt", "w") as file:
        json.dump([], file)
    with multiprocessing.Manager() as manager:
        lock = manager.Lock()  # Create a lock using Manager (fixes the issue)

        count = [lock] * 10  # Create a list of locks
        with multiprocessing.Pool(processes=4) as pool:
            pool.map(run, count)  # Run processes safely
    with open("simulate_data.txt", "r") as file:
        simulates_data = json.load(file)
    simulates = [i for i in range(1, 11)]
    hit_rates = []
    scores = []
    avg_waiting_times = []
    avg_res_time = []
    for sim_data in simulates_data:
        hit_rates.append(sim_data['hit rate'])
        scores.append(sim_data["score"])
        avg_waiting_times.append(sim_data["average waiting time"])
        avg_res_time.append(sim_data["average response time"])

    # Create a figure with 2 rows & 2 columns of subplots
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))

    # First subplot (Top-Left)
    axes[0, 0].plot(simulates, hit_rates, marker='o', color='b', label='hit rate')
    axes[0, 0].set_title("Hit Rate")
    axes[0, 0].legend()

    # Second subplot (Top-Right)
    axes[0, 1].plot(simulates, scores, marker='o', color='r', linestyle='--', label='score')
    axes[0, 1].set_title("Score")
    axes[0, 1].legend()

    # Third subplot (Bottom-Left)
    axes[1, 0].plot(simulates, avg_waiting_times, marker='o', color='g', linestyle='-.', label='avg waiting time')
    axes[1, 0].set_title("Average Waiting Time")
    axes[1, 0].legend()

    # Fourth subplot (Bottom-Right)
    axes[1, 1].plot(simulates, avg_res_time, marker='o', color='purple', linestyle=':', label='avg response time')
    axes[1, 1].set_title("Average Response Time")
    axes[1, 1].legend()

    # Adjust layout to prevent overlap
    plt.tight_layout()
    plt.show()
    print("All processes finished.")
