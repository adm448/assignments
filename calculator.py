def multiply(a,b):
	return a * b

def add(a,b):
	return a + b

def subtract(a,b):
	return a - b

def divide(a,b):
	return a / b

def square(a):
	return a ** 2

def cube(a):
	return a ** 3

def square_n_times(a,n):
	return (square(a)) ** n 

print "I'm going to use the calculator functions to multiply 5 and 6"
x = multiply(5,6)
print x

print "Let's test the square function with 5"
y = square(5)
print y

print "Let's also test the cube function with 2"
z = cube(2)
print z

print square_n_times(5,2)
