#2.2
a = 1 + 2 * 4
print(a)

#2.4
#(a)
string = input('Enter some words: ')
print('What you typed is:',string)
#(b)
num = input('Enter a number: ')
print('The number you entered is: %d' %(int(num)))

#2.5
#(a)
counter = 0
while counter <= 10:
	print(counter, end = ' ')
	counter += 1
print()
#(b)
for num in range(11):
	print(num, end =' ')
print()

#2.6
num = input('Enter a number: ')
num = int(num)
if num > 0:
	print('%d is a positive number.' % num)
elif num < 0:
	print('%d is a negative number.' % num)
else:
	print('The number is zero.')

#2.7
string = input('Enter a string: ')
counter = 0
while counter < len(string):
	print(string[counter], end = ' ')
	counter += 1
print()

for ch in string:
	print(ch, end = ' ')
print()

#2.8
# while循环
print('Enter five numbers: ')
sum  = 0
counter = 0
while counter < 5:
	num = input('n%d = ' % (counter+1))
	num = int(num)
	sum += num
	counter += 1
print('The sum is: %d' % sum)
# for循环
print('Enter five numbers: ')
sum  = 0
for i in range(5):
	num = input('n%d = ' % (i+1))
	num = int(num)
	sum += num
print('The sum is: %d' % sum)
# 答案（最后生成一个列表v）
print('Enter five numbers: ')
v = [] #生成一个空列表
s = 0
for i in range(5):
	num = input('n%d = ' % (i+1))
	v.extend([int(num)])
	s += v[i]
print('The sum is: %d' % s)

#2.9
print('Enter five numbers: ')
v = []
s = 0
for i in range(5):
	num = input('n%d = ' % (i+1))
	v.extend([int(num)])
	s += v[i]
print('The mean is: %f' % (s/len(v)))

#2.10
num = input('Enter a number: ')
while int(num) > 100 or int(num) < 0:
	num = input('Failed. Input another number: ')
print('Done. The number is %d' % (int(num)))

#2.11
print('Welcome!')
choice = input('[1] sum [2] mean [X] exit: ')
while choice == '1' or choice == '2':
	if choice == '1':
		print('Enter five numbers: ')
		v = []
		s = 0
		for i in range(5):
			num = input('n%d = ' % (i+1))
			v.extend([int(num)])
			s += v[i]
		print('The sum is %d' % s)
	else:
		print('Enter five numbers: ')
		v = []
		s = 0
		for i in range(5):
			num = input('n%d = ' % (i+1))
			v.extend([int(num)])
			s += v[i]
		m = s/len(v)
		print('The mean is %f' % m)
	choice = input('[1] sum [2] mean [X] exit: ')
print('Thanks for using!')

#2.15
#从小到大
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))
if a > b:
	buff = a
	a = b
	b = buff
if c > b:
	print('The ascending order is %d, %d, %d' %(a,b,c))
elif c < a:
	print('The ascending order is %d, %d, %d' %(c,a,b))
else:
	print('The ascending order is %d, %d, %d' %(a,c,b))
#从大到小
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))
if a < b:
	buff = a
	a = b
	b = buff
if c < b:
	print('The descending order is %d, %d, %d' %(a,b,c))
elif c > a:
	print('The descending order is %d, %d, %d' %(c,a,b))
else:
	print('The descending order is %d, %d, %d' %(a,c,b))

# 答案（建立一个空列表）
#从小到大
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))
n = []
if a > b:
	a,b = b,a #交换两者的值
if a > c:
	a,c = c,a
if b > c:
	b,c = c,b
n.extend([a,b,c])
print('The ascending order is:',n)
#从大到小
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))
n = []
if a < b:
	a,b = b,a #交换两者的值
if a < c:
	a,c = c,a
if b < c:
	b,c = c,b
n.extend([a,b,c])
print('The descending order is:',n)