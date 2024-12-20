import matplotlib.pyplot as plt
import numpy as np

def generate_comparison_plot(data, output_path="output/comparison_plot.png"):
    epochs = data["epochs"]
    baseline = data["baseline"]
    optimized = data["optimized"]

    plt.figure(figsize=(10, 6))
    plt.plot(epochs, baseline, label="Baseline", marker="o")
    plt.plot(epochs, optimized, label="Optimized", marker="s")
    plt.xlabel("Epochs")
    plt.ylabel("Performance (FLOPS)")
    plt.title("Performance Comparison")
    plt.legend()
    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.savefig(output_path)
    plt.close()
    print(f"Comparison plot saved to {output_path}")

def generate_histogram_plot(data, output_path="output/histogram_plot.png"):
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=10, color="skyblue", edgecolor="black")
    plt.xlabel("Performance (FLOPS)")
    plt.ylabel("Frequency")
    plt.title("Histogram of Performance")
    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.savefig(output_path)
    plt.close()
    print(f"Histogram plot saved to {output_path}")
