#lambda problems 

#problem1
x=lambda a: a+10
print(x(15))
#lambda function can take any nbumbers of arguments

#problem2
y= lambda a,b,c :a*b*c
print(y(6,7,5))
#summarize the argument a,b,c and return the result:

#problem3
z=lambda a,b,c:a+b+c
print(z(13,45,67))
#a lamda function is small anonymous function
#a lambda function can take any number of arguments ,
#but can only have one expression

#problem4
def myfunc(n):
	return lambda a:a*n
double=myfunc(5)
print(double(10))

#problem5

#trible function
def myfunc(n):
	return lambda a:a*n
triple=myfunc(3)
print(triple(3))
#or use the same function defimsastion to make both function ,in the same program:

#problem 6

def myfunc(m):
	return lambda a:a*m
a=myfunc(10)
b=myfunc(15)
print(a(5))
print(b(10))
