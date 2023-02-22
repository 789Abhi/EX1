# # # # # # # # # # # # with open("abhi.txt",'w') as files:
# # # # # # # # # # # # 	files.write("hello abhi")

# # # # # # # # # # # import math
# # # # # # # # # # # print(math.factorial(5))

# # # # # # # # # # n=10
# # # # # # # # # # for i in range(n):
# # # # # # # # # #  print(i,end=" ")

# # # # # # # # # g=lambda x:x*x
# # # # # # # # # print(g(2))
# # # # # # # # from math import factorial
# # # # # # # # print(factorial(5))

# # # # # # # i="Abhishek"
# # # # # # # if "f" in i:
# # # # # # # 	print("true")
# # # # # # # else:
# # # # # # # 	print("false")

# # # # # a=4
# # # # # b=4
# # # # # try:
# # # # # 	k=a//b
# # # # # 	print(int(k))

# # # # # except ZeroDivisionError :
# # # # # 	print("cant divide by zero ")
# # # # # finally:
# # # # # 	print("problem solved")

# # # # # print ("The value of a / b is : ")
# # # # # assert b != 0, "Divide by 0 error"
# # # # # print (a / b)

# # # # a=22
# # # # b='Abhishek'
# # # # print(a)
# # # # print(b)
# # # # del a
# # # # del b
# # # # a="nachi"
# # # # b="18"
# # # # print(a)
# # # # print(b)

# # # a=10
# # # b=20
# # # def add():
# # # 	c=a+b
# # # 	print(c)
# # # add()

# # # def fun():
# # # 	var=150
# # # 	def gun():
# # # 		nonlocal var
# # # 		var=var+50
# # # 		print(var)
# # # 	gun()
# # # fun()

# # # a,b,c=1,3,5
# # # print(a+b+c)
# # # g = input("Enter your name : ")
# # # print(g)

# # # a, b, c, d = input("enter 2 value:").split()
# # # print(a)
# # # print(b)
# # # print(c)
# # # print(d)

# # # taking multiple inputs at a time 
# # # and type casting using list() function
# # # x = list(input("Enter multiple values: ").split())
# # # print("List of students: ",x)
# # # x = set(input("Enter multiple values: ").split())
# # # print("List of students: ",x)


# # # x,y=[int(x) for x in input("enter 2 values:").split()]
# # # print(x,y)

# # # x=10
# # # y=20
# # # print("value of x is {} and value of y is {}".format(y,x))

# # # x=set(int(x) for x in input("ENter multiple value:").split(','))
# # # print(x)
# # # import time
# # # count_down=5
# # # for i in reversed(range(count_down+1)):
	
# # # 	if i>0:
# # # 		print(i,end=">>>",flush='true')
# # # 		time.sleep(1)
# # # 	else:
# # # 		print("start")

# # # x=20
# # # y=2
# # # z=2023
# # # print(x,y,z,sep='-')
# # # import io

# # # # declare a dummy file
# # # dummy_file = io.StringIO()

# # # # add message to the dummy file
# # # print('Hello Geeks!!', file=dummy_file)

# # # # get the value from dummy file
# # # dummy_file.getvalue()

# # # import io
# # # dummy_file = io.StringIO()
# # # print('Abhishek ', file=dummy_file)
# # # dummy_file.getvalue()

# # print("Hello Abhishek You are learnig Python",file=open('abi.html','w'))

# a=[1,2,3,4]
# for i in range(4):
# 	print(a[i],end=" ")

# a=[1,3,5,7,9]
# b=[2,4,5,6,8,8]
# print(set( a + b))
#import the below module and see what happens
# import antigravity
#NOTE - it wont work on online ide

# abhi="Abhishek"
# print(abhi.center(20,'-'))

# a=True
# b=False
# print(a and b)  

# a=10
# b=4
# print(a & b)
# print(a | b)
# print(~a)
# print(a^b)
# print(a>>2)
# print(a<<2)

# x=24
# y=20
# list=[10,20,30,40,50]
# if(x not in list):
# 	print("X not present")
# else:
# 	print("x is present")

# a=1+20*10
# print(a)

# a=140
# b=20
# min=a if a<b else b
# print(min)

a=10
b=20
# print((b,a) [a>b])
print({True: a, False: b} [a < b])