Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#join()
a="hi","guys"
"".join(a)
'higuys'
" ".join(a)
'hi guys'
#formatting():
a=5
b=9
>>> print("the sum is",a+b)
the sum is 14
>>> print("the product is",a*b)
the product is 45
>>> a="vijayawada"
>>> print("the royal city is",a)
the royal city is vijayawada
>>> #concatenation()
>>> a="python"
>>> b="course"
>>> print(a+""+b)
pythoncourse
>>> print(a+" "+b)
python course
>>> fname="bhanu"
>>> lname="ch"
>>> print(fname+" "+lname)
bhanu ch
>>> print(fname.title()+" "+lname.title())
Bhanu Ch
>>> print((fname+" "+lname).title())
Bhanu Ch
>>> #format method
>>> 

>>> 

... 
... 
>>> #format method():(.format)
>>> a="tom"
>>> b="jerry"
>>> print("hello {}{}".format(a,b))
hello tomjerry
>>> print("hello {} {}".format(a,b))
hello tom jerry
>>> print("hello {} hello {}".format(a,b))
hello tom hello jerry
>>> #fstring(formatting string):
>>> a="micky"
>>> b="mouse"
>>> print(f"hello {a}{b}")
hello mickymouse
print(f"hello {a} {b}")
hello micky mouse
print(f"hello {a} hello {b}")
hello micky hello mouse
a=5
b=2
c=a*b
print(f"the sum is {c}")
the sum is 10
#indexing
#1 positive indexing:
a="I am happy for you"
a[5]+a[6]+a[7]+a[8]+a[9]
'happy'
a[11]+a[12]+a[13]
'for'
#2 negative indexing:
a="I am travelling"
a[-10]+a[-9]+a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'travelling'
#slicing:
#1 positive slicing:
a="Codegnan"
a[0:4]
'Code'
a[4:]
'gnan'
#Negative slicing:
a="learning java"
a[-13:-8]
'learn'
a[-4:]
'java'
