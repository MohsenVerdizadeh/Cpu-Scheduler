# EDF-Based Process Scheduler

## 📌 Project Overview

This project is the final implementation for my Operating Systems course, which simulates a **multi-core CPU** running the **Earliest Deadline First (EDF)** scheduling algorithm. The system efficiently manages **real-time processes** with strict execution constraints, prioritizing tasks based on their deadlines to maximize overall system performance.

## ⚙️ Features

- **Multi-core CPU support**: Configurable number of CPUs for parallel processing.
- **EDF Scheduling**: Prioritizes processes based on the nearest deadline.
- **Dynamic priority updates**: Priorities increase as deadlines approach.
- **Process expiration handling**: Automatically removes processes that miss their deadlines.
- **Maximized system score**: Optimizes task order to achieve the highest system performance.
- **Thread-safe priority queue**: Utilizes a min-heap and max-heap for efficient process management.
- **Simulation of 10 Runs**: The scheduler runs 10 simulations, generating random processes each time, and displays performance results, such as system score and CPU utilization.
- **Charts for Results**: Visualizes the results with graphs such as process completion time and CPU utilization across simulations.

## 🛠 Installation & Setup

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/MohsenVerdizadeh/Cpu-Scheduler.git
   cd Cpu-Scheduler
   ```
3. **Run the Scheduler:**
   ```sh
   python main.py
   ```

## 📜 Usage

- The system continuously **generates random processes** with execution times and deadlines.
- Processes are **stored in a priority queue** (EDF-based ordering).
- The **scheduler assigns tasks to available CPU threads**.
- **Expired processes** are automatically removed to prevent execution.
- **Total system score is maximized** by efficiently handling process selection.

## 🏗 Project Structure

```
├── main.py                # Main entry point for execution
├── classes.py             # classes definition
├── simulate.py            # simulate 10 times and showing results with charts
├── simulate_main.py       # special main for simulate
├── configs.py             # maintain some configs for running main 
├── requirements.txt       # include some requirements library for this project
├── README.md              # Project documentation
```

## 🧑‍💻 Contributing

1. **Fork** the repository.
2. **Create a new branch** (`feature-xyz`).
3. **Commit your changes**.
4. **Push to your fork & submit a PR**.

## ⚖️ License

This project is licensed under the **MIT License**.

---

*Developed by Your Name* 🚀

