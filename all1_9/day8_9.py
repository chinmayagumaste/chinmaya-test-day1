rev=0
num=int(input("Enter a number: "))
num_copy=num
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)    
print(num_copy)
if rev==num_copy:
    print("The number is a palindrome.")
else:  
     print("The number is not a palindrome.")