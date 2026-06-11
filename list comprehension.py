#list comprehension:Every list comprehension can be written as a for loop but, for loop cannot be rewritten in list comprehension.
#syntax=[expression for i in range/condition]
'''a=["python","codegnan","course"]
b=str(a)
print(b.upper(),end=" ")'''

'''a=["python","codegnan","course"]
b=[i.upper() for i in  a]
print(b)'''

'''a=["vjwda","hyd","bnglr"]
b=[i.title() for i in a]
print(b)'''

'''a=["PYTHON","FULLSTACK","COURSE"]
b=[i.lower() for i in  a]
print(b)'''

'''a=[2,3,4,5,6,8,12,13]
#b=[i**2 for i in a]
#b=[i*i for i in a]
b=[pow(i,2) for i in a]
print(b)'''

#using range
'''num=int(input("Enter the value"))
range=[d for d in range(num)]
print(range)'''

'''while 1:
    n=int(input("Enter the number:"))
    a=[c for c in range(21) if c%2==0]
    print(a)'''

'''a=[c*c for c in range(21) if c%2==0]
print(a)'''

'''fruits=["apples","banana","dragon","berry","mango"]
#b=[i for i in fruits if "a" not in i]
#b=[i for i in  fruits if "a" in i]
print(b)'''

#no-elif usage in list-comprehension
#if-else :
'''num=int(input("Enter the number:"))
a=[i*i if i%2==0 else i*5 for i in range(num)]
print(a)'''

'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
#add=[a[i]+b[i] for i in range(5)]
add=[a[i]+b[i] for i in range(len(a))]
print(add)'''

#ATM application:
balance=100000
card="c"
password=1234
user_card=input("Enter card:")
if user_card==card:
    print("Welcome Bhanu")
    user_pin=int(input("enter pin:"))
    if user_pin==password:
        print("1.Balance Enqueiry")
        print("2.Withdrawl")
        option=int(input("enter option:"))
        if option==1:
            print("Balance Enqueiry",balance)
        elif option==2:
            amount=int(input("enter amount:"))
            if amount<=balance:
                balance=balance-amount
                print("Withdrawal succesful")
                print("remaining balance=",balance)
            else:
                print("insufficent balance ")
        else:
            print("invalid option")
    else:
        print("Incorrect pin")
else:
    print("Incorrect card")




























