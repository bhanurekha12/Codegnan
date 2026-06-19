#Local and Global Variables/scope of the variable:Variables inside and outside the function is called global and local varibales.
#A variable defined above the function and is accesible to the entire global space is called global variable.
#A variable is defined inside the function is called local variable.

#global variable:case1
'''a=3
def check():
    print("inside value is:",a)
check()
print("outside variable is:",a)'''

#case2:
'''a=5
def check():
    a=2
    a=a**5
    print("inside value is",a)
check()
print("Outside value is",a)'''


#case3:both global and local variables
'''a=6
b=10
def check():
    a=3
    print("Inside value is",a)
    a=15
    print("updated value is",a+5)
    b=20
    b=b+a #local variable
    print("value of b is",b)
check()
print("a value is",a)
print("b value is",b)'''

#usage of global keyword: when user wants to access the global variable inside the function
#directly and carry forward the updated value even outside the function then we need to use global keyword.

#case4:
'''a=5
def final():
    global a,b
    print("inside value",a)
    a=6
    print("updated value",a)
    b=15
    b=15+a
    print("b value",b)
final()
print("value of a",a)
print("value of b ",b)'''


  


























