import pytest
import determine_datatype as dd
import numpy as np

def test_is_boolean():
    assert dd.is_boolean("True") == True
    assert dd.is_boolean("False") == True
    assert dd.is_boolean("true") == True
    assert dd.is_boolean("false") == True
    assert dd.is_boolean("random") == False

def test_is_integer():
   assert dd.is_integer("five") == False
   assert dd.is_integer("5") == True
   assert dd.is_integer("5.0") == False
   assert dd.is_integer("-8") == True
   assert dd.is_integer("200") == True

def test_is_float():
    assert dd.is_float("5.0") == True
    assert dd.is_float("5") == False
    assert dd.is_float("-51") == False
    assert dd.is_float("-42.3") == True

def test_determine_value_datatype():
    assert dd.determine_value_datatype("True") == "bool" 
    assert dd.determine_value_datatype("toxic") == "str" 
    assert dd.determine_value_datatype("-56") == "int"
    assert dd.determine_value_datatype("79.3") == "float" 

def test_determine_column_datatype():
    str_array = ["str1", "5.0", "5", "strings", "randomness"]
    float_array = ["-7.9", "0.3", "4", "-2", "float?", "6.8", "456.321", "3.141592"]
    int_array = ["9", "-3002", "this is definitely an integer", "567", "1.0", "2", "-1024"]
    bool_array = ["True", "False", "Maybe", "True", "False"]
    assert dd.determine_column_datatype(str_array) == "str"
    assert dd.determine_column_datatype(float_array) == "float"
    assert dd.determine_column_datatype(int_array) == "int"
    assert dd.determine_column_datatype(bool_array) == "bool"
    int_array2 = ["label", "int", "5", "4"]
    assert dd.determine_column_datatype(int_array2, False) == "str"
    assert dd.determine_column_datatype(int_array2, True) == "int"

def test_determine_matrix_datatypes():
    test_matrix = np.array([["test", "1.1", "2"], ["str", "4.2", "3"], ["hello", "-1.2", "-3"]])
    result = dd.determine_matrix_datatypes(test_matrix)
    real_result = np.array(["str", "float", "int"])
    assert np.array_equiv(result, real_result) == True
    test_matrix2 = np.array([["Label", "Label", "Label"], ["True", "2", "1.0"], ["False", "-7", "-0.21"], ["True", "43", "420.1"]])
    result2 = dd.determine_matrix_datatypes(test_matrix2)
    real_result2 = np.array(["bool", "int", "float"])
    assert np.array_equiv(result2, real_result2) == True

def test_column_contains_label():
    label_array = np.array(["label", "1", "labels", "testing"])
    assert dd.column_contains_label(label_array) == True
    no_label_array = np.array(["False", "strings", "terror", "1.4"])
    assert dd.column_contains_label(no_label_array) == False

def test_matrix_contains_labels():
    label_matrix = np.array([["Label", "Label", "Label"], ["True", "2", "1.0"], ["False", "-7", "-0.21"], ["True", "43", "420.1"]])
    assert dd.matrix_contains_labels(label_matrix) == True
    no_label_matrix = np.array([["Label", "Label", "1"], ["True", "2", "1.0"], ["False", "-7", "-0.21"], ["True", "43", "420.1"]])
    assert dd.matrix_contains_labels(no_label_matrix) == False

def test_calculate_numeric_percentage():
    label_matrix = np.array([["Label", "Label", "Label"], ["True", "2", "1.0"], ["False", "-7", "-0.21"], ["True", "43", "420.1"]])
    assert dd.calculate_numeric_percentage(label_matrix) == 0.67
    no_label_matrix = np.array([["Label", "Label", "1"], ["True", "2", "1.0"], ["False", "-7", "-0.21"], ["True", "43", "420.1"]])
    assert dd.calculate_numeric_percentage(no_label_matrix) == 0.58

def test_matrix_information_dictionary():
    label_matrix = np.array([["Label", "Label", "Label"], ["True", "2", "1.0"], ["False", "-7", "-0.21"], ["True", "43", "420.1"]])
    real_result = {"labels": True, "datatypes": np.array(["bool", "int", "float"]), "numeric percentage": 0.67}
    result = dd.matrix_information_dictionary(label_matrix)
    assert real_result["labels"] == result["labels"]
    assert np.array_equiv(real_result["datatypes"], result["datatypes"])
    assert real_result["numeric percentage"] == result["numeric percentage"]
    no_label_matrix = np.array([["Label", "Label", "1"], ["True", "2", "1.0"], ["False", "-7", "-0.21"], ["True", "43", "420.1"]])
    real_result2 = {"labels": False, "datatypes": np.array(["bool", "int", "float"]), "numeric percentage": 0.58}
    result2 = dd.matrix_information_dictionary(no_label_matrix)
    assert real_result2["labels"] == result2["labels"]
    assert np.array_equiv(real_result2["datatypes"], result2["datatypes"])
    assert real_result2["numeric percentage"] == result2["numeric percentage"]
