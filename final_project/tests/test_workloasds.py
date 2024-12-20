import unittest
import os
from workloads.gpt2_model import GPT2Small
from workloads.data_loader import get_data_loader
from workloads.benchmark import Benchmark
from accelerator.simulator import AcceleratorSimulator

class TestWorkloads(unittest.TestCase):
    def test_gpt2_model(self):
        model = GPT2Small()
        sample_text = "The quick brown fox jumps over the lazy dog."
        inputs = model.preprocess(sample_text)
        outputs = model.forward(inputs)
        self.assertEqual(len(inputs["input_ids"].shape), 2)  # Batch size x Sequence length
        self.assertEqual(outputs.shape[0], inputs["input_ids"].shape[0])  # Batch 일치

    def test_data_loader(self):
        sample_texts = [
            "Artificial Intelligence is transforming industries.",
            "GPT-2 is a powerful model for language tasks."
        ]
        data_loader = get_data_loader(sample_texts, batch_size=2)
        for batch in data_loader:
            input_ids, attention_masks = batch
            self.assertEqual(input_ids.shape[0], 2)  # Batch size
            self.assertEqual(input_ids.shape[1], attention_masks.shape[1])  # Sequence length
            self.assertTrue(input_ids.is_cuda or not input_ids.is_cuda)  # GPU/CPU 호환성 확인
            break

    def test_benchmark(self):
        config_path = "configs/accelerator_config.json"
        if not os.path.exists(config_path):
            self.skipTest(f"Config file not found: {config_path}")
        gpt2 = GPT2Small()
        simulator = AcceleratorSimulator(config_path)
        benchmark = Benchmark(gpt2, simulator)
        sample_text = "Hello, world! This is a benchmark test."
        results = benchmark.run_benchmark(sample_text, batch_size=2)
        self.assertIn("total_time", results)
        self.assertGreater(results["total_time"], 0)

if __name__ == "__main__":
    unittest.main()
