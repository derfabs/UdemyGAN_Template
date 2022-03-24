def list_max(my_list):
    result = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > result:
            result = my_list[i]

    print(result)


l1 = [-2, 1, 2, -10, 22]
list_max(l1)

l2 = [-5, 1, 2, 10, 212]
list_max(l2)
