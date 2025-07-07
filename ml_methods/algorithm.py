from abc import ABC, abstractmethod

class Algorithm(ABC):

    @abstractmethod
    def applyAlgorithm(self, amount: float):
        pass
