import multiprocessing
import time

def cpu_stress(duration=60):
    end_time = time.time() + duration
    try:
        while time.time() < end_time:
            _ = 1 + 1  # Busy loop to stress CPU
    except KeyboardInterrupt:
        pass

def simulate_cpu_stress(duration=60):
    processes = []
    try:
        print(f"🚀 Injecting CPU stress for {duration} seconds...")
        for _ in range(4):  # 4 processes to max out CPU cores
            process = multiprocessing.Process(target=cpu_stress, args=(duration,))
            processes.append(process)
            process.start()
        
        # Wait for processes to finish
        for process in processes:
            process.join()
            
        print("✅ Anomaly injection completed.")
    except Exception as e:
        print(f"ERROR: {e}")
    finally:
        # Cleanup if interrupted
        for process in processes:
            if process.is_alive():
                process.terminate()

if __name__ == "__main__":
    simulate_cpu_stress()