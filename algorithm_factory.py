from inspect import getmembers, isclass, isabstract
import ml_methods

class AlgorithmFactory(object):
    algorithm_implementations = {}

    def __init__(self):
        self.load_algorithm_methods()

    def load_algorithm_methods(self):
        implementations = getmembers(ml_methods, lambda m: isclass(m) and not isabstract(m))
        for name, _type in implementations: 
            if isclass(_type) and issubclass(_type, ml_methods.Algorithm):
                self.algorithm_implementations[name] =_type


    def create(self, algorithm_type: str):
        if algorithm_type in self.algorithm_implementations:
            return self.algorithm_implementations[algorithm_type]()
        else:
            raise ValueError(f"{algorithm_type} is not currently supported as an ML method.")
        
