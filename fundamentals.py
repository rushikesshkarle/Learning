class calculations:
    def add(self,a,b):
        return a+b
    def substract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b
    def modulus(self,a,b):
        return a%b
    def exponent(self,a,b):
        return a**b

calc=calculations()
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("1 for add , 2 for substract, 3 for multiply, 4 for divide, 5 for modulus, 6 for exponent:"))

if c==1:
    print("Output:",calc.add(a,b))
elif c==2:
    print("Output:",calc.substract(a,b))
elif c==3:
    print("Output:",calc.multiply(a,b))
elif c==4:
    print("Output:",calc.divide(a,b))
elif c==5:
    print("Output:",calc.modulus(a,b))
elif c==6:
    print("Output:",calc.exponent(a,b))
else:
    print("Invalid input")