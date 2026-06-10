  #loops:
##for,while,range,break,continues,pass
'''a=[10,20,30,40,50]
for i in a:
    print(i)'''

'''a=[10,20,30,40,50]
for i in a:
    print(i,end=" ")'''

'''a=[10,20,30,40,50]
for i in a:
    print(a)'''

'''a=[10,20,30,40,50]
for i in a:
    print(i)
    print(type(a))'''

'''a=[10,20,30,40,50]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a=(1,2,3,4,5,6)
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a={10,20,30,40,50}
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a={"name":"bhanu","age":21,"date":9}
for i in a:
    print(i)
    print(type(a))
    print(type(i))
for i in a.keys():
    print(i)
for i in a.values():
    print(i)
for i in a.items():
    print(i)
    print(type(a))
    print(type(i))'''

'''a=[4,2.9,"python",4+8j,True,False]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a="codegnan"
for i in a:
    print(i)
    print(type(i))
    print(type(a))'''

'''fruits=["apple","mango","dragonfruit"]
for i in fruits:
    print(i, end=" ")'''

#a=["codegnan","python","course"]
#op:{"CODEGNAN","PYTHON","COURSE"]

'''a=["codegnan","python","course"]
b=str(a)
print(b.upper())'''


'''a=["codegnan","python","course"]
for i in a:
    print(i.upper(),end=" ")'''

'''a=["codegnan","python","course"]
b=[]
for i in a:
    b.append(i.upper())'''

##while loop:
'''a=10
while a>1:
    print(a)'''


'''a=10
while a>=1:
    print(a)
    a=a-1'''

'''a=20
while a>5:
    print(a)
    a=a-1'''

'''a=10
while a>=1:
    a=a-1
    print(a)'''


'''a=20
while a>6:
    print(a)
    a+=1'''

'''a=20
while a>6:
    print(a)
    a-=1'''

'''while True:
    age= int(input("enter age:"))
    if age>=18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")'''

'''while 1:
    n = int(input("enter value:"))
    if n % 2==0:
              print("Even number")
    else:
        print("odd number")'''

##Range: The range function returns a sequence of numbers, starting from 0 by default and increments one by one and stops before a specified number.
#start-stop-step:
'''for i in range(10):
    print(i)'''

'''for i in range(1,101):
    print(i)'''

'''for i in range(0,28,3):
    print(i)'''

'''for i in range(2,19,2):
    print(i)'''

'''for i in range(5,46,5):
    print(i)'''

#task:
'''marks=int(input("enter marks:"))
if marks in range(91,101):
    print("Grade-A")
elif marks in range(81,91):
    print("GRADE-B")
elif marks in range(71,81):
    print("GRADE-C")
elif marks in range(50,71):
    print("GRADE-D")
else:
    print("Fail")'''


##Break:The break statement is used to terminate the entire loop.
#Continue :The continue statemnt skips the current iteration and rest of the code will continue.
#Pass:The pass statemnt is a null statemnet it does nothing, but syntatically we need.


#break
''''a=10
while a>1:
    print(a)
    a=a-1
    if a==7:
        break'''

'''a=20
while a>5:
    a=a-1
    if a==10:
        break
print(a)'''


'''a=20
while a>5:
    a=a-1
    print(a)'''


'''a=20
while a>5:
    print(a)
    a=a-1
    if a==8:
        break'''
    

'''for i in range(20):
    if i==13:
        break
    print(i)'''

    
'''a="python"
for i in a:
    if i=="h":
        break
    print(i)'''

##continue:
'''a=30
while a>10:
    a=a-1
    if a==19:
        continue
    print(a)'''


'''a=40
while a>15:
    a=a-1
    if a==25:
        continue
    print(a)'''


'''a=30
while a>10:
    a=a-1
    if a==19:
        continue
print(a)'''


'''for i in range(25):
    if i==17:
        continue
    print(i)'''

'''a="python"
for i in a:
    if i=="y":
        continue
    print(i)'''

##pass:
'''a=15
while a>10:
    print(a)
    a=a-1
    if a==14:
        pass'''


'''for i in range(20):
    if i==15:
        pass
    print(i)'''


#task;
'''a=30
while a>12:
    a=a-1
    if a==20:
        continue
    if a==18:
        break
    print(a)'''


#Student attendence report:

'''students=int(input("enter number of students:"))
p=0
a=0
for i in range(1,students+1):
    b=input(f"students attendence {i} p or a")
    if b=="p":
        p+=1
    elif b=="a":
        a+=1
print("Attendence report....")
print("total stdudents",students)
print("total presenties",p)
print("total absenties",a)'''








































