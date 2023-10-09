def diagonal_difference(arr):
    length_of_array = len(arr)
    counter = 0
    left_to_right = 0
    exit_switch = True
    while exit_switch:
        left_to_right = left_to_right + arr[counter][counter]
        counter += 1
        if counter == length_of_array:
            exit_switch = False

    right_to_left = 0
    i = 0
    j = 1
    exit_switch_2 = True
    while exit_switch_2:
        right_to_left = right_to_left + arr[i][length_of_array - j]
        i += 1
        j += 1
        if i == length_of_array:
            exit_switch_2 = False

    return abs(left_to_right - right_to_left)


matrix = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]
print(diagonal_difference(matrix))
