import pytest
import data_conversion
import numpy as np

def test_determine_file_extension():
    assert data_conversion.determine_file_extension("test.txt") == "txt"
    assert data_conversion.determine_file_extension("hello_darkness_my_old_friend.csv") == "csv"
    assert data_conversion.determine_file_extension("testingtesting123.xlsx") == "xlsx"

def test_file_to_matrix():
   file_to_matrix_test_array = data_conversion.file_to_matrix("src/filetomatrixtest.csv")
   assert file_to_matrix_test_array[0][0] == "hi" 
   assert file_to_matrix_test_array[0][1] == "test" 
   assert file_to_matrix_test_array[1][0] == "hello" 
   assert file_to_matrix_test_array[1][1] == "crazy" 
   assert data_conversion.file_to_matrix("randomfile.txt") == -1

def test_csv_to_matrix():
   file_to_matrix_test_array = data_conversion.csv_to_matrix("src/filetomatrixtest.csv")
   assert file_to_matrix_test_array[0][0] == "hi" 
   assert file_to_matrix_test_array[0][1] == "test" 
   assert file_to_matrix_test_array[1][0] == "hello" 
   assert file_to_matrix_test_array[1][1] == "crazy" 