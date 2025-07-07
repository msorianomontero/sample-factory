from algorithm_factory import AlgorithmFactory
factory = AlgorithmFactory()
algorithm = factory.create("NaiveBayes")
algorithm.applyAlgorithm('dataset_01.csv')
