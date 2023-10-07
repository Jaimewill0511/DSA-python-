def mini_max_sum(arr):
    arr.sort()
    left_sum = sum(arr[:4])
    right_sum = sum(arr[1:])
    print(left_sum, right_sum)


mini_max_sum([1, 3, 5, 7, 9])
