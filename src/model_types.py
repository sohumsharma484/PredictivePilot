def return_all_models(purpose_of_model):
    ''' Returns list of commonly used ML models for a specific purpose '''

    # purpose_of_model should be one of the following strings:
    # regression, classifier, clustering, reinforcement, generation
    # return_all_models returns a list of all commonly used ML models for that specific purpose
   
    purpose_to_list = {'regression':[
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
                        ],
                    'classifier':[
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
                    ],
                    'clustering':[
                        'k-means clustering',
                        'heirarchical clustering',
                        'density-based spectral clustering',
                        'gaussian mixture model',
                        'principal component analysis',
                        'autoencoders (neural network)',
                        'uniform manifold approximation and projection',
                        'linear discriminant analysis',
                    ],
                    'reinforcement':[
                        'Q-learning',
                        'deep Q network',
                        'deterministic policy gradient',
                        'trust region policy optimization',
                        'proximal policy optimization',
                        'actor-critic methods',
                        'monte carlo tree search',
                        'recurrent neural networks',
                    ], 
                    'generation':[
                        'generative adversarial networks',
                        'diffusion methods (e.g. stable)',
                        'variational autoencoders',
                        'transformers',
                        'boltzmann machines',
                        'autoregressive models',
                    ]}
    if purpose_of_model not in purpose_to_list:
        return "NOT A VALID PURPOSE FOR THE ML MODEL. MUST BE IN (regression, classifier, clustering, reinforcement, generation)"
    return purpose_to_list[purpose_of_model]
    