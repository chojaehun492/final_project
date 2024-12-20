import matplotlib.pyplot as plt
import numpy as np

def generate_roofline_graph(data, output_path="output/roofline_analysis.png"):
    intensities = data.get("intensities", [])
    performances = data.get("performances", [])
    bandwidths = data.get("bandwidths", [])
    peak_performance = data.get("peak_performance", 0)

    if not intensities or not performances or not bandwidths or peak_performance <= 0:
        raise ValueError("Invalid data: Please provide intensities, performances, bandwidths, and peak performance.")

    # Roofline 곡선 계산
    max_intensity = max(intensities + [1000])
    operational_intensities = np.logspace(-2, np.log10(max_intensity), 100)
    roofline_performances = [np.minimum(operational_intensities * bw, peak_performance) for bw in bandwidths]

    # Roofline 플롯
    plt.figure(figsize=(10, 6))
    for idx, roof_perf in enumerate(roofline_performances):
        plt.plot(operational_intensities, roof_perf, label=f"Bandwidth {bandwidths[idx]} GB/s", linestyle="--")
    plt.scatter(intensities, performances, color="red", label="Workloads", s=100, edgecolors="black")
    plt.axhline(peak_performance, color="magenta", linestyle="-", label="Peak Performance")

    # 그래프 포맷 설정
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Operational Intensity (FLOPS/Byte)")
    plt.ylabel("Performance (FLOPS)")
    plt.title("Roofline Analysis")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)

    # 그래프 저장
    plt.savefig(output_path)
    plt.close()
    print(f"Roofline graph saved to {output_path}")
