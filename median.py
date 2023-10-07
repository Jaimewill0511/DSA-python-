import math


def find_median(arr):
    # Write your code here
    arr.sort()
    length_of_list = len(arr)
    length_of_list = math.floor(length_of_list / 2)
    median_number = arr[length_of_list]
    return median_number

