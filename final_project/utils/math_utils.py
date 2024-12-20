import numpy as np

class MathUtils:
    @staticmethod
    def calculate_mean(values):
        if not values:
            raise ValueError("Empty list provided for mean calculation.")
        return np.mean(values)

    @staticmethod
    def calculate_std(values):
        if not values:
            raise ValueError("Empty list provided for standard deviation calculation.")
        return np.std(values)

    @staticmethod
    def normalize(values):
        values = np.array(values)
        range_ = np.max(values) - np.min(values)
        if range_ == 0:
            raise ValueError("Normalization is not possible as all values are identical.")
        return (values - np.min(values)) / range_
