# Syntax for function
def function():
    print('Independent Function')


# Syntax for Class
class Classname:
   # define a function , same function in class(OOPS concept) are  called as 'Method'
   def method(self):
       print("Inside 'method' of 'Classname'")

function()
## will display - Independent Function'
# method()
## will give an error as now we cannot execute 'method' directly

# Right syntax

#Classname.method()
# TypeError: Classname.method() missing 1 required positional argument: 'self'

# Classname.method(self)
# NameError: name 'self' is not defined
# The class above has not been allocated an memory/space and not executable yet, Class is just the blue print of
# the task we want to achieve

# We need to create something on computer memory/space which exists physcially -- that soemthing is Object

## Syntax of object creation
object1 = Classname()
object2 = Classname()

Classname.method(object1)
Classname.method(object2)

## Above can be written as below
object1.method()

# Inside 'method' of 'Classname'

