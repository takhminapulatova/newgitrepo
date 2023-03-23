def split_half(string):
    l = len(string)
    if l % 2 == 0:
        h = l // 2
        new_str = string[h:] + string[:h]
        print(new_str)
    else:
        h = (l // 2) + 1
        new_str = string[h:] + string[:h]
        print(new_str)


split_half('bbbbbcaaaaa')
