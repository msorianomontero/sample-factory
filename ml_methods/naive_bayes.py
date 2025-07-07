from .algorithm import Algorithm

class NaiveBayes(Algorithm):
    def applyAlgorithm(self, dataset: str):
        print(f"Will apply Naive Bayes to dataset in file ${dataset}.")