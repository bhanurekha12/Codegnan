  #Functions:1 A function is a block of organised, reusable code and that is used to perform a single or multiple tasks.
#2. Python gives inbuilt functions like print, you can make your own function also and these are called user defined functions.
#3. Function blocks begin with the keyword def followed by the function name and paranthesis (()).

#without using functions:
'''a=100
b=200
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)
a=1000
b=2000
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)
a=3000
b=2300
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''

#functions usage:
'''def calculate(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)
calculate(200,30)
calculate(120,31)
calculate(56,90)'''

'''def calculate(a,b):
    print("the intdiv is",a//b)
    print("the powerval is",a**b)
    print("the modulusval is",a%b)
calculate(12,34)'''


'''def add(a,b):
    print(a+b)
add(4,9)'''

#recursive:
'''while True:
    def add():
        a=int(input("a value:"))
        b=int(input("b value:"))
        print(a+b)
    add()'''

'''def add():
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)
    add()
add()'''

'''def fullname():
    fname=input("first name:")
    lname=input("last name:")
    print((fname+" "+lname).title())
fullname()'''

#task:
'''def solve():
    a=int(input("Enter a value:"))
    b=int(input("Enter b value:"))
    option=int(input("enter option:"))
    if option == 1:
        print(a+b)
    elif option == 2:
        print(a-b)
    elif option == 3:
        print(a*b)
    solve()
solve()'''

'''while True:
        a= int(input("a value"))
        b=int(input("b value"))
        option = int(input(choose the option
                           1. add
                           2. sub
                           3. mul))
        if option==1:
            add()
        elif option==2:
            sub()
        elif option==3:
            mul()'''
        
# split bill task:
'''def bill():
    persons=10
    amount=10000
    split=10000/10
    print(split)
bill()'''

'''def bill():
    person=int(input("enter number of persons:"))
    amount=int(input("enter amount:"))
      split=amount//person
    print(split)
bill()'''



'''def splitbill():
person=int(input("enter number of persons:"))
amount=int(input("enter amount:"))
split=amount/person
print(f"splitbill is {split}")
print("Split bill is {}".format(split))
splitbill()''' 



#Diff btw return and print:
#Print:Print just shows the human user input in a console.
#Return:Will terminate the function and gives back a value from function.

'''def add(a,b):
    print(a+b)
add(2,6)'''

'''def add(a,b):
    return(a+b)
print(add(1,8))'''

'''def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
add(1,5)'''

'''def add(x,y):
    c=x+y
    d=x%y
    e=x*y
    return c
    return d
    return e
print(add(3,6))'''#only the first return would be working and after that it would terminate .

'''def add(a,b):
    c=a+b
    d=a*b
    e=a-b
    return c,d,e
print(add(2,8))'''#if we need all the values to be printed it should be written  in single line



  

 

































