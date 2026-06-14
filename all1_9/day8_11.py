num=int(input("Enter the number : "))
sum=0
original=num
i=1
while i <  num :
    if num % i == 0 : 
        sum=sum+i
    i+=1    
if (sum==original):
    print ("Perfect Number")
else :
    print ("Not Perfect Number")    
