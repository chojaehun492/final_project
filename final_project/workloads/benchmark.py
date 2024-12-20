import time
import torch
from workloads.gpt2_model import GPT2Small
from accelerator.simulator import AcceleratorSimulator

class Benchmark:
    def __init__(self, model, simulator):
        self.model = model
        self.simulator = simulator

    def measure_model_performance(self, input_text, batch_size=1):
        inputs = self.model.preprocess(input_text)
        inputs = {key: val.repeat(batch_size, 1) for key, val in inputs.items()}
        start_time = time.time()
        with torch.no_grad():
            outputs = self.model.forward(inputs)
        inference_time = time.time() - start_time
        flops = batch_size * outputs.shape[-1] * inputs["input_ids"].shape[1]
        return inference_time, flops

    def run_benchmark(self, input_text, batch_size=1):
        inference_time, flops = self.measure_model_performance(input_text, batch_size)
        print(f"Inference Time: {inference_time:.4f} sec, FLOPS: {flops:.2f}")

        # 수정된 workload 정의
        workload = {
            "flops": flops,
            "batch_size": batch_size,
            "address": hash(input_text),  # 유일한 주소 생성
            "data": input_text,
        }
        simulation_result = self.simulator.simulate(workload)
        print("Simulation Result:", simulation_result)
        return simulation_result
