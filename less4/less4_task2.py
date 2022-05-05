my_list=[300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(my_list)
my_list_more = [my_list[num] for num in range(0, len(my_list)) if my_list[num]>my_list[num-1]]
print(my_list_more)