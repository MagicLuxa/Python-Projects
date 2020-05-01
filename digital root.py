def digital_root(num):
    while num >= 10:
        num_array = [int(x) for x in str(num)]
        print(num_array)
        temp = 0
        for i in range(len(num_array)):
            temp += num_array[i]
        num = temp
    print(num)


digital_root(999)