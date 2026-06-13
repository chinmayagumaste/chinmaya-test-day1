count=0
num = int(input("Enter a number: "))
num_1=num
num_2=num
while num > 0:
     num = num // 10
     count = count + 1
     digi=num_1%2
     print(digi)
     sum=digi^3
     print(sum)
if sum==num_2 : 
    print("Armstrong") 
else :
     print ("Not Armstrong")     