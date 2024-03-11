from model_types import return_all_models

def test_model_types():
    ''' Tests the possible paths of return_all_models '''
    assert return_all_models("a") == "NOT A VALID PURPOSE FOR THE ML MODEL. MUST BE IN (regression, classifier, clustering, reinforcement, generation)"
    assert return_all_models("regression") == [
                        'linear regression',
                        'polynomial regression',
                        'ridge/lasso regression',
                        'elastic net regression',
                        'bayesian regression',
                        'random forest regression',
                        'gradient boosting regression',
                        'support vector regression',
                        'neural network regression',
                        'k-nearest neighbors regression',
                        'gaussian process regression',
                        ]
    assert return_all_models("classifier") == [
                        'logistic regression',
                        'decision trees classifiers',
                        'random forest classifiers',
                        'gradient boosting classifier',
                        'logistic model tree'
                        'support vector machine',
                        'k-nearest neighbors classifier',
                        'nearest centroid classifier',
                        'naive bayes classifier',
                        'linear/quadratic discriminant analysis'
                        'multilayer perceptron network',
                        'hidden markov model',
                        'convolutional neural network',
                        'transformer',
                    ]
    assert return_all_models("clustering") == [
                        'k-means clustering',
                        'heirarchical clustering',
                        'density-based spectral clustering',
                        'gaussian mixture model',
                        'principal component analysis',
                        'autoencoders (neural network)',
                        'uniform manifold approximation and projection',
                        'linear discriminant analysis',
                    ]
    assert return_all_models("reinforcement") == [
                        'Q-learning',
                        'deep Q network',
                        'deterministic policy gradient',
                        'trust region policy optimization',
                        'proximal policy optimization',
                        'actor-critic methods',
                        'monte carlo tree search',
                        'recurrent neural networks',
                    ]
    assert return_all_models("generation") == [
                        'generative adversarial networks',
                        'diffusion methods (e.g. stable)',
                        'variational autoencoders',
                        'transformers',
                        'boltzmann machines',
                        'autoregressive models',
                    ]