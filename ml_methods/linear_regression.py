from .algorithm import Algorithm

class LinearRegression(Algorithm):
    def applyAlgorithm(self, dataset: str):
        print(f"Will apply Linear regression to dataset in file ${dataset}.")