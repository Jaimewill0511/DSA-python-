def mini_max_sum(arr):
    sorted_array = sorted(arr)
    left_arr = list(sorted_array)
    right_arr = list(sorted_array)
    del left_arr[-1]
    del right_arr[0]
    left_sum, right_sum = 0, 0
    for num in left_arr:
        left_sum += num
    for num in right_arr:
        right_sum += num
    print(left_sum, right_sum)


mini_max_sum([1, 3, 5, 7, 9])
