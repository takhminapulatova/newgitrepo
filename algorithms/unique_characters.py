def unique_characters(string):
    sorted_str = sorted(string)
    for i in range(len(sorted_str)):
        if sorted_str[i-1] == sorted_str[i]:
            # print(False)
            return False
    # print(True)
    return True


unique_characters('abcde')
unique_characters('aabcde')
