# Even First
# Your input is a list of integers, and you have to reorder its entries so that the even entries appear first. You are required to solve it without allocating additional storage (operate with the input list).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]
def even_first(list_of_int):
    # left = 0
    # right = len(list_of_int) - 1
    # while left < right:
    #     if list_of_int[left] % 2 == 0:
    #         left += 1
    #     else:
    #         list_of_int[right], list_of_int[left] = list_of_int[left], list_of_int[right]
    #         right -= 1
    #
    # return list_of_int
    j = -1
    for i in range(len(list_of_int)):
        if list_of_int[i] % 2 == 0:
            j += 1
            t = list_of_int[i]
            list_of_int[i] = list_of_int[j]
            list_of_int[j] = t
    return list_of_int


print(even_first([7, 3, 5, 6, 4, 10, 3, 2]))
print(even_first([1, 4, 5, 3, 6, 4, 10, 3, 2]))
print(even_first([0, 1, 2, 3, 4, 5, 54, 6, 55, 7, 8]))
