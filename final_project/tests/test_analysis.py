import unittest
import os
from analysis.roofline import RooflineAnalysis
from analysis.plot_results import plot_comparison

class TestAnalysis(unittest.TestCase):
    def test_roofline_analysis(self):
        peak_flops = 1e12
        peak_mem_bw = 512e9
        roofline = RooflineAnalysis(peak_flops, peak_mem_bw)
        op_intensities = [0.5, 10, 50]
        performance = roofline.calculate_roofline(op_intensities)
        self.assertEqual(len(performance), len(op_intensities))
        self.assertTrue(all(p <= peak_flops for p in performance))  # FLOPS 한계 확인

    def test_plot_comparison(self):
        x = [1, 2, 3, 4, 5]
        y1 = [10, 20, 30, 40, 50]
        y2 = [15, 25, 35, 45, 55]
        output_path = "output/test_comparison.png"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        try:
            plot_comparison(
                x, y1, y2,
                labels=["Model A", "Model B"],
                title="Test Comparison Plot",
                xlabel="X-Axis",
                ylabel="Y-Axis",
                output_path=output_path
            )
            self.assertTrue(os.path.exists(output_path))
        except Exception as e:
            self.fail(f"Plotting failed with exception: {e}")

if __name__ == "__main__":
    unittest.main()
