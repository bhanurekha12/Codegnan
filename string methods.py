Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string method:
#length()
a="bhanu"
len(a)
5
b="python"
len(b)
6
#count()
a="hey you"
a.count("you")
1
a="twinkle twinkle little star"
a.count("twinkle")
2
a.count("t")
5
#find a string
a="python"
a.find("t")
2
a.find("n")
5
a="chittibomma"
a.find("k")
-1
#escape sequence
a="name\nmailid:bhanuchittibomma@gmail.com\tmobilenumber:
SyntaxError: unterminated string literal (detected at line 1)
a="name\nmailid:bhanuchittibomma@gmail.com\tmobilenumber:"
print(a)
name
mailid:bhanuchittibomma@gmail.com	mobilenumber:
#replace
    
a="helloooo"
a.replace("l","u")
'heuuoooo'
b="work work until you goo"
b.replace("work","wait")
'wait wait until you goo'
b.replace("work","wait",1)
'wait work until you goo'
#uppercase
a="bhanu"
a.uppercase()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a.uppercase()
AttributeError: 'str' object has no attribute 'uppercase'
a="bhanu"
a.upper()
'BHANU'
#lower()
b="python"
b.upper()
'PYTHON'
#lower()
b="HEY"
b.lower(0)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    b.lower(0)
TypeError: str.lower() takes no arguments (1 given)
b.lower()
'hey'
#capitalize()
a="hello"
a.capitalize()
'Hello'
#title()
a="i am happy"
a.title()
'I Am Happy'
##conditions##
a="hello"
a.isupper()
False
a.islower()
True
a.isdigit()
False
>>> a.isalnum()
True
>>> a.isalpha()
True
>>> b="hello everyone"
>>> a.isalpha()
True
>>> b="hellooall"
>>> b.isalpha()
True
>>> #alphanumeric:
>>> n="bhanu123"
>>> n.isalnum()
True
>>> n="bhanu@123"
>>> n.isalnum()
False
>>> #startswith,endswith:
>>> c="hello"
>>> c.startswith("h")
True
>>> c.startswith("f")
False
>>> #string(),lstrip(),rstrip():
>>> a="        heyy           "
>>> a.strip()
'heyy'
>>> a.lstrip()
'heyy           '
>>> a.rstrip()
'        heyy'
>>> #split()
>>> a="python java c c++"
>>> a.split()
['python', 'java', 'c', 'c++']
>>> b="pythonjava"
>>> b.split()
['pythonjava']
>>> c="you   i"
>>> c.split()
['you', 'i']
