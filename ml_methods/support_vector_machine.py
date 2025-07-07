from .algorithm import Algorithm

class SupportVectorMachine(Algorithm):
    def applyAlgorithm(self, dataset: str):
        print(f"Will apply SVM regression to dataset in file ${dataset}.")