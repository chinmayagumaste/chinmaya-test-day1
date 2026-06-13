def print_list (list , idx):
    if (idx==len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
my_list = [1, 2, 3, 4, 5]
print_list(my_list, 0)