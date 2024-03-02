''' Applies Multvariate Linear Regression to input data '''
import pandas as pd

data = pd.DataFrame([
    [1, 2, 3, 4],
    [4, 9, 5, 1],
    [6, 1, 9, 6]
])

def correlations(dataset, cols_idx):
    ''' Finds correlation matrix between specified variables in the dataset '''
    # dataset is a numpy array with the data and cols_idx is a list with the columns (variables) we want '''
    df = pd.DataFrame(dataset)
    if len(cols_idx) > 0:
        df = df[cols_idx]
    return df.corr()
    
def test_answer1():
    " Test #1 "
    a = correlations(data, [])
    b = pd.DataFrame([
        [1.000000,  0.000000,  0.953821,  0.289474],
        [0.000000,  1.000000, -0.300376, -0.957186],
        [0.953821, -0.300376,  1.000000,  0.563621],
        [0.289474, -0.957186,  0.563621,  1.000000],
    ])
    a = a.round(5)
    b = b.round(5)
    assert a.equals(b)

def test_answer2():
    " Test #2 "
    d = { 0:0, 1:1, 3:2 }
    a = correlations(data, [0, 1, 3])
    b = pd.DataFrame([
        [1.000000,  0.000000,  0.289474],
        [0.000000,  1.000000, -0.957186],
        [0.289474, -0.957186,  1.000000]
    ])
    a.rename(columns = d, index = d, inplace = True)
    a = a.round(5)
    b.rename(columns = d, index = d, inplace = True)
    b = b.round(5)
    assert a.equals(b)
