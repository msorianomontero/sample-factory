from .algorithm import Algorithm

class LogisticRegression(Algorithm):
    def applyAlgorithm(self, dataset: str):
        print(f"Will apply logistic regression to dataset in file ${dataset}.")