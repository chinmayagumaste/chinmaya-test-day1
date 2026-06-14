def sum (x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x + sum(x - 1)
    
num = int(input("Enter a number: "))
result = sum(num)
print("The sum of the first", num, "natural numbers is:", result)


def print_list (list , idx):
    if (idx==len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
my_list = [1, 2, 3, 4, 5]
print_list(my_list, 0)
