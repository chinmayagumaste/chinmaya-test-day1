num = int(input("Enter a number: "))

if num == 0:
    product = 0
else:
    product = 1
    while num > 0:
        digit = num % 10
        product = product * digit
        num = num // 10

print(product)