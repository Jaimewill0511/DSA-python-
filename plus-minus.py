def plus_minus(arr):
    a, b, c = 0, 0, 0
    for i in arr:
        if i > 0:
            a = a + 1
        elif i < 0:
            b = b + 1
        else:
            c = c + 1
    print(a / len(arr))
    print(b / len(arr))
    print(c / len(arr))


plus_minus([1, 1, 0, -1, -1])
