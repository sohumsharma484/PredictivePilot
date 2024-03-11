import numpy as np
from statistics import mode

def is_boolean(s):
    return s in ["True", "true", "False", "false"]

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def is_float(s):
    if is_integer(s):
        return False
    try:
        float(s)
        return True
    except ValueError:
        return False
    
# Determine data type of given string
def determine_value_datatype(s):
    if is_integer(s):
        return "int"
    elif is_float(s):
        return "float"
    elif is_boolean(s):
        return "bool"
    else:
        return "str"
    
def determine_column_datatype(col):
    data_types = [determine_value_datatype(s) for s in col]
    return mode(data_types)

# returns list of types of each column
def determine_matrix_datatypes(matrix):
    types = [''] * matrix.shape[1]
    for i in range(matrix.shape[1]):
        col = matrix[:, i]
        types[i] = determine_column_datatype(col)
    return types