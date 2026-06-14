num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,9,8,7,6,5,4,3,2,1)
x = int(input("Enter a number: "))
idx=0
for el in num:
    if el == x:
        print("Number found at index", idx)
        break
    idx+=1
else:    print("Number not found")  