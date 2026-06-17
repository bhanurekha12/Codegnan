#keywords and positional arguments:
#argument1
'''def Details(id,name,mailid):
    id=26
    name="bhanu"
    mailis="bhanu@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''

'''def Details(id,name,mailid):
    print(id,name,mailid)
#step2
Details(id="id",name="name",mailid="mailid")
Details(id="26",name="bhanu",mailid="bhanuchittibomma@gmail.com")
Details(id="66",name="buddi",mailid="b@gmail.com")
Details("d@gmail.com","Deeksha",40)#should be entered in order if not it would be printed same as given.
Details(mailid="Deeksha@gmail.com",name="deeksha",id=40)# when given randomly with key words then it would print in order.'''

#Swapping
'''a=10
b=20
a,b=b,a
print(a)
print(b)'''

'''a=20
b=10
temp=a
a=b
b=temp
print(a)
print(b)'''

'''a=12
b=22
a=a+b
b=a-b
a=a-b
print("a value is",a)
print("b value is",b)'''

'''a=22
b=44
a=a+b
b=a-b
a=a-b
print("After swapping a=%d,b=%d" %(a,b))'''

#Argument 2:
'''def Grocery(item,price):
    print("item is %s" %item)
    print("price is %d" %price)
Grocery("Sugar",100)'''

'''def Grocery(item="Rice",price=1300):
    print("item is %s" %item)
    print("price is %d" %price)
Grocery()'''

'''def Grocery(item="Salt",price):
    print("item is %s" %item)
    print("price is %d" %price)
Grocery(50)'''#non-default argument follows the default argument.

'''def Grocery(item,price=80):
    print("item is %s" %item)
    print("price is %d" %price)
Grocery("Ghee")'''

#task
'''def bakery(cake,price,quantity):
    print("cake is %s" %cake)
    print("price is %d" %price)
    print("quantity is %d" %quantity)
bakery("chocolate",1200,1)'''

# * arugument:* is used to unpack the elements.

'''a=[2,3,4,5,6,7]
print(a)
print(type(a))
print(*a) '''# o/p:2,3,4,5,6,7

'''a=(1,3,5,7,9)
print(a)
print(type(a))
print(*a)'''      #o/p:1,3,5,7,9

'''a={0,2,4,6,8,10}
print(a)
print(type(a))
print(*a) '''         #o/p:0,2,4,6,8,10

'''a={"name":"bhanu", "year":2026,  "month":"June"}
print(a)
print(type(a))
print(*a) '''  #only key values will be printed

'''a="codegnan"
print(a)
print(*a)'''      #c o d e g n a n


'''a,b,c=1,2,3,4,5,6,7,8
print(a)
print(b)
print(c) '''    #error becasue when 3 variables are given  only 3 values should be passed.

          

'''a,b,c=3,6,9
print(a)
print(b)
print(c)'''      #o/p: 3 6 9

'''a,b,c="codegnan"
print(a)
print(b)
print(c)'''     #error bcse too many varibales passed

'''a,b,c="cod"
print(a)           
print(b)
print(c)'''     #c o d


'''*a,b,c=5,10,15,20,25,30    #o/p: 5,10,15,20
print(*a)                     #    25
print(b)                       #   30
print(c)'''


'''a,*b,c=1,2,3,4,5,6,7,8        #o/p: 1
print(a)                           #  2,3,4,5,6,7
print(*b)                           #  8
print(c)'''


'''a,b,*c="bhanu"              o/p: b
print(a)                            h
print(b)                           a n u
print(*c)'''

#variable length arguments: Automatically stores in tuple , and we use star arguments.

'''def check(*a):                   # o/p: ()
    print(a)
    print(type(a))               #    <class tuple>
check()
check(1,2,3,4,5)

b=[3,4,5,6,7]                    #(3,4,5,6,7)
check(*b)

c=(1,2,3)                       #(1,2,3)
check(*c)

d={2,4,6,8}                       #(2,4,6,8)
check(*d)

e={"year":2026,"month":"june","date":17}        #only keyvalues would be printed in tuple   o/p:(year,month,date)
check(*e)'''


'''def check1(*a):
    d=1 #creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()
check1(1,2,3,4,5)
check1(2,3.2,1.8,3,9)
check1(1,2,4,6,2.8,4,1,"bhanu")   
check1(1,2.8,"bhanu",3+1j)'''  #ouput would be printed till int and float and doesn't consider anyother types.


#task:  Railway Ticket
'''while True:
    def railway_ticket():
        ticket=1000
        gender=input("enter gender")
        age=int(input("enter age:"))
        if gender=="m":
            if age>=60:
                print("senior citizen")
                ticket=ticket-30/100*ticket
                print(ticket)
            elif age<60:
                print("normal citizen")
                print(ticket)
        elif gender =="f":
            if age>=60:
                print("senior citizen")
                ticket=ticket-50/100*ticket
                print(ticket)
            elif age<60:
                print("normal citizen")
                print(ticket)
    railway_ticket()'''








































