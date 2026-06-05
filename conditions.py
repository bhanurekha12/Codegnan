#if conditions by using comparision operators:<,>,<=,>=,!=,==
'''a=10
if a<1:
    print("true")'''

'''a=10
if a>1:
    print("true")'''

'''a=33
b=12
if a>b:
    print("yes")'''


'''a=5
b=7
if a<=b:
    print("true")'''

'''a=15
b=7
if a>=b:
    print("greater")'''

'''a=3
b=6
if a!=b:
    print("not equal")'''

'''a=int(input("a value"))
b=int(input("b value"))
if a>b:
    print("greater")'''

'''a= int(input(" enter a value:"))
if a!=20:
    print("true")'''

'''a="python"
if a=="python":
    print("true")'''

'''a= input("enter data:")
if a=="python":
    print("true")'''


##if condition by using logical operators: and ,or, not:

'''a=2
b=4
if a<b and b>a:
    print("true")'''

'''a=2
b=4
if a<b and b<a:
    print("true")'''

'''a=5
b=7
if a<=b and b>=a:
    print("true")'''

'''a=9
b=11
if a!=b and b==a:
    print("true")'''

'''a=1
b=3
if a<b or b>a:
    print("true")'''

'''a=2
b=4
if a!=b or a==b:
    print("true")'''

'''a=5
b=10
if not a<b:
    print("true")'''

'''a=5
b=10
if not a>b:
    print("true")'''

'''a=5
b=10
if not a<b and b>a:
    print("true")'''

'''a=5
b=10
if not a<b or b>a:
    print("true")'''


'''a=4
b=9
if not a<b or a!=b:
    print("true")'''

#if condition by using identify operators:is ,is not
'''a=2
if type(a) is int:
    print("it is integer")'''

'''a=2
if type(a) is  not int:
    print("it is integer")'''

'''a=int(input("enter value:"))
if type(a) is int:
    print("true")'''

'''a=2.8
if type(a) is float:
    print("it is float")'''

'''a=2.8
if type(a) is not  float:
    print("it is float")'''

'''a= float(input("enter a value"))
if type(a) is float:
    print("true")'''

'''a="python"
if type(a) is str:
    print("true")'''

'''a=11
if type(a) is str:
    print("yes")'''

#if condition by using membership operators: in, not in
'''a=[10,20,30,40,50]
if 50 in a:
    print("true")'''

'''a=[10,20,30,40,50]
if 30  not in a:
    print("true")'''

'''a=[10,20,30,40,50]
if 60  not in a:
    print("true")'''

'''a=int(input("enter a value:"))
if 40 in a:
    print("true")'''#error

'''a=[4,5,6,7,8,9,10]
b=int(input("value"))
if b in a:
    print("true")'''

##if-else conditions by using comparision:

'''a=2
b=4
if a<b:
    print("true")
else:
    print("false")'''


'''a=2
b=4
if a>b:
    print("true")
else:
    print("false")'''


'''a=7
b=9
if a!=b:
    print("true")
else:
    print("false")'''


'''a=int(input("enter a value:"))
b=int(input("enter b value:"))
if a>b:
    print("less")
else:
    print("true")'''



#logical operators: and ,or not
'''a=100
b=150
if a>b and b<a:
    print("greater")
else:
    print("less")'''

'''a=100
b=150
if a>b or b<a:
    print("greater")
else:
    print("less")'''

'''a=12
b=15
if not b>a:
    print("true")
else:
    print("false")'''

'''a=int(input("enter a value:"))
b=int(input("enter b value:"))
if a>b and b<a:
    print("greater")
else:
    print("less")'''

'''a=int(input("enter a value:"))
b=int(input("enter b value:"))
if a>b or b<a:
    print("greater")
else:
    print("less")'''

'''a=int(input("enter a value:"))
b=int(input("enter b value:"))
if not b<a:
    print("greater")
else:
    print("less")'''

#membership operators:in not in

'''a=[12,13,14,15,16,17]
if 16 in a:
     print("true")
else:
    print("false")'''

'''a=[11,12,13,14,15]
b=int(input("enter a value:"))
if b in a:
    print("true")
else:
    print("false")'''


'''a=[12,13,14,15,16,17]
if 18  not  in a:
     print("not in list")
else:
    print("in list")'''

'''a=[11,12,13,14,15]
b=int(input("enter a value:"))
if b  not in a:
    print("true")
else:
    print("false")'''


#identifier operators: is ,is not
'''a=12
if type(a) is int:
    print("interger")
else:
    print("not an integer")'''

'''a=input("enter a value:")
if type(a) is int:
    print("is integer")
else:
    print("not an integer")'''

'''a=133
if type(a) is not int:
    print("false")
else:
    print("true")'''

'''a=input("enter a value:")
if type(a) is not int:
    print("false")
else:
    print("true")'''

'''a=input("enter a value:")
if type(a) is str:
    print("is str")
else:
    print("not a str")'''

'''a="python"
if type(a) is not str:
    print("not a str")
else:
    print("is a str")'''

'''a=input("enter a value")
if type(a) is str:
    print("true")
else:
    print("false")'''


















      
