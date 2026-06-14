rev=0
num=int(input("Enter a number: "))
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print( rev)

num = 5382
rev1 = int(str(num)[::-1])
print(rev1)