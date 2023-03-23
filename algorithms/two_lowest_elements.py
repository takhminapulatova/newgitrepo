def two_lowest_elements(list_1):
    min_el1 = min(list_1)
    list_1.pop(list_1.index(min_el1))
    min_el2 = min(list_1)
    print(min_el1, min_el2)


two_lowest_elements([198, 3, 4, 9, 10, 9, 2])
