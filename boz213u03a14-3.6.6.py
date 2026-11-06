my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
clean_list = []


for i in range(len(my_list)):
    if my_list[i] in clean_list:
        continue
    else:
        clean_list.append(my_list[i])
my_list = clean_list
print("The list with unique elements only:")
print(my_list)
