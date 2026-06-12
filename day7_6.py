n=int(input("Enter a number: "))
sum=1
for i in range(1, n + 1):
    sum *= i
print("Product of first", n, "numbers is", sum)
