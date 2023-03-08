# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # with open("abhi.txt",'w') as files:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 	files.write("hello abhi")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # import math
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(math.factorial(5))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # n=10
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # for i in range(n):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  print(i,end=" ")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # g=lambda x:x*x
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(g(2))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # from math import factorial
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(factorial(5))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # i="Abhishek"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # if "f" in i:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 	print("true")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 	print("false")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a=4
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # b=4
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # try:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 	k=a//b
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 	print(int(k))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # except ZeroDivisionError :
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 	print("cant divide by zero ")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # finally:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 	print("problem solved")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print ("The value of a / b is : ")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # assert b != 0, "Divide by 0 error"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print (a / b)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # a=22
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # b='Abhishek'
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(b)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # del a
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # del b
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # a="nachi"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # b="18"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(b)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # a=10
# # # # # # # # # # # # # # # # # # # # # # # # # # # # b=20
# # # # # # # # # # # # # # # # # # # # # # # # # # # # def add():
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 	c=a+b
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 	print(c)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # add()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # def fun():
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 	var=150
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 	def gun():
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 		nonlocal var
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 		var=var+50
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 		print(var)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 	gun()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # fun()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # a,b,c=1,3,5
# # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a+b+c)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # g = input("Enter your name : ")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # print(g)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # a, b, c, d = input("enter 2 value:").split()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # print(b)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # print(c)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # print(d)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # taking multiple inputs at a time
# # # # # # # # # # # # # # # # # # # # # # # # # # # # and type casting using list() function
# # # # # # # # # # # # # # # # # # # # # # # # # # # # x = list(input("Enter multiple values: ").split())
# # # # # # # # # # # # # # # # # # # # # # # # # # # # print("List of students: ",x)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # x = set(input("Enter multiple values: ").split())
# # # # # # # # # # # # # # # # # # # # # # # # # # # # print("List of students: ",x)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # x,y=[int(x) for x in input("enter 2 values:").split()]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # print(x,y)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # x=10
# # # # # # # # # # # # # # # # # # # # # # # # # # # # y=20
# # # # # # # # # # # # # # # # # # # # # # # # # # # # print("value of x is {} and value of y is {}".format(y,x))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # x=set(int(x) for x in input("ENter multiple value:").split(','))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # print(x)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # import time
# # # # # # # # # # # # # # # # # # # # # # # # # # # # count_down=5
# # # # # # # # # # # # # # # # # # # # # # # # # # # # for i in reversed(range(count_down+1)):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 	if i>0:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 		print(i,end=">>>",flush='true')
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 		time.sleep(1)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 	else:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 		print("start")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # x=20
# # # # # # # # # # # # # # # # # # # # # # # # # # # # y=2
# # # # # # # # # # # # # # # # # # # # # # # # # # # # z=2023
# # # # # # # # # # # # # # # # # # # # # # # # # # # # print(x,y,z,sep='-')
# # # # # # # # # # # # # # # # # # # # # # # # # # # # import io

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # declare a dummy file
# # # # # # # # # # # # # # # # # # # # # # # # # # # # dummy_file = io.StringIO()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # add message to the dummy file
# # # # # # # # # # # # # # # # # # # # # # # # # # # # print('Hello Geeks!!', file=dummy_file)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # get the value from dummy file
# # # # # # # # # # # # # # # # # # # # # # # # # # # # dummy_file.getvalue()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # import io
# # # # # # # # # # # # # # # # # # # # # # # # # # # # dummy_file = io.StringIO()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # print('Abhishek ', file=dummy_file)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # dummy_file.getvalue()

# # # # # # # # # # # # # # # # # # # # # # # # # # # print("Hello Abhishek You are learnig Python",file=open('abi.html','w'))

# # # # # # # # # # # # # # # # # # # # # # # # # # a=[1,2,3,4]
# # # # # # # # # # # # # # # # # # # # # # # # # # for i in range(4):
# # # # # # # # # # # # # # # # # # # # # # # # # # 	print(a[i],end=" ")

# # # # # # # # # # # # # # # # # # # # # # # # # # a=[1,3,5,7,9]
# # # # # # # # # # # # # # # # # # # # # # # # # # b=[2,4,5,6,8,8]
# # # # # # # # # # # # # # # # # # # # # # # # # # print(set( a + b))
# # # # # # # # # # # # # # # # # # # # # # # # # #import the below module and see what happens
# # # # # # # # # # # # # # # # # # # # # # # # # # import antigravity
# # # # # # # # # # # # # # # # # # # # # # # # # #NOTE - it wont work on online ide

# # # # # # # # # # # # # # # # # # # # # # # # # # abhi="Abhishek"
# # # # # # # # # # # # # # # # # # # # # # # # # # print(abhi.center(20,'-'))

# # # # # # # # # # # # # # # # # # # # # # # # # # a=True
# # # # # # # # # # # # # # # # # # # # # # # # # # b=False
# # # # # # # # # # # # # # # # # # # # # # # # # # print(a and b)

# # # # # # # # # # # # # # # # # # # # # # # # # # a=10
# # # # # # # # # # # # # # # # # # # # # # # # # # b=4
# # # # # # # # # # # # # # # # # # # # # # # # # # print(a & b)
# # # # # # # # # # # # # # # # # # # # # # # # # # print(a | b)
# # # # # # # # # # # # # # # # # # # # # # # # # # print(~a)
# # # # # # # # # # # # # # # # # # # # # # # # # # print(a^b)
# # # # # # # # # # # # # # # # # # # # # # # # # # print(a>>2)
# # # # # # # # # # # # # # # # # # # # # # # # # # print(a<<2)

# # # # # # # # # # # # # # # # # # # # # # # # # # x=24
# # # # # # # # # # # # # # # # # # # # # # # # # # y=20
# # # # # # # # # # # # # # # # # # # # # # # # # # list=[10,20,30,40,50]
# # # # # # # # # # # # # # # # # # # # # # # # # # if(x not in list):
# # # # # # # # # # # # # # # # # # # # # # # # # # 	print("X not present")
# # # # # # # # # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # # # # # # # # # 	print("x is present")

# # # # # # # # # # # # # # # # # # # # # # # # # # a=1+20*10
# # # # # # # # # # # # # # # # # # # # # # # # # # print(a)

# # # # # # # # # # # # # # # # # # # # # # # # # # a=140
# # # # # # # # # # # # # # # # # # # # # # # # # # b=20
# # # # # # # # # # # # # # # # # # # # # # # # # # min=a if a<b else b
# # # # # # # # # # # # # # # # # # # # # # # # # # print(min)

# # # # # # # # # # # # # # # # # # # # # # # # # # a = 10
# # # # # # # # # # # # # # # # # # # # # # # # # # b = 20
# # # # # # # # # # # # # # # # # # # # # # # # # # # print((b,a) [a>b])
# # # # # # # # # # # # # # # # # # # # # # # # # # print({True: a, False: b}[a < b])
# # # # # # # # # # # # # # # # # # # # # # # # # # Python Program illustrate how
# # # # # # # # # # # # # # # # # # # # # # # # # # to overload an binary + operator
# # # # # # # # # # # # # # # # # # # # # # # # # # And how it actually works

# # # # # # # # # # # # # # # # # # # # # # # # # # class Ab:

# # # # # # # # # # # # # # # # # # # # # # # # # # 	def __init__(self, a):
# # # # # # # # # # # # # # # # # # # # # # # # # # 		self.a = a

# # # # # # # # # # # # # # # # # # # # # # # # # 	# adding two objects
# # # # # # # # # # # # # # # # # # # # # # # # # # 	def __add__(self, o):
# # # # # # # # # # # # # # # # # # # # # # # # # # 		return self.a + o.a

# # # # # # # # # # # # # # # # # # # # # # # # # # ob1 = Ab("1")
# # # # # # # # # # # # # # # # # # # # # # # # # # ob2 = Ab("2")
# # # # # # # # # # # # # # # # # # # # # # # # # # ob3 = Ab("Geeks")
# # # # # # # # # # # # # # # # # # # # # # # # # # ob4 = Ab("For")

# # # # # # # # # # # # # # # # # # # # # # # # # # print(ob1 + ob2)
# # # # # # # # # # # # # # # # # # # # # # # # # # print(ob3 + ob4)
# # # # # # # # # # # # # # # # # # # # # # # # # # print(Ab.__add__(ob1, ob4))
# # # # # # # # # # # # # # # # # # # # # # # # # # print(ob1.__add__(ob2))
# # # # # # # # # # # # # # # # # # # # # # # # # # Actual working when Binary Operator is used.
# # # # # # # # # # # # # # # # # # # # # # # # # # print(A.__add__(ob1 , ob2))
# # # # # # # # # # # # # # # # # # # # # # # # # # print(A.__add__(ob3,ob4))
# # # # # # # # # # # # # # # # # # # # # # # # # # #And can also be Understand as :
# # # # # # # # # # # # # # # # # # # # # # # # # # print(ob1.__add__(ob2))
# # # # # # # # # # # # # # # # # # # # # # # # # # print(ob3.__add__(ob4))

# # # # # # # # # # # # # # # # # # # # # # # # # # class Ab:
# # # # # # # # # # # # # # # # # # # # # # # # # # 	def __init__(self,a,b):
# # # # # # # # # # # # # # # # # # # # # # # # # # 		self.a=a
# # # # # # # # # # # # # # # # # # # # # # # # # # 		self.b=b
# # # # # # # # # # # # # # # # # # # # # # # # # # 	def __add__(self,other):
# # # # # # # # # # # # # # # # # # # # # # # # # # 		return self.a + other.a, self.b + other.b

# # # # # # # # # # # # # # # # # # # # # # # # # # ob1=Ab(1,2)
# # # # # # # # # # # # # # # # # # # # # # # # # # ob2=Ab(2,7)

# # # # # # # # # # # # # # # # # # # # # # # # # # print(Ab.__add__(ob1,ob2))

# # # # # # # # # # # # # # # # # # # # # # # # # # Python program to overload
# # # # # # # # # # # # # # # # # # # # # # # # # # a comparison operators

# # # # # # # # # # # # # # # # # # # # # # # # # # class A:
# # # # # # # # # # # # # # # # # # # # # # # # # # 	def __init__(self,a):
# # # # # # # # # # # # # # # # # # # # # # # # # # 		self.a=a
# # # # # # # # # # # # # # # # # # # # # # # # # # 		def __chk__(self,other):
# # # # # # # # # # # # # # # # # # # # # # # # # # 			if(self.a > other.a):
# # # # # # # # # # # # # # # # # # # # # # # # # # 				return True
# # # # # # # # # # # # # # # # # # # # # # # # # # 			else:
# # # # # # # # # # # # # # # # # # # # # # # # # # 				return

# # # # # # # # # # # # # # # # # # # # # # # # # # ob1=A(2)
# # # # # # # # # # # # # # # # # # # # # # # # # # ob2=A(3)
# # # # # # # # # # # # # # # # # # # # # # # # # # if (ob1>ob2):
# # # # # # # # # # # # # # # # # # # # # # # # # # 	print("Ob1 is greater")
# # # # # # # # # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # # # # # # # # # 	print("Ob2 is greater")

# # # # # # # # # # # # # # # # # # # # # # # # # # a=[1,2,3,4,5,6]
# # # # # # # # # # # # # # # # # # # # # # # # # # b=reversed(a)
# # # # # # # # # # # # # # # # # # # # # # # # # # print(b)

# # # # # # # # # # # # # # # # # # # # # # # # # # a=(1,2,3,4,5,6,7,8,9)
# # # # # # # # # # # # # # # # # # # # # # # # # # rev=a[::-1]
# # # # # # # # # # # # # # # # # # # # # # # # # # print(rev)

# # # # # # # # # # # # # # # # # # # # # # # # # # class A:
# # # # # # # # # # # # # # # # # # # # # # # # # # 	def __init__(self,a):
# # # # # # # # # # # # # # # # # # # # # # # # # # 		self.a=a

# # # # # # # # # # # # # # # # # # # # # # # # # # 	def __invert__(self):
# # # # # # # # # # # # # # # # # # # # # # # # # # 		return "This is Operator"

# # # # # # # # # # # # # # # # # # # # # # # # # # ob1=A(2)

# # # # # # # # # # # # # # # # # # # # # # # # # # print(~ob1)

# # # # # # # # # # # # # # # # # # # # # # # # # # print(any([True,True,True]))
# # # # # # # # # # # # # # # # # # # # # # # # # # print(any([True,False,True]))
# # # # # # # # # # # # # # # # # # # # # # # # # # print(any([False,False,True]))
# # # # # # # # # # # # # # # # # # # # # # # # # # print("\n")
# # # # # # # # # # # # # # # # # # # # # # # # # # print(all([True,True,True]))
# # # # # # # # # # # # # # # # # # # # # # # # # # print(all([True,False,True]))
# # # # # # # # # # # # # # # # # # # # # # # # # # print(all([False,False,True]))

# # # # # # # # # # # # # # # # # # # # # # # # # # list1=[]
# # # # # # # # # # # # # # # # # # # # # # # # # # list2=[]
# # # # # # # # # # # # # # # # # # # # # # # # # # for i in range(1,11):
# # # # # # # # # # # # # # # # # # # # # # # # # # 	list1.append(4*i)
# # # # # # # # # # # # # # # # # # # # # # # # # # 	list2.append(5*i)

# # # # # # # # # # # # # # # # # # # # # # # # # # print(list1)
# # # # # # # # # # # # # # # # # # # # # # # # # # print(list2)

# # # # # # # # # # # # # # # # # # # # # # # # # # list1=[]
# # # # # # # # # # # # # # # # # # # # # # # # # # list2=[]

# # # # # # # # # # # # # # # # # # # # # # # # # # for i in range(1,11):
# # # # # # # # # # # # # # # # # # # # # # # # # # 	list1.append(3*i)

# # # # # # # # # # # # # # # # # # # # # # # # # # for i in range(0,10):
# # # # # # # # # # # # # # # # # # # # # # # # # # 	list2.append(list1[i]%5==0)

# # # # # # # # # # # # # # # # # # # # # # # # # # print(list1)
# # # # # # # # # # # # # # # # # # # # # # # # # # print(all(list2))

# # # # # # # # # # # # # # # # # # # # # # # # # # import operator
# # # # # # # # # # # # # # # # # # # # # # # # # # a=10
# # # # # # # # # # # # # # # # # # # # # # # # # # b=10
# # # # # # # # # # # # # # # # # # # # # # # # # # print(operator.ne(a,b))

# # # # # # # # # # # # # # # # # # # # # # # # # # import operator
# # # # # # # # # # # # # # # # # # # # # # # # # # li=[1,2,4,7,9,3,10]

# # # # # # # # # # # # # # # # # # # # # # # # # # for i in range(0,len(li)):
# # # # # # # # # # # # # # # # # # # # # # # # # # 	print(li[i],end=",")

# # # # # # # # # # # # # # # # # # # # # # # # # # operator.delitem(li,3)
# # # # # # # # # # # # # # # # # # # # # # # # # # print('\n')
# # # # # # # # # # # # # # # # # # # # # # # # # # for i in range (0,len(li)):
# # # # # # # # # # # # # # # # # # # # # # # # # # 		print(li[i],end=",")

# # # # # # # # # # # # # # # # # # # # # # # # # # import operator
# # # # # # # # # # # # # # # # # # # # # # # # # # list=[1,2,3,4,9,8,7,6,5]

# # # # # # # # # # # # # # # # # # # # # # # # # # for i in range(0,len(list)):
# # # # # # # # # # # # # # # # # # # # # # # # # # 	print(list[i],end=",")
# # # # # # # # # # # # # # # # # # # # # # # # # # print('\n')
# # # # # # # # # # # # # # # # # # # # # # # # # # print('4th item in the list is :',end=' ')
# # # # # # # # # # # # # # # # # # # # # # # # # # print(operator.setitem(list,4,98))

# # # # # # # # # # # # # # # # # # # # # # # # # # for i in range(0,len(list)):
# # # # # # # # # # # # # # # # # # # # # # # # # # 	print(list[i],end=",")
# # # # # # # # # # # # # # # # # # # # # # # # # # print('\n')
# # # # # # # # # # # # # # # # # # # # # # # # # # operator.delitem(list,1)

# # # # # # # # # # # # # # # # # # # # # # # # # # for i in range(0,len(list)):
# # # # # # # # # # # # # # # # # # # # # # # # # # 	print(list[i],end=",")

# # # # # # # # # # # # # # # # # # # # # # # # # # import operator
# # # # # # # # # # # # # # # # # # # # # # # # # # a="abhi"
# # # # # # # # # # # # # # # # # # # # # # # # # # b="shek"
# # # # # # # # # # # # # # # # # # # # # # # # # # c=operator.concat(a,b)
# # # # # # # # # # # # # # # # # # # # # # # # # # d=c.upper()
# # # # # # # # # # # # # # # # # # # # # # # # # # print(d)

# # # # # # # # # # # # # # # # # # # # # # # # # # a=10
# # # # # # # # # # # # # # # # # # # # # # # # # # print(a+a)
# # # # # # # # # # # # # # # # # # # # # # # # # # a=20
# # # # # # # # # # # # # # # # # # # # # # # # # # print(a)

# # # # # # # # # # # # # # # # # # # # # # # # # # a='''Hifd'''
# # # # # # # # # # # # # # # # # # # # # # # # # # print(a)

# # # # # # # # # # # # # # # # # # # # # # # # # # import operator
# # # # # # # # # # # # # # # # # # # # # # # # # # L = [1, "a" , "string" , 1+2]
# # # # # # # # # # # # # # # # # # # # # # # # # # print(L)
# # # # # # # # # # # # # # # # # # # # # # # # # # operator.setitem(L,3,10)
# # # # # # # # # # # # # # # # # # # # # # # # # # print(L)
# # # # # # # # # # # # # # # # # # # # # # # # # # L.pop()
# # # # # # # # # # # # # # # # # # # # # # # # # # print(L)
# # # # # # # # # # # # # # # # # # # # # # # # # # L.pop()
# # # # # # # # # # # # # # # # # # # # # # # # # # print(L)
# # # # # # # # # # # # # # # # # # # # # # # # # # L.pop()
# # # # # # # # # # # # # # # # # # # # # # # # # # print(L)

# # # # # # # # # # # # # # # # # # # # # # # # # # list=(1,2,3,"abhi",1+10)
# # # # # # # # # # # # # # # # # # # # # # # # # # for i in range(0,len(list)-2):
# # # # # # # # # # # # # # # # # # # # # # # # # # 	print(list[i],end=" ")

# # # # # # # # # # # # # # # # # # # # # # # # # # i=0
# # # # # # # # # # # # # # # # # # # # # # # # # # while(i<=10):
# # # # # # # # # # # # # # # # # # # # # # # # # # 	print((i*2)+1,end=" ")
# # # # # # # # # # # # # # # # # # # # # # # # # # 	i+=1
# # # # # # # # # # # # # # # # # # # # # # # # # # a="abhi"
# # # # # # # # # # # # # # # # # # # # # # # # # # print(a[-2])

# # # # # # # # # # # # # # # # # # # # # # # # # # def reversed(s):
# # # # # # # # # # # # # # # # # # # # # # # # # # 	str=""
# # # # # # # # # # # # # # # # # # # # # # # # # # 	for i in s:
# # # # # # # # # # # # # # # # # # # # # # # # # # 		str=i+str
# # # # # # # # # # # # # # # # # # # # # # # # # # 	return str

# # # # # # # # # # # # # # # # # # # # # # # # # # s="abhi"
# # # # # # # # # # # # # # # # # # # # # # # # # # print("Original string is" ,s,"\n",end="")
# # # # # # # # # # # # # # # # # # # # # # # # # # print("Reversed string is ",end="")
# # # # # # # # # # # # # # # # # # # # # # # # # # print(reversed(s))

# # # # # # # # # # # # # # # # # # # # # # # # # # def rev(s):
# # # # # # # # # # # # # # # # # # # # # # # # # # 	if len(s)==0:
# # # # # # # # # # # # # # # # # # # # # # # # # # 		return s
# # # # # # # # # # # # # # # # # # # # # # # # # # 	else:
# # # # # # # # # # # # # # # # # # # # # # # # # # 		return rev(s[1:])+s[0]

# # # # # # # # # # # # # # # # # # # # # # # # # # s="Abhishek"
# # # # # # # # # # # # # # # # # # # # # # # # # # print("Original string is",end=" ")
# # # # # # # # # # # # # # # # # # # # # # # # # # print(s)
# # # # # # # # # # # # # # # # # # # # # # # # # # print("Reversed String is",end=" ")
# # # # # # # # # # # # # # # # # # # # # # # # # # print(rev(s))

# # # # # # # # # # # # # # # # # # # # # # # # # def createStack():
# # # # # # # # # # # # # # # # # # # # # # # # # 	stack=[]
# # # # # # # # # # # # # # # # # # # # # # # # # 	return stack

# # # # # # # # # # # # # # # # # # # # # # # # # def push(stack,item):
# # # # # # # # # # # # # # # # # # # # # # # # # 	stack.append(item)

# # # # # # # # # # # # # # # # # # # # # # # # # def size(stack):
# # # # # # # # # # # # # # # # # # # # # # # # # 	return len(stack)

# # # # # # # # # # # # # # # # # # # # # # # # # def isempty(stack):
# # # # # # # # # # # # # # # # # # # # # # # # # 	if size(stack)==0:
# # # # # # # # # # # # # # # # # # # # # # # # # 		return True

# # # # # # # # # # # # # # # # # # # # # # # # # def pop(stack):
# # # # # # # # # # # # # # # # # # # # # # # # # 	if isempty(stack):
# # # # # # # # # # # # # # # # # # # # # # # # # 		return
# # # # # # # # # # # # # # # # # # # # # # # # # 	else:
# # # # # # # # # # # # # # # # # # # # # # # # # 		return stack.pop()

# # # # # # # # # # # # # # # # # # # # # # # # # def rev(string):
# # # # # # # # # # # # # # # # # # # # # # # # # 	n=len(string)

# # # # # # # # # # # # # # # # # # # # # # # # #   # creating Stack
# # # # # # # # # # # # # # # # # # # # # # # # # 	stack=createStack()

# # # # # # # # # # # # # # # # # # # # # # # # # 	# pushing string to stack
# # # # # # # # # # # # # # # # # # # # # # # # # 	for i in range(0,n,1):
# # # # # # # # # # # # # # # # # # # # # # # # # 		push(stack,string[i])

# # # # # # # # # # # # # # # # # # # # # # # # # 	string=""

# # # # # # # # # # # # # # # # # # # # # # # # # 	for i in range(0,n,1):
# # # # # # # # # # # # # # # # # # # # # # # # # 		string=string+pop(stack)
# # # # # # # # # # # # # # # # # # # # # # # # # 	return string

# # # # # # # # # # # # # # # # # # # # # # # # # s="Abhishek"
# # # # # # # # # # # # # # # # # # # # # # # # # print("Original string is",end=" ")
# # # # # # # # # # # # # # # # # # # # # # # # # print(s)
# # # # # # # # # # # # # # # # # # # # # # # # # print("Reversed String is",end=" ")
# # # # # # # # # # # # # # # # # # # # # # # # # print(rev(s))

# # # # # # # # # # # # # # # # # # # # # # # # def createstack():
# # # # # # # # # # # # # # # # # # # # # # # # 	stack = []
# # # # # # # # # # # # # # # # # # # # # # # # 	return stack

# # # # # # # # # # # # # # # # # # # # # # # # def push(stack, item):
# # # # # # # # # # # # # # # # # # # # # # # # 	stack.append(item)

# # # # # # # # # # # # # # # # # # # # # # # # def size(stack):
# # # # # # # # # # # # # # # # # # # # # # # # 	return len(stack)

# # # # # # # # # # # # # # # # # # # # # # # # def isempty(stack):
# # # # # # # # # # # # # # # # # # # # # # # # 	if size(s) == 0:
# # # # # # # # # # # # # # # # # # # # # # # # 		return True

# # # # # # # # # # # # # # # # # # # # # # # # def pop(stack):
# # # # # # # # # # # # # # # # # # # # # # # # 	if isempty(stack):
# # # # # # # # # # # # # # # # # # # # # # # # 		return
# # # # # # # # # # # # # # # # # # # # # # # # 	else:
# # # # # # # # # # # # # # # # # # # # # # # # 		return stack.pop()

# # # # # # # # # # # # # # # # # # # # # # # # def rev(s):
# # # # # # # # # # # # # # # # # # # # # # # # 	n = len(s)
# # # # # # # # # # # # # # # # # # # # # # # # 	stack = createstack()

# # # # # # # # # # # # # # # # # # # # # # # # 	for i in range(0, n, 1):
# # # # # # # # # # # # # # # # # # # # # # # # 		push(stack, s[i])

# # # # # # # # # # # # # # # # # # # # # # # # 	string = ""

# # # # # # # # # # # # # # # # # # # # # # # # 	for i in range(0, n, 1):
# # # # # # # # # # # # # # # # # # # # # # # # 		string = string + pop(stack)
# # # # # # # # # # # # # # # # # # # # # # # # 	return string

# # # # # # # # # # # # # # # # # # # # # # # # s = "Abhishek"
# # # # # # # # # # # # # # # # # # # # # # # # print("Orginal string is", end="")
# # # # # # # # # # # # # # # # # # # # # # # # print(s)
# # # # # # # # # # # # # # # # # # # # # # # # print("Reversed String is ", end="")
# # # # # # # # # # # # # # # # # # # # # # # # print(rev(s))

# # # # # # # # # # # # # # # # # # # # # # # a="abhishek"
# # # # # # # # # # # # # # # # # # # # # # # a="".join(reversed(a))
# # # # # # # # # # # # # # # # # # # # # # # print(a)

# # # # # # # # # # # # # # # # # # # # # # # a="abhishektk"
# # # # # # # # # # # # # # # # # # # # # # # print(a[3:-1])

# # # # # # # # # # # # # # # # # # # # # # a="hello this is string"
# # # # # # # # # # # # # # # # # # # # # # lst=list(a)
# # # # # # # # # # # # # # # # # # # # # # print(lst)

# # # # # # # # # # # # # # # # # # # # # # lst[9]='p'
# # # # # # # # # # # # # # # # # # # # # # lst2=''.join(lst)
# # # # # # # # # # # # # # # # # # # # # # print(lst2)

# # # # # # # # # # # # # # # # # # # # # # a='abhiishek'
# # # # # # # # # # # # # # # # # # # # # # b=a[0:4]+a[5:]
# # # # # # # # # # # # # # # # # # # # # # print(b)

# # # # # # # # # # # # # # # # # # # # # # a='abhi'
# # # # # # # # # # # # # # # # # # # # # # del a
# # # # # # # # # # # # # # # # # # # # # # print(a)

# # # # # # # # # # # # # # # # # # # # # # a="abhishek is a good"
# # # # # # # # # # # # # # # # # # # # # # b=""
# # # # # # # # # # # # # # # # # # # # # # print(b.endswith(a))
# # # # # # # # # # # # # # # # # # # # # # a="Abhishek is a good boy"
# # # # # # # # # # # # # # # # # # # # # # print(a.upper())
# # # # # # # # # # # # # # # # # # # # # # print(a.lower())
# # # # # # # # # # # # # # # # # # # # # # print(a.swapcase())
# # # # # # # # # # # # # # # # # # # # # # print(a.title())

# # # # # # # # # # # # # # # # # # # # # # a="abhishek is a good boy"
# # # # # # # # # # # # # # # # # # # # # # if 'isa' in a:
# # # # # # # # # # # # # # # # # # # # # # 	print("string exists")
# # # # # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # # # # # 	print("Not exists")
# # # # # # # # # # # # # # # # # # # # # def check(a,b):
# # # # # # # # # # # # # # # # # # # # # 	if(a.find(b)==-1):
# # # # # # # # # # # # # # # # # # # # # 		print("string not exists")
# # # # # # # # # # # # # # # # # # # # # 	else:
# # # # # # # # # # # # # # # # # # # # # 		print("exists")
# # # # # # # # # # # # # # # # # # # # # a="abhishek is a good boy"
# # # # # # # # # # # # # # # # # # # # # b="is ab"

# # # # # # # # # # # # # # # # # # # # # check(a,b)

# # # # # # # # # # # # # # # # # # # # import re
# # # # # # # # # # # # # # # # # # # # a="abhishek has lenovo laptop"
# # # # # # # # # # # # # # # # # # # # b="ek h"
# # # # # # # # # # # # # # # # # # # # if re.search(b,a):
# # # # # # # # # # # # # # # # # # # # 	print("present")
# # # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # # # 	print("Not present")
# # # # # # # # # # # # # # # # # # # a="abhishek has lenovo laptop"
# # # # # # # # # # # # # # # # # # # b="has"
# # # # # # # # # # # # # # # # # # # x=list(filter(lambda x: (b in a),a.split()))
# # # # # # # # # # # # # # # # # # # print(["yes" if x else "no"])

# # # # # # # # # # # # # # # # # # import operator as op
# # # # # # # # # # # # # # # # # # a="abhishek is "
# # # # # # # # # # # # # # # # # # b="is"
# # # # # # # # # # # # # # # # # # print(["yes" if op.countOf(a.split(),b)>0 else "no"])

# # # # # # # # # # # # # # # # # a="gbeezksforgeeks"
# # # # # # # # # # # # # # # # # print(min(a))
# # # # # # # # # # # # # # # # # print(max(a))

# # # # # # # # # # # # # # # # from string import maketrans
# # # # # # # # # # # # # # # # str="geeksforgeeks"

# # # # # # # # # # # # # # # # a="gek"
# # # # # # # # # # # # # # # # b="usz"

# # # # # # # # # # # # # # # # mapped=maketrans(a,b)
# # # # # # # # # # # # # # # # print(str.translate(mapped))

# # # # # # # # # # # # # # # str="nerdsfornerds is for nerds"

# # # # # # # # # # # # # # # a="nerds"
# # # # # # # # # # # # # # # b="geeks"

# # # # # # # # # # # # # # # print(str.replace(a,b,3))

# # # # # # # # # # # # # # strng=input("Enter the elemnts")
# # # # # # # # # # # # # # a=strng.split()
# # # # # # # # # # # # # # print(a)

# # # # # # # # # # # # # a=([1,2,3,4,5,6,7,8,9])
# # # # # # # # # # # # # a.reverse()
# # # # # # # # # # # # # print(a)

# # # # # # # # # # # # # a=['a','b','c','d']
# # # # # # # # # # # # # lst=a[::-1]
# # # # # # # # # # # # # print(lst)
# # # # # # # # # # # # def fun(var):
# # # # # # # # # # # # 	letters = ['a', 'e', 'i', 'o', 'u']
# # # # # # # # # # # # 	if var in letters:
# # # # # # # # # # # # 		return True
# # # # # # # # # # # # 	else:
# # # # # # # # # # # # 		return False

# # # # # # # # # # # # charcters = ['a', 'b', 'h', 'i', 's', 'h', 'e', 'k']

# # # # # # # # # # # # filtered = filter(fun, charcters)

# # # # # # # # # # # # print("Vowels Present in your name is")
# # # # # # # # # # # # for strings in filtered:
# # # # # # # # # # # # 	print((strings))

# # # # # # # # # # # a="abhishek"
# # # # # # # # # # # print(tuple(a))
# # # # # # # # # # # print(a[::-1])
# # # # # # # # # # a=("12345")
# # # # # # # # # # b=("abhishek")
# # # # # # # # # # c=tuple(a+b)
# # # # # # # # # # print(c)

# # # # # # # # # # a=tuple('abhishek')
# # # # # # # # # # print(a[::-1])

# # # # # # # # # # a="pranitha"
# # # # # # # # # # print(list(set(a)))

# # # # # # # # # # a={10,20,30,40,50}
# # # # # # # # # # b={90,30,40,50}
# # # # # # # # # # c=b.difference(a)
# # # # # # # # # # print(c)

# # # # # # # # # # a={1:'abhi',2:'nachi', 3:'rajath', 4:'kio'}
# # # # # # # # # # print(a,end=" ")

# # # # # # # # # # Creating a Nested Dictionary
# # # # # # # # # # # as shown in the below image
# # # # # # # # # # Dict = {1: 'Geeks', 2: 'For',
# # # # # # # # # # 		3: {1: 'Welcome',2: 'To', 3: 'Geeks'}}

# # # # # # # # # # print(Dict)
# # # # # # # # # import array as a

# # # # # # # # # b = a.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# # # # # # # # # for i in range(10):
# # # # # # # # # 	print(b[i], end=" ")

# # # # # # # # # b.insert(0,10)
# # # # # # # # # print()
# # # # # # # # # for i in b:
# # # # # # # # # 	print(b[i],end=" ")
# # # # # # # # # print()
# # # # # # # # # b.append(11)
# # # # # # # # # for i in b:
# # # # # # # # # 	print(b[i],end=" ")
# # # # # # # # # print()
# # # # # # # # # b.append(12)
# # # # # # # # # for i in b:
# # # # # # # # # 	print(b[i],end=" ")

# # # # # # # # import array as a

# # # # # # # # a = a.array('i', {2, 4, 6, 8, 10})
# # # # # # # # for i in range(5):
# # # # # # # # 	print(a[i], end=" ")
# # # # # # # # print()
# # # # # # # # a.pop(1)  #deletes specific index values

# # # # # # # # for i in range(4):
# # # # # # # # 	print(a[i], end=" ")
# # # # # # # # print()

# # # # # # # # a.remove(2)  #removes specific values
# # # # # # # # for i in range(3):
# # # # # # # # 	print(a[i], end=" ")

# # # # # # # import array

# # # # # # # list=[1,2,3,4,5,6,7,8,9,10]

# # # # # # # a=array.array('i',list)

# # # # # # # for i in a:
# # # # # # # 	print(i,end=" ")

# # # # # # # print()
# # # # # # # print(a[1:5])
# # # # # # # print()
# # # # # # # print(a[1:])
# # # # # # # print()
# # # # # # # print(a[1:5])
# # # # # # # print()
# # # # # # # print(a[:5])
# # # # # # # print()
# # # # # # # print(a[:])
# # # # # # # print("reverse")
# # # # # # # print(a[::-1])

# # # # # # # import array
# # # # # # # list=(1,2,3,1,2,3,5)
# # # # # # # a=array.array('i',list)

# # # # # # # for i in a:
# # # # # # # 	print(i,end=" ")
# # # # # # # print()
# # # # # # # print("1st occurance of 5 is @index :",end=" ")
# # # # # # # print(a.index(5))

# # # # # # # i = 10
# # # # # # # print("ass") if i < 15 else print(False)

# # # # # # i = "abhishek"

# # # # # # print(True) if i == 'abhishek' else print(False)

# # # # # d = dict()
# # # # # f=dict()
# # # # # s=dict()
# # # # # d['xyz'] = 123
# # # # # d['abc'] = 456
# # # # # f['abhi']=22
# # # # # s['nachi']=19
# # # # # for i in d:
# # # # # 	print("%s %s" % (i, d[i]))

# # # # # for i in f:
# # # # # 	print(f)
# # # # # for i in s:
# # # # # 	print(s)

# # # # # s='isarva info tech solution'
# # # # # for i in s:
# # # # # 	if i=='i'or i=='t':
# # # # # 		continue
# # # # # 	print(i,end=" ")

# # # # s='abhis'
# # # # for i in s:
# # # # 	pass
# # # # print(i)

# # # # for i in range(1,11):
# # # # 	print(i,end=" ")
# # # # print()
# # # # print("Sum of 1-10 values is",end=" ")
# # # # sum=0
# # # # for i in range(1,10):
# # # # 	sum+=i
# # # # print(sum)

# # # # a=[1,2,3,4]
# # # # while a:
# # # # 	print(a.pop())

# # # # count=1
# # # # while count<=10:
# # # # 	print(count)
# # # # 	count+=2

# # # # a=int(input("Enter a number"))
# # # # while a!=-1:
# # # # 	a=int(input("Enter a number"))

# # # # count = 0
# # # # while True:
# # # # 	count += 1
# # # # 	print(f"count is {count}")
# # # # 	count += 1
# # # # 	if count == 10:
# # # # 		break
# # # # print("Loop ended")

# # # # d={"hi":"abhi",'how are you ?':"good"}

# # # # for i,j in d.items():
# # # # 	print(i,j)

# # # # a=[1,4,2,3,5,3,2,1,4,6,3,9]

# # # # for i in sorted(a):
# # # # 	print(i,end=" ")
# # # # print()
# # # # for i in sorted(set(a)):
# # # # 	print(i,end=" ")

# # # # for i in reversed(range(1,10,2)):
# # # # 	print(i+1)
# # # # def add(a,b):
# # # # 	c=a+b
# # # # 	return c

# # # # a,b=10, 20
# # # # ans=add(a,b)
# # # # print(f"Sum of {a} and {b} is ",ans)

# # # # some more functions
# # # def is_prime(n):
# # # 	if n in [2, 3]:
# # # 		return True
# # # 	if (n == 1) or (n % 2 == 0):
# # # 		return False
# # # 	r = 3
# # # 	while r * r <= n:
# # # 		if n % r == 0:
# # # 			return False
# # # 		r += 2
# # # 	return True
# # # print(is_prime(79998), is_prime(79))

# # # check for prime Number
# # # def isprime(n):
# # # 	if n in [2, 3]:
# # # 		return True

# # # 	if n == 1 or n % 2 == 0:
# # # 		return False

# # # 	r=3
# # # 	while r*r<=n:
# # # 		if n%r==0:
# # # 		  return False
# # # 		r=r+1
# # # 	return True

# # # a = int(input("Enter the Number"))
# # # print(isprime(a))

# # # # check for even or odd
# # # def evenodd(n):
# # # 	if n%2==0:
# # # 		print("Even Number")
# # # 	else:
# # # 		print("Odd Number")

# # # a=int(input("ENter a Number"))
# # # evenodd(a)

# # # def myfun(* args):
# # # 	for i in args:
# # # 		print(i,end=" ")


# # # myfun('hi','hello','hwru')
# # # def myfun(**args):
# # # 	for i, j in args.items():
# # # 		print('%s==%s' % (i,j))


# # # myfun(first='abh', second='ish', third='ektk')

# # # A simple Python function to check
# # # whether x is even or odd


# # # def evenOdd(x):
# # # 	"""Function to check if the number is even or odds"""
	
# # # 	if (x % 2 == 0):
# # # 		print("even")
# # # 	else:
# # # 		print("odd")


# # # # Driver code to call the function
# # # print(evenOdd.__doc__)


# # # Square 
# # # def s(n):
# # # 	return n**5
# # # print(s(2))

# # # def myFun(a,b,c):
# # #  print("a",a)
# # #  print("b",b)
# # #  print("c",c)

# # # def myfun1(x,y,z):
# # # 	print('x',x)
# # # 	print('y',y)
# # # 	print('z',z)
	
# # # args = ("Geeks", "for", "Geeks")
# # # myFun(*args)

# # # kwargs={"x":"abhi",'y':'nachi','z':'amma'}
# # # myfun1(**kwargs)

# # # class car():
# # # 	def __init__(self,*args):
# # # 		self.price=args[0]
# # # 		self.color=args[1]

# # # audi=car(20000,'red')
# # # bmw=car(280000,'black')

# # # print(audi.price,"-->",audi.color)

# # # class student():
# # # 	def __init__(self,*args):
# # # 		self.id=args[0]
# # # 		self.place=args[1]
# # # 		self.education=args[2]


# # # abhi=student(22,"alape",'MCA')
# # # nachi=student(19,'Mangalore','puc')
# # # rajath=student(21,'Naguri','Iti')

# # # student_name=[abhi,nachi,rajath]

# # # sorted_answer=sorted(student_name,key=lambda x:x.id)

# # # for i in sorted_answer:
# # # 	print(i.id,i.place,i.education)

# # class student():
# #     def __init__(self, id, place, education, age):
# #         self.id = id
# #         self.place = place
# #         self.education = education
# #         self.age = age

# # students = []

# # # Add students using input
# # while True:
# #     id = input("Enter student id (or press q to quit): ")
# #     if id == "q":
# #         break
# #     place = input("Enter student place: ")
# #     education = input("Enter student education: ")
# #     age = int(input("Enter student age: "))
# #     student_obj = student(id, place, education, age)
# #     students.append(student_obj)

# # # Sort the list based on age
# # students_sorted_by_age = sorted(students, key=lambda x: x.age)

# # # Print the sorted list
# # for student in students_sorted_by_age:
# #     print(student.id, student.place, student.education, student.age)


# # class students():
# # 	def __init__(self,*args):
# # 		self.id=args[0]
# # 		self.name=args[1]
# # 		self.place=args[2]
# # 		self.age=args[3]
# # 		self.degree=args[4]

# # # create array
# # geeks=[]


# # while True:
# # 	id=input("Enter the id ")
# # 	if id=='q':
# # 	  	break
# # 	name=input("Enter the Student name ")
# # 	place=input("Enter the student place ")
# # 	age=input("Enter the student age ")
# # 	degree=input("Enter the student class ")
# # 	student_details=students(id,name,place,age,degree)
# # 	geeks.append(student_details)

# # all_details=sorted(geeks,key=lambda x:x.age)

# # for i in all_details:
# # 	print(f"id is {i.id} \n name is {i.name} \n place is {i.place} \n age is {i.age} \n degree is {i.degree} ")

# # def gen():
# # 	i=1

# # 	while True:
# # 		yield i*i
# # 		i+=1

# # for num in gen():
# # 	if num>100:
# # 		break
# # 	print(num)
# # def fib(n):
# # 	a,b=0,1
# # 	while(a<n):
# # 		yield a
# # 		a,b=b,a+b

# # for i in fib(9):
# # 	print(i)
# def fib(limit):
# 	a,b=0,1
# 	while a<limit:
# 		yield a
# 		a,b=b,a+b

# x=fib(10)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# for i in fib(9):
# 	print(i,end=" ")