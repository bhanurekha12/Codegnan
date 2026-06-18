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


#kwargs(**):

'''def Details(**a):
    print(a)
    print(type(a))
Details()                  #{}  class dict
d={"idno":[20,40,60],
   "names":["Bhanu","Rekha","Deeksha"],
   "status":["p","a","p"]}
Details(**d)'''

'''def Details(**a):
    print(a)
    print(type(a))
    for i in  a:          #idnos names status
        print(i)         
    for i in a:           #[20,40,60]  ["bhanu","rekha","deeksha"]  [p ,a, p]
        print(a[i])
    for i in a:
        print(a,a[i])
    for i in a.keys():       #dictionary methods
        print(i)
    for i in a.values():      #dictionary methods
        print(i)
    for i in a.items():          #dictionary methods
        print(i)
Details()
d={"idno":[20,40,60],
   "names":["Bhanu","Rekha","Deeksha"],
   "status":["p","a","p"]}
Details(**d)'''

#* and ** usage task:
'''def final(*a,**b):
    print(a)
    print(b)
    d=2
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("Keys are",i)
        print("Values are",j)
final()
d=(2,6,7,9.1,3.4)
final(*d)
e={"idno":[20,40,60],
   "names":["Bhanu","Rekha","Deeksha"],
   "status":["p","a","p"]}
final(**e)
final(*d,**e)'''


#max(),min(),sum()

'''print(max(3,1,5,8,12,19,45))


print(min(0,45,12,37,82,66))

a=2,3,4,5,6,7,8
print(sum(a))'''

#Marks analysis report:

'''students=int(input("enter number of students"))
marks=[]
for i in range(1,students+1):
    mark=int(input(f"enter student {i} marks"))
    b=marks.append(mark)
for i in marks:
    print(i)
print("Marks Analysis Report")
print("total students",students)
print("highest marks",max(marks))
print("lowest marks",min(marks))
print("total marks",sum(marks))
print("average is",sum(marks)/students)'''









