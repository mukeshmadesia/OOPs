from abc import ABC

class Calculator:
    def __init__(self):
        print('inside calculator')

    def addmethod(self):
        print('inside calculator add method')

    def submethod(self):
        print('inside calculator submethod')

    def percentage(self):
        print('Inside calculator percentage')

class Add(Calculator):
    def __init__(self):
        #super().__init__()
        print('Add class')

    def addmethod(self,x,y):
        return x + y


class Sub(Calculator):
    def __init__(self):
        print('Sub class')

    def submethod(self,x,y):
        return x - y


class Multiply(Add,Sub):

    def __init__(self):
        print('Multiply class')

    def multiplymethod(self, x, y):
        return x * y


# We need  to update the submethod to y-x instead of x-y, example of abstract method
class Divide(Sub, Add):

    def __init__(self):
        print('Divide class')

    def submethod(self, x, y):
        return y-x

    def divide(self, x, y):
        return x/y

    def __add__(self, other):
        x





print('Run0')
calc = Add()

print(calc.addmethod(2, 3))

cal2 = Multiply()

print('Run1')
print(cal2.submethod(3, 4))

print('Run2')
cal2.percentage()


print('Before create Divide Instance')
cal3 = Divide()

print('Run3')

print(cal3.submethod(3, 4))



