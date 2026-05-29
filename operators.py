Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#operators
#arthematic
a=3
b=5
print(a+b)
8
print(a-b)
-2
print(a*b)
15
print(a//b)
0
print(a/b)
0.6
print(a**b)
243
#they would be considering the same values which are declared at start.
#assignment(these would use the values which are latest value assigned to the variables...)
a=6
b=2
a+=b
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
10
a-=1
a
9
a*=3
a
27
a//=4
a
6
a/=2
a
3.0
a**=3
a
27.0
a%=4
a
3.0
#comparision/ relational operators
a=4
b=7
a<b
True
a>b
False
b>=a
True
a<=b
True
a!=b
True
a==b
False
a=6
b=6
a==b
True
#logical operators
a=4
b=9
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
#(or)
a=4
b=9
a<b or a>b
True
a<b or b>a
True
a<=b or b>=a
True
a!=b or a==b
True
#(not)
not True
False
not False
True
#(in and operator both should be true ..in or operator any one true is enough..not operator is opposite of wht mentioned)
#identify operators
a=5
SyntaxError: invalid syntax
a=3
if type(a) is int:
    print("it is int")

    
it is int
if type(a) is not int:
    print("true")

    
b=4.5
>>> if type(b) is float:
...     print("it is float")
... 
...     
it is float
>>> if type(b) is not float:
...     print("false")
... 
...     
>>> 
>>> #membership operators
...     
>>> a=2,3,4,6,1,8
>>> if 4 in a:
...     print(yes)
... 
...     
Traceback (most recent call last):
  File "<pyshell#82>", line 2, in <module>
    print(yes)
NameError: name 'yes' is not defined
>>> a=2,3,4,5,6,1
>>> if 5 in a:
...     print(5)
... 
...     
5
>>> if 8 not in a:
...     print(8)
... 
...     
8
>>> if 9 not in a:
...     print(9)
... 
...     
9
>>> if 20 in a:
...     print(20)
... 
...     
