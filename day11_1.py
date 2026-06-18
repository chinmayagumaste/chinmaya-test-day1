class Student :
    def __init__(self,fullname,marks1,marks2,marks3):
        self.name=fullname
        self.sub1_marks=marks1
        self.sub2_marks=marks2
        self.sub3_marks=marks3
    def avg (self) :
        sum= int (self.sub1_marks+self.sub2_marks+self.sub3_marks) 
        avg_sum = sum/3
        print ("Average marks of",self.name , "is :",avg_sum)

s1=Student("Chinmaya",40,30,20)
s1.avg()           