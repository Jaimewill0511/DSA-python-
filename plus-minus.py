def plus_minus(arr):
    total_elements = len(arr)
    positive_count = 0
    negative_count = 0
    zero_count = 0
    for num in arr:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1
    print(positive_count / total_elements)
    print(negative_count / total_elements)
    print(zero_count / total_elements)


plus_minus([-4, 3, -9, 0, 4, 1])
