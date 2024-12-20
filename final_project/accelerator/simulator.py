import json
import os

class AcceleratorSimulator:
    def __init__(self, config_path, use_cache=False):
        self.config = self.load_config(config_path)
        self.peak_flops = self.config["peak_flops"]
        self.peak_mem_bw = self.config["peak_mem_bw"]
        self.memory_bandwidth = self.config.get("memory_bandwidth", self.peak_mem_bw)  # Default to peak_mem_bw
        self.use_cache = use_cache

    def load_config(self, config_path):
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
        with open(config_path, "r") as f:
            return json.load(f)

    def calculate_operational_intensity(self, flops, data_transfer):
        return flops / data_transfer if data_transfer > 0 else 0

    def simulate(self, workload):
        flops = workload.get("flops", 0)
        batch_size = workload.get("batch_size", 1)
        data_transfer = flops / 10

        op_intensity = self.calculate_operational_intensity(flops, data_transfer)

        if op_intensity < self.peak_mem_bw:
            bottleneck = "Memory-Bound"
        else:
            bottleneck = "Compute-Bound"

        compute_time = flops / self.peak_flops
        memory_time = data_transfer / self.memory_bandwidth  # Use memory_bandwidth
        total_time = max(compute_time, memory_time)

        return {
            "operational_intensity": op_intensity,
            "bottleneck": bottleneck,
            "compute_time": compute_time,
            "memory_time": memory_time,
            "total_time": total_time,
            "flops": flops
        }
