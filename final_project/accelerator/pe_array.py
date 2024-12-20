import numpy as np

class ProcessingElement:
    def __init__(self, id):
        self.id = id
        self.data = None
        self.result = None

    def compute(self, data):
        data_matrix = np.array(data).reshape(-1, 1)
        weights = np.random.random((data_matrix.shape[0], 1))
        self.result = np.dot(data_matrix.T, weights).flatten().tolist()
        return self.result

class PEArray:
    def __init__(self, num_pe):
        self.num_pe = num_pe
        self.pes = [ProcessingElement(i) for i in range(num_pe)]

    def distribute_workload(self, workloads):
        results = []
        for i, workload in enumerate(workloads):
            pe_id = i % self.num_pe
            result = self.pes[pe_id].compute(workload)
            results.append((pe_id, result))
        return results
