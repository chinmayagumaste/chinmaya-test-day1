def sum(x):
    total = 0
    for i in range(1, x + 1):
        total += i
    return total

num = int(input("Enter a number: "))
result = sum(num)
print("The sum of the first", num, "natural numbers is:", result)
