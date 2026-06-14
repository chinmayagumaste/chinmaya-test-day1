num=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter a number: "))
i=0
while i<len(num):
    if num[i]==x:
        print("Number found at index", i)
        break     
    i+=1
else:
    print("Number not found")
    