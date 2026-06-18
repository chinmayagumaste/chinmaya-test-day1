class Student :
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def   welcome(self) :
        print ("Welcome to college",self.name)  
        

s1=Student("Karan",97)
print (s1.name,s1.marks)

s2=Student ("Madhurmanoj",100)
print (s2.name , s2.marks,)
s2.welcome()

        