import numpy as np

class DataFlowOptimizer:
    def __init__(self, strategy="WeightStationary"):
        self.strategy = strategy

    def optimize(self, data):
        if not isinstance(data, (list, np.ndarray)):
            raise TypeError("Input data must be a list or numpy array.")
        
        if self.strategy == "WeightStationary":
            return self.weight_stationary(data)
        elif self.strategy == "OutputStationary":
            return self.output_stationary(data)
        else:
            raise ValueError(f"Unknown strategy: {self.strategy}")

    def weight_stationary(self, data):
        if isinstance(data, list):
            data = np.array(data)
        return np.sort(data)

    def output_stationary(self, data):
        if isinstance(data, list):
            data = np.array(data)
        return data * 2
