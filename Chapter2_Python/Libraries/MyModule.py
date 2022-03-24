def list_max(input_list):
    result = input_list[0]
    for i in range(len(input_list)):
        if input_list[i] > result:
            result = input_list[i]

    print(result)


def list_min(input_list):
    result = input_list[0]
    for i in range(len(input_list)):
        if input_list[i] < result:
            result = input_list[i]

    print(result)
