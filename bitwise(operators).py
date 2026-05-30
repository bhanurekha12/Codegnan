Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #bitwise operators:
>>> a=7
>>> b=3
>>> a&b
3
>>> a=9
>>> b=8
>>> a&b
8
>>> a=2
>>> b=3
>>> a&b
2
>>> bin(2)
'0b10'
>>> bin(3)
'0b11'
>>> #bitwise (|) operator:
>>> a=3
>>> b=8
>>> a|b
11
>>> bin(3)
'0b11'
>>> bin(8)
'0b1000'
>>> #bitwise (~) operator:
>>> a=25
>>> ~a
-26
>>> b=11
>>> ~b
-12
>>> #bitwise (^) operator:
>>> a=5
>>> b=9
>>> a^b
12
>>> bin(5)
'0b101'
bin(9)
'0b1001'

#bitwise (<<) operator:
a=7
a<<3
56
b=2
b<<3
16
#bitwise (>>) operator:
a=7
a>>2
1
b=5
b>>3
0
