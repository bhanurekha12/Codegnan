Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
print(7+9)
16
a=10
print(a)
10
b=30
print(b)
30
x=100
print(x)
100
x=100
print(X)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
Z=50
print(Z)
50
#do not start a variable as number
5=10
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
7=100
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a7=100
print(a7)
100
20a=40
SyntaxError: invalid decimal literal
a0123456789=30
print(a0123456789)
30
#letters
name="bhanu"
print(bhanu)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(bhanu)
NameError: name 'bhanu' is not defined
name="bhanu
SyntaxError: unterminated string literal (detected at line 1)
name="bhanu"
print(name)
bhanu
print("name")
name
place="vjwda"
print(place)
vjwda
country="india"
print(country)
india
# special characters and underscore(-)
#=20
@=90
SyntaxError: invalid syntax
$=30
SyntaxError: invalid syntax
_=30
print(_)
30
_a=80
print(_a)
80
 x=100
 
SyntaxError: unexpected indent
_100
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    _100
NameError: name '_100' is not defined
#keywords
if=30
SyntaxError: invalid syntax
else=100
SyntaxError: invalid syntax
#single line with multiple variables
a=3,b=8
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=3;b=8
print(a+b)
11
a,b=5,8
print(a,b)
5 8
a=3,4,5,6,7,8
print(a)
(3, 4, 5, 6, 7, 8)
#multiples variables  single value
a=b=c=20
print(a,b,c)
20 20 20
a,b,c=3,4,5,6,7,8,9
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a,b,c=3,4,5,6,7,8,9
ValueError: too many values to unpack (expected 3, got 7)
a,b,c=6,7,8
print(a,b,c)
6 7 8
#no space btw two words(use underscore)
first name="bhanu"
SyntaxError: invalid syntax
first_name="bhanu"
print(first_name)
bhanu
firstname="bhanu"
>>> print(firstname)
bhanu
>>> #can only have alphanumberic
>>> fname="bhanu"
>>> lname="ch"
>>> print(fname+lname)
bhanuch
>>> print(fname+" "+lname)
bhanu ch
>>> print(fname,lname)
bhanu ch
>>> a="python"
>>> b="course"
>>> print(a+b)
pythoncourse
>>> print(a,b)
python course
>>> #unpacking and dlt keyword
>>> a,b,c=(6,7,8)
>>> print(a,b,c)
6 7 8
>>> x=10
>>> print(x)
10
>>> del a
>>> del x
>>> print(x)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
>>> #case sensitive
>>> Age=10
>>> print(Age)
10
>>> AGE=20
>>> print(AGE)
20
>>> age=25
>>> print(age)
25
