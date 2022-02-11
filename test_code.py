#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This program is used to test the function which returns majority element in the given list.
# A majority element is defined as an element in list which occurs at least n/2 times where
# n = length of list

import gdown, time

# Downloading code to be tested from Google Drive

url = 'https://drive.google.com/uc?id=1yf558X7Tvt2AABqZxjrcIJgBs7n6l9Cc'
output = 'actual_code.py'
gdown.download(url, output, quiet=False)

time.sleep(3)

# Importing the function to be tested
from actual_code import get_majority_element

# Function which validates actual function
def my_get_majority_element(arr):
    
    if(len(arr) == 0):
        return None
    
    maj_index = 0
    count = 1
    for i in range(1, len(arr)):
        if(arr[maj_index] == arr[i]):
            count += 1
        else:
            count -= 1
        
        if(count == 0):
            maj_index = i
            count = 1
    
    #check if arr[maj_index] is occuring n/2 times
    count = 0
    for i in range(0, len(arr)):
        if(arr[i] == arr[maj_index]):
            count += 1
    
    if(count >= len(arr)/2):
        return arr[maj_index]
    
    return None

# List of input data to be tested
test_data = [
    [1, 1, 2],
    [1,2,3,4,5],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    []
]

# Iterating over test_cases and validating for each test case
for input_arr in test_data:
    
    try:
        expected_output =  my_get_majority_element(input_arr)
        actual_output = get_majority_element(input_arr)

        assert actual_output == expected_output
        
        print("Test case passed for input {}".format(input_arr))
    except AssertionError as e:
        print("Test case failed for input {} Actual Output: {} Expected Output: {}".format(input_arr, actual_output, expected_output))
    except Exception as e:
        print("Test case execution for input: {} failed with below error\n {}".format(input_arr, e))


# In[ ]:




