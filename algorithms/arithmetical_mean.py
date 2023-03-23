def below_arithmetical_mean(list_1):
    new_list = []
    ar_mean = sum(list_1)/len(list_1)

    for i in range(len(list_1)):
        if list_1[i] < ar_mean:
            new_list.append(list_1[i])
    print(new_list)


below_arithmetical_mean([1, 3, 5, 6, 4, 10, 2, 3])
