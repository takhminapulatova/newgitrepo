# Increment a Number
# Write a program that takes as input a list of digits encoding a nonnegative decimal integer D and updates the list to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].
def increment_a_number(list_of_digits):
    print(list_of_digits)
    list_of_digits[-1] += 1
    for i in range(len(list_of_digits)-1, 0, -1):
        if list_of_digits[i] == 10:
            list_of_digits[i] = 0
            list_of_digits[i-1] += 1

    if list_of_digits[0] == 10:
        list_of_digits[0] = 1
        list_of_digits.append(0)

    print(list_of_digits)


increment_a_number([9, 9, 9])
increment_a_number([1, 9, 8, 9])
increment_a_number([5, 3, 9])
