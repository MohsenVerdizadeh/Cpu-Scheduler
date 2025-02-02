# EDF-Based Process Scheduler

## 📌 Project Overview

This is the final project of my operating system course that implements an **Earliest Deadline First (EDF)** scheduling algorithm for a **multi-core CPU simulation**. It efficiently manages **real-time processes** with execution constraints, prioritizing tasks based on their deadlines and maximizing system performance.

## ⚙️ Features

- **Multi-core CPU support** (configurable number of CPUs)
- **EDF Scheduling** (prioritizes processes with the nearest deadlines)
- **Dynamic priority updates** (priority increases as deadline approaches)
- **Process expiration handling** (removes missed deadline processes)
- **Maximizing total system score** (optimizes process execution order)
- **Thread-safe priority queue** (efficient process management using min-heap & max-heap)

## 🛠 Installation & Setup

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/MohsenVerdizadeh/Cpu-Scheduler.git
   cd your-repository
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

