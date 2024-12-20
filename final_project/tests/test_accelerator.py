import unittest
from accelerator.pe_array import PEArray
from accelerator.cache import MultiLevelCache
from accelerator.dataflow import DataFlowOptimizer
from accelerator.simulator import AcceleratorSimulator

class TestAccelerator(unittest.TestCase):
    def test_pe_array(self):
        pe_array = PEArray(num_pe=4)
        workloads = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        results = pe_array.distribute_workload(workloads)
        self.assertEqual(len(results), len(workloads))
        self.assertEqual(len(results[0][1]), 1)  # PE 연산 결과의 형태 확인

    def test_cache(self):
        cache = MultiLevelCache(l1_size=2, l2_size=4)
        cache.store(1, "A")
        self.assertEqual(cache.fetch(1), "A")
        self.assertIsNone(cache.fetch(3))

    def test_dataflow(self):
        optimizer = DataFlowOptimizer(strategy="WeightStationary")
        optimized_data = optimizer.optimize([3, 1, 2])
        self.assertEqual(optimized_data, [1, 2, 3])

if __name__ == "__main__":
    unittest.main()
