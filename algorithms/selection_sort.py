# Selection Sort
# Implement the selection sort algorithm that is sorting in descending order.
def selection_sort_in_descending_order(my_list):
    for i in range(len(my_list)):
        max_num = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] > my_list[max_num]:
                max_num = j
        my_list[i], my_list[max_num] = my_list[max_num], my_list[i]

    print(my_list)


selection_sort_in_descending_order([2, 4, 5, 99, 43, 50])
