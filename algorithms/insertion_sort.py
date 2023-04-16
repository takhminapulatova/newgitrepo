# Insertion Sort
# Implement the insertion sort algorithm that is sorting in descending order.
def insertion_sort_in_descending_order(my_list):
    for i in range(1, len(my_list)):
        key = my_list[i]
        j = i - 1
        while j >= 0 and key > my_list[j]:
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = key

    print(my_list)


insertion_sort_in_descending_order([2, 4, 5, 99, 43, 50])
