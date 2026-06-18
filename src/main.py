import os
import time
import psutil
import pandas as pd
import matplotlib.pyplot as plt
from src.blockchain import Blockchain


# Mines 5 blocks at a given difficulty and returns the elapsed time and average CPU usage.
def benchmark(algorithm, difficulty):
    chain = Blockchain(difficulty, algorithm)
    psutil.cpu_percent(interval=None)
    start = time.perf_counter()
    for i in range(5):
        chain.add_block(f"Block {i}")
    elapsed = time.perf_counter() - start
    cpu = psutil.cpu_percent(interval=None)
    return elapsed, cpu


# Runs the benchmark for all three protocols across difficulty levels 1 to 5 and collects the metrics.
def run_benchmarks():
    records = []
    for difficulty in range(1, 6):
        for algorithm in ["sha256", "sha3_256", "arip"]:
            elapsed, cpu = benchmark(algorithm, difficulty)
            records.append({"Difficulty": difficulty, "Algorithm": algorithm, "Time": elapsed, "CPU": cpu})
    return records


# Converts the collected metrics into a DataFrame and exports it to the results CSV file.
def save_results(records):
    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame(records)
    df.to_csv("data/arip_benchmark_results.csv", index=False)
    return df


# Draws a line chart comparing mining time per difficulty for both algorithms.
def plot_time(df):
    os.makedirs("output", exist_ok=True)
    plt.figure()
    for algorithm in df["Algorithm"].unique():
        subset = df[df["Algorithm"] == algorithm]
        plt.plot(subset["Difficulty"], subset["Time"], marker="o", label=algorithm)
    plt.xlabel("Difficulty")
    plt.ylabel("Time Taken (s)")
    plt.title("Time Complexity: SHA-256 vs SHA-3 vs ARIP")
    plt.legend()
    plt.savefig("output/dynamic_time_complexity_chart.png", dpi=300)
    plt.close()


# Draws a line chart comparing CPU utilization per difficulty for both algorithms.
def plot_cpu(df):
    os.makedirs("output", exist_ok=True)
    plt.figure()
    for algorithm in df["Algorithm"].unique():
        subset = df[df["Algorithm"] == algorithm]
        plt.plot(subset["Difficulty"], subset["CPU"], marker="o", label=algorithm)
    plt.xlabel("Difficulty")
    plt.ylabel("CPU Usage (%)")
    plt.title("CPU Utilization: SHA-256 vs SHA-3 vs ARIP")
    plt.legend()
    plt.savefig("output/core_utilization_chart.png", dpi=300)
    plt.close()


# Orchestrates the full benchmark flow: run, save results, and generate both charts.
def main():
    records = run_benchmarks()
    df = save_results(records)
    plot_time(df)
    plot_cpu(df)
    print("Benchmark complete. Results saved to data/ and charts saved to output/.")


if __name__ == "__main__":
    main()
