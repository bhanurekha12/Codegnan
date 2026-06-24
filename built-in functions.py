#print(dir())
#print(dir("__builtins__"))
'''a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a))'''

#fromkeys():

'''b=dict.fromkeys(a)
print(b)'''

'''c=dict.fromkeys(a,"bhanu")
print(c)'''

'''c["g"]="python"
print(c)'''

#eval():

'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''


'''while True:
    a=float(input("a value"))
    b=float(input("b value"))
    print(a+b)'''


'''while True:
    a=input("a value")
    b=input("b value")
    print(a+b)'''

'''while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)'''                  # anything given in str should be in quotes.


#zip()-> we can combine multiple collections into one collection.
'''a=[10,20,30,40]
names=["bhanu","rekha","deeksha","tanmai"]
print(a+names)                                  #[10, 20, 30, 40, 50, 'bhanu', 'rekha', 'deeksha', 'tanmai']

b=zip(a,names)
print(b)                                    #[10, 20, 30, 40, 50, 'bhanu', 'rekha', 'deeksha', 'tanmai']

c=list(zip(a,names))
print(c)                                    #[(10, 'bhanu'), (20, 'rekha'), (30, 'deeksha'), (40, 'tanmai')]

c=tuple(zip(a,names))
print(c)                                        #((10, 'bhanu'), (20, 'rekha'), (30, 'deeksha'), (40, 'tanmai'))

c=set(zip(a,names))
print(c)'''                                            #{(10, 'bhanu'), (30, 'deeksha'), (20, 'rekha'), (40, 'tanmai')}
                                            

#enumerate-> we can counter to the collection
names=["bhanu","rekha","deeksha","tanmai"]
'''for i in range(len(names)):
       print(i,names[i])'''

'''b=list(enumerate(names))
print(b)'''                                #[(0, 'bhanu'), (1, 'rekha'), (2, 'deeksha'), (3, 'tanmai')]

'''b=list(enumerate(names,100))
print(b)'''                                   #[(100, 'bhanu'), (101, 'rekha'), (102, 'deeksha'), (103, 'tanmai')]

'''b=dict(enumerate(names))
print(b) '''                                   #{0: 'bhanu', 1: 'rekha', 2: 'deeksha', 3: 'tanmai'}

'''b=set(enumerate(names))
print(b)'''                                        #{(0, 'bhanu'), (1, 'rekha'), (2, 'deeksha'), (3, 'tanmai')}


#Body Mass Index task:(BMI)
'''while True:
    weight=float(input("enter weight:"))
    height=float(input("enter height:"))
    bmi=weight/(height**2)
    if bmi<=18.5:
        print("Under Weight")
    elif 18.5<bmi<24.5:
        print("Normal Weight")
    elif 24.5<bmi<29.5:
        print("Over weight")
    else:
        print("obesity")'''

#Anonmous functions:Anonmous functions are name less functions and we use a keyword called as lambda to create anonmous functions.
#write a fuction to calculate 2*x+5 where x=5
# using functions:
'''def calculate():
    x=5
    y=2*x+5
    print(y)
calculate()'''

#syntax
#a=lambda arg:expr
'''a=lambda x:2*x+5
print(a(5))'''


'''a= int(input("a value:"))
b=lambda x:2*x+5
print(b(a))'''

'''a="codegnan"            #o/p:CODEGNAN
b=lambda  a:a.upper()
print(b(a))'''


'''a="python course"
b=lambda a:a.title()
print(b(a))'''                  #o/p:Python Course

#multiply:
'''a=int(input("a value"))
b=int(input("b value"))
c= lambda a,b:a*b
print(c(a,b))'''


#
'''fname="Bhanu"
lname="Rekha"
fulname = lambda fname,lname:fname+" "+lname
print(fulname(fname,lname))'''

'''a=input("fname")
b=input("lname")
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''

#using generators and anonmous function
'''a,b=[x for x in input("enter names").split(",")]
c= lambda a,b:(a+" "+b).title()
print(c(a,b))'''


#print even numbers
'''a=[2,8,10,13,15,17,20,23,50,80,90,100]
for i in  a:
    if i%2==0:
        print(i)'''


#filter()

'''a=[2,8,10,13,15,17,20,23,50,80,90,100]
b=list(filter(lambda x:x%2==0,a))
print(b)'''


 #[],(),{}
'''a=[]
print(type(a))

b=()
print(type(b))

c={}
print(type(c))

d=set()
print(type(d))'''

'''a=[[],(),{},set(),"",None,4.6,2,"python",4+2j,True,False]
b=list(filter(None,a))
print(b)'''
                                          # o/p: [4.6, 2, 'python', (4+2j), True]
#map()-> each object from a collection and forms a new collection called map.

'''a=[2,6,9,13,17,20]
b=[3,7,12,15,19,23]
c=list(map(max,a,b))
print(c)                       # o/p:[3, 7, 12, 15, 19, 23]


d=list(map(min,a,b))            #[2, 6, 9, 13, 17, 20]
print(d)'''

#run time for str:
#str
'''a=int(input("Data1"))
b=int(input("Data2"))
print(a+b)'''


'''a,b=input("enter names:").split(",")
print(a+b)'''


'''a,b=[x for x in input("data").split(",")]
print(a+b)'''

'''a,b=map(str,input("enter names:").split(","))
print(a+b)'''

#int

'''a=int(input("a value"))
b=int(input("b value"))
print(a+b)'''

'''a,b=[int(x) for x in input("enter values:").split(",")]
print(a+b)'''

'''a,b=int(input("values").split(","))
print(a+b)'''#error

'''a,b=map(int,input("values").split(","))
print(a+b)'''


#
'''a,b=map(int,input("values").split(","))
print(a+b)'''


'''a=list(map(int, input("enter the values").split(",")))
print(a)'''


'''a=tuple(map(int,input("enter values:").split(",")))
print(a)'''


'''a=set(map(int,input("enter values:").split(",")))
print(a)'''


'''a=list(map(str, input("enter values:").split(",")))
print(a)'''


'''a=input("enter the key value pairs:")
b=dict(i.split(":") for i in a.split(","))
print(b)'''


#ASCII:
# 1.chr()

'''print(chr(12))

print(chr(90))'''


# 2. ord()

'''print(ord("a"))
print(ord("A"))

print(ord(1))'''# error


#task:

'''for i in  range(65, 91):
    print(chr(i), end=" ")
for i in range(97,123):
    print(chr(i),end=" ")'''     #A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 

    
'''a="bhanu"
for i in a:
    print(i, ord(i))

b="rekha"
for i in b:
    print(i, ord(i))'''





#modules:

#1.A module in python is a single python file it consists python code .
#2.It typically consists of functions,classes and attributes and variables that can be used in other python scripts or programs.
#3.Examples of modules include math.py , random.py or mymodule.py.

#package:
#1.A package in python is a directory containing one or more python modules and an __init__.py file .
#2. The __init__.py file can be empty or contain intialization code for the package.
#3.Examples of packages include numpy , pandas, or dgango.

#library():
#Library can consists of multiple modules and packages, organised to serve a particular purpose or domain.
#examples of libraries such as requests, numpy, pandas, and matplotlib.

#Note:Every python file is a module and import is a keyword and every python file is saved internally with variable name as __main__.
        

























