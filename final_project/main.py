from accelerator.simulator import AcceleratorSimulator
from workloads.benchmark import Benchmark
from workloads.gpt2_model import GPT2Small
from analysis.roofline import generate_roofline_graph

def main():
    # 모델 초기화
    gpt2_model = GPT2Small()

    # 캐시 사용 시뮬레이터
    simulator_with_cache = AcceleratorSimulator("configs/accelerator_config.json", use_cache=True)
    benchmark_with_cache = Benchmark(gpt2_model, simulator_with_cache)

    # 캐시 미사용 시뮬레이터
    simulator_without_cache = AcceleratorSimulator("configs/accelerator_config.json", use_cache=False)
    benchmark_without_cache = Benchmark(gpt2_model, simulator_without_cache)

    print("Running benchmark with multi-level cache...")
    results_with_cache = benchmark_with_cache.run_benchmark("Sample text", batch_size=100)
    print("Results with Cache:", results_with_cache)

    print("\nRunning benchmark without cache...")
    results_without_cache = benchmark_without_cache.run_benchmark("Sample text", batch_size=100)
    print("Results without Cache:", results_without_cache)

    # Roofline 데이터 생성
    roofline_data = {
        "intensities": [results_with_cache["operational_intensity"], results_without_cache["operational_intensity"]],
        "performances": [results_with_cache["flops"], results_without_cache["flops"]],
        "bandwidths": [10, 50, 100],  # 각 메모리 계층의 대역폭
        "peak_performance": 200000  # 시스템의 최대 FLOPS
    }

    # Roofline 그래프 생성
    print("\nGenerating Roofline graph...")
    generate_roofline_graph(roofline_data, output_path="output/roofline_analysis.png")

if __name__ == "__main__":
    main()
