a=int(input("Enter a 1st number: "))
b=int(input("Enter a 2nd number: "))
c=int(input("Enter a 3rd number: "))
d=int(input("Enter a 4th number: "))

if a > b and a > c and a > d:
    print("The greatest number is: ", a)
elif b > c and b > d:
    print("The greatest number is: ", b)
elif c > d:
    print("The greatest number is: ", c)
else:
    print("The greatest number is: ", d)