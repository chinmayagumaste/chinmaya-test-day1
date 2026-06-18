class Complex :
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNumber (self) :
        print (self.real ,"i+" , self.img , "j")

    def __add__(self, num2):
        NewReal=self.real + num2.real
        NewImg=self.img + num2.img
        return Complex (NewReal,NewImg)
    
               
num1=Complex(1,3)        
num1.showNumber()

num2=Complex(6,9)
num2.showNumber()

num3 =num1 +num2
num3.showNumber()