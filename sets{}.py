Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets{}:
a={3,4.6,"python",2+5j,True,False}
print(a)
{False, True, (2+5j), 3, 4.6, 'python'}
b={2,3,4,5,3,4,5}
print(b)
{2, 3, 4, 5}
#add():
a={5,6,7,8,9}
a.add(10)
a
{5, 6, 7, 8, 9, 10}
#issubset():Is  part of main part
a={1,2,3,4,5,6,7,8}
b={5,6,7,8}
b.issubset(a)
True
a.issubset(b)
False
#issuperset():
a={2,4,6,8,10}
b={2,4,6}
a.issuperset(b)
True
b.issuperset(a)
False
#union:
a={1,2,3,4,5,6,7}
b={5,6,7,8,9,10}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#intersection()
a={11,12,13,14,15,16,17}
b={15,16,17,18}
a.intersection(b)
{16, 17, 15}
b.intersection(a)
{16, 17, 15}
#update():union and update are same but in update:the recently updated value would be prnted when we call the variable
a={1,2,3,4,5,6}
b={5,6,7,8,9,10}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
c={2,4,6,8,10}
d={6,8,10,12,13}
c.update(d)
c
{2, 4, 6, 8, 10, 12, 13}
d
{6, 8, 10, 12, 13}
d.update(c)
d
{2, 4, 6, 8, 10, 12, 13}
#difference()
a={2,3,4,5,6}
b={1,2,3,7,8,9}
a.difference(b)
{4, 5, 6}
b.difference(a)
{8, 1, 9, 7}
#symmetric_difference()
a={1,2,3,4,5,6}
b={5,6,7,8}
a.symmetric_difference(b)
{1, 2, 3, 4, 7, 8}
b.symmetric_difference(a)
{1, 2, 3, 4, 7, 8}
# in symmetric_difference: it would print diff values by merging the sets
##differnce_update():it would print diff value by comparing both the sets..and the prntd value would be condsidered when we call for 2nd diff_upadte
a={2,3,4,5,6}
b={5,6,7,8,9}
a.difference_update(b)
a
{2, 3, 4}
a
{2, 3, 4}
b
{5, 6, 7, 8, 9}
b.difference_update(a)
b
{5, 6, 7, 8, 9}
#bcse it would consder outp of a and b

#intersection_update(): prnt common values
a={5,6,7,8,9,10}
b={2,3,4,5,6,7}
a.intersection_update(b)
a
{5, 6, 7}
a
{5, 6, 7}
b
{2, 3, 4, 5, 6, 7}
b.intersection_update(a)
b
{5, 6, 7}
a
{5, 6, 7}
b
{5, 6, 7}
#symmetric_difference_update()
#removing the same values and merging
a={2,3,4,5,6,7}
b={1,6,7,8,9,10}
a.symmetric_difference_update(b)
a
{1, 2, 3, 4, 5, 8, 9, 10}
b.symmetric_difference_update(a)
b
{2, 3, 4, 5, 6, 7}
#copy() and clear()
a={2,3,4,5,6}
a.copy()
{2, 3, 4, 5, 6}
#clear()
a={7,8,9,10,11}
a.clear()
a
set()
#add
>>> a=set()
>>> a.add(11)
>>> a
{11}
>>> #pop():you can pop only first number in set(). if you want to rmove particular number then we need to use remove().
>>> a={12,13,14}
>>> a.pop()
12
>>> a.remove(13)
>>> a
{14}
>>> #discard and remove are same
>>> a={2,3,4,5,6}
>>> a.discard(4)
>>> a
{2, 3, 5, 6}
>>> #set{} consists of only length , count and index would reflect as error because set{} would be in order .
>>> a={2,1,3,4,5}
>>> len(a)
5
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    a.count()
AttributeError: 'set' object has no attribute 'count'
>>> a.index(2)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    a.index(2)
AttributeError: 'set' object has no attribute 'index'
>>> #disjoint(): no number should be same
>>> a={1,2,3,4,5}
>>> b={4,5,6,7,8}
>>> a.isdisjoint(b)
False
>>> a.isdisjoint(b)
False
>>> a={1,2,3,4}
>>> b={5,6,7,8}
>>> a.isdisjoint(b)
True
