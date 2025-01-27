import multiprocessing
import time

def cpu_stress(duration=60):
    end_time = time.time() + duration
    while time.time() < end_time:
        pass

def simulate_cpu_stress(duration=60):
    # Create multiple processes to stress CPU
    processes = []
    for _ in range(4):  # Adjust the number of processes as needed
        process = multiprocessing.Process(target=cpu_stress, args=(duration,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    print("Injecting CPU stress for 60 seconds...")
    simulate_cpu_stress()
