def lonely_integer(arr):
    hash_map = {}
    count = 0
    for num in arr:
        if num in hash_map:
            hash_map[num] += 1
        else:
            hash_map[num] = count + 1
    for num, count in hash_map.items():
        if count == 1:
            return num


print(lonely_integer([1, 1, 3]))


