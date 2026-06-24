#Generators:No tuple comprehension in above cases if we remove those braces and keep paranthesis then the outcome is generator.

#same as list comprehension but we need to use paranthesis.
'''a=(i for i in range(20))
print(a)                    #o/p:<generator object <genexpr> at 0x0000012F8DE08E10>
print(type(a))'''               #o/p: class generator


a=(i for i in range(20))
print(a)
# print(list(a))
#print(tuple(a))
#  print(set(a))

#generator is also a function which can be used as an iterator (loop) by producing group of values,where we use yield keyword.
#yield vs return:return will terminate the function where as yield can pass the function and go on with every successive iteration.

#yield:(pass)
'''a,b=[int(x) for x in input("enter values").split(",")]
def data(a,b):
    while a<b:
        #yield a
        a=a+3
        yield a
print(*data(a,b))'''

#return:(terminate)
'''a,b=[int(x) for x in input("enter values").split(",")]
def data(a,b):
    while a<b:
        a=a+3
        return a
print(data(a,b))'''

#yield vs return:
'''def mygen():
    #return "python"
    #return "java"
    #return "sql"
    return "python","java","sql"
print(*mygen())'''                         #o/p:python java sql


'''def mygen():
    yield "vja"
    yield "hyd"
    yield "bglr"
print(*mygen())'''                 #o/p:vja hyd bglr


#next()
'''d=mygen()
print(next(d))          #o/p:vja
print(next(d))          #o/p:hyd
print(next(d))'''          #o/p:bglr


























