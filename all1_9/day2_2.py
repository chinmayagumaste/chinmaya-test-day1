marks=input("Enter your marks: ")
if int(marks) >= 90:
    print("Grade A")
elif (int(marks) < 90 and int(marks) >=80):
    print("Grade B")
elif (int(marks) < 80 and int(marks) >=70):
    print("Grade C")
else:
    print("Grade D")