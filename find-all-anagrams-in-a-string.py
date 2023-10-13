def find_all_anagrams_in_a_string(s, p):
    s_count, p_count = {}, {}  # initialize hashmap
    if len(s) < len(p):
        return []
    for i in range(
            len(p)):  # filling up the first hashmap by looping and using the stop as the length of the smaller string
        s_count[s[i]] = 1 + s_count.get(s[i],
                                        0)  # adding the first value of the string in the hashmap but also putting a check to make incase its not there it will be assigned to zero
        p_count[p[i]] = 1 + p_count.get(p[i],
                                        0)  # we use this to make sure python doesn't return this value doesn't exist

    if s_count == p_count:
        res = [0]
    else:
        res = []  # add the zero as the first item of our result folder

    left_pointer = 0
    for right_pointer in range(len(p), len(s)):
        s_count[s[right_pointer]] = 1 + s_count.get(s[right_pointer], 0)
        s_count[s[left_pointer]] -= 1

        if s_count[s[left_pointer]] == 0:
            s_count.pop(s[left_pointer])

        left_pointer += 1

        if s_count == p_count:
            res.append(left_pointer)
    return res


s = "cbaebabacd"
p = "abc"
print(find_all_anagrams_in_a_string(s, p))
