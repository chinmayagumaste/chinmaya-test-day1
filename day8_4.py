x=int(input("Enter a number: "))
i=0
sum=0
while i<=x:
    if (x%2==0):
        sum=sum+i
    i=i+1
print("The sum of even numbers from 1 to", x, "is:", sum)