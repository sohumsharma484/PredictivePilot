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
    
def determine_column_datatype(col, contains_label=False):
    data_types = [determine_value_datatype(s) for s in col]
    if contains_label:
        data_types = data_types[1:]
    return mode(data_types)

# returns list of types of each column
def determine_matrix_datatypes(matrix):
    contains_labels = matrix_contains_labels(matrix)
    types = [''] * matrix.shape[1]
    for i in range(matrix.shape[1]):
        col = matrix[:, i]
        types[i] = determine_column_datatype(col, contains_labels)
    return types

def column_contains_label(col):
    return determine_value_datatype(col[0]) == "str"

# if a matrix contains labels, we will remove the first row when accounting for types
def matrix_contains_labels(matrix):
    for i in range(matrix.shape[1]):
        col = matrix[:, i]
        if not column_contains_label(col):
            return False
    return True


def calculate_numeric_percentage(matrix):
    used_matrix = matrix
    if matrix_contains_labels(matrix):
        used_matrix = matrix[1: , :]
    count = 0
    for row in used_matrix:
        for el in row:
            if determine_value_datatype(el) == "float" or determine_value_datatype(el) == "int":
                count += 1
    return np.round(count/(used_matrix.shape[0] * used_matrix.shape[1]) * 100)/100

def matrix_information_dictionary(matrix):
    contains_labels = matrix_contains_labels(matrix)
    datatypes = determine_matrix_datatypes(matrix)
    numeric_percentage = calculate_numeric_percentage(matrix)
    information_dictionary = {"labels": contains_labels, "datatypes": datatypes, "numeric percentage": numeric_percentage}
    return information_dictionary