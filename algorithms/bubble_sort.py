# Bubble Sort
# Implement the bubble sort algorithm that is sorting in descending order.
def bubble_sort_in_descending_order(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list) - 1 - i):
            if my_list[j] < my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    print(my_list)


bubble_sort_in_descending_order([2, 4, 5, 99, 43, 50])
