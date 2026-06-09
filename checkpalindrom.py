x=['a', 'b', 'c']
y=['a', 'b', 'a']
x_copy=x.copy()
y_copy=y.copy()
x_copy.reverse()
y_copy.reverse()
print(x_copy)
print(y_copy)
if x==x_copy:
    print("The list is a palindrome")
else:    print("The list is not a palindrome")
if y==y_copy:
    print("The list is a palindrome")
else:    print("The list is not a palindrome")