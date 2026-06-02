Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#striding:...[a : b : c] represented
#positive striding:
a="data management"
a[::]
'data management'
a[::1]
'data management'
a[::3]
'daage'
a="python course"
a[2:11:3]
'tno'
a[4:9:1]
'on co'
#negavtive striding:
a="deep learning"
a[-1:-4:-2]
'gi'
a[-5:-9:-3]
'rl'
##List[]:
a=[5,3.7,"python",3+7j,True,False]
print(a)
[5, 3.7, 'python', (3+7j), True, False]
type(a)
<class 'list'>
b=7.9
type(b)
<class 'float'>
a=[9.2]
type(a)
<class 'list'>
#list methods():
#append()
a=["python","java","c"]
a.append("ml")
a
['python', 'java', 'c', 'ml']
#extend()
a=["dragon fruit", "mango", "kiwi"]
a.extend(["papaya","pear"])
a
['dragon fruit', 'mango', 'kiwi', 'papaya', 'pear']
#insert()
a=["blue","red","yellow"]
a.insert(0,"black")
a
['black', 'blue', 'red', 'yellow']
#index()
a=["ml","dl","c"]
a.index("dl")
1
#copy()
a=["ml","dl","python"]
b=a.copy()
b
['ml', 'dl', 'python']
#sort()
a=["blue","black","green"]
a.sort()
a
['black', 'blue', 'green']
b=[8,4,0,5,1,7,6]
b.sort()
b
[0, 1, 4, 5, 6, 7, 8]
#reverse()
a=["vijwda","hyd","bnglr"]
a.reverse()
a
['bnglr', 'hyd', 'vijwda']
b=[9,5,3,8,5,1,11]
b.reverse()
b
[11, 1, 5, 8, 3, 5, 9]
#pop()
a={"python","java","ml"]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
#pop()
a=["python","java","ml"]
a.pop()
'ml'
a.pop(1)
'java'
#remove()
a=["python"]
a.remove()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a.remove()
TypeError: list.remove() takes exactly one argument (0 given)
>>> a.remove("python")
>>> a
[]
>>> #length and count(0
>>> a=["hi","hello","bye"]
>>> len(a)
3
>>> b="hello"
>>> len(b)
5
>>> a.count("bye")
1
>>> #clear()
>>> a=["python","java"]
>>> a.clear()
>>> a
[]
>>> ##Tuple():
>>> #len()
>>> a=["a","e","i","o","u"]
>>> len(a)
5
>>> #count()
>>> a.count(True)
0
... 
>>> a.count(False)
0
>>> a.count(True)
0
>>> #index()
>>> a.index("python")
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    a.index("python")
ValueError: list.index(x): x not in list
>>> a=["python"]
>>> a.index("python")
0
