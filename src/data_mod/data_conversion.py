import numpy as np

def determine_file_extension(filename):
    if type(filename) != str:
        return "none"
    return filename.split(".")[-1]

def file_to_matrix(filename, delimiter = ","):
    file_extension = determine_file_extension(filename)
    if (file_extension == "csv"):
        return csv_to_matrix(filename)
    elif (file_extension == "txt"):
        return txt_to_matrix(filename, delimiter)
    else:
        return -1 # to be implemented later

def csv_to_matrix(filename):
    return np.loadtxt(filename, dtype=str, delimiter=',')

def txt_to_matrix(filename, delimiter):
    return np.loadtxt(filename, dtype=str, delimiter=delimiter)