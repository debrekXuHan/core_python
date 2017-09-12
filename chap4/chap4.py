#4.1
#!/usr/bin/env python

def displayNumType(num):
	print(num, 'is', end = ' ')
	if isinstance(num, (int, float, complex)):
		print('a number of type:', type(num).__name__)
	else:
		print('not a number at all')

displayNumType(-69)
displayNumType(99999999999999999999) #在python 3.x中没有long型，统一为int型
displayNumType(98.6)
displayNumType(-5.2+1.9j)
displayNumType('xxx')

def displayNumType(num):
	print(num, 'is', end = ' ')
	if type(num) == int:
		print('an integer.')
	else:
		print('not an integer.')


displayNumType(-69)
displayNumType(99999999999999999999) #在python 3.x中没有long型，统一为int型
displayNumType(98.6)
displayNumType(-5.2+1.9j)
displayNumType('xxx')

# exercise 4.9
a = 0
b = 0
c = 0
d = 0
while a is b:
	a += 1
	b += 1
while c is d:
	c -= 1
	d -= 1
print('The buffer range for simple int number is: %d to %d.' %(c+1,a-1))