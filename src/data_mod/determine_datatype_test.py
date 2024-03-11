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

def test_determine_matrix_datatypes():
    test_matrix = np.array([["test", "1.1", "2"], ["str", "4.2", "3"], ["hello", "-1.2", "-3"]])
    result = dd.determine_matrix_datatypes(test_matrix)
    real_result = np.array(["str", "float", "int"])
    assert np.array_equiv(result, real_result) == True
    test_matrix2 = np.array([["Label", "Label", "Label"], ["True", "2", "1.0"], ["False", "-7", "-0.21"], ["True", "43", "420.1"]])
    result2 = dd.determine_matrix_datatypes(test_matrix2)
    real_result2 = np.array(["bool", "int", "float"])
    assert np.array_equiv(result2, real_result2) == True