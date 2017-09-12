#5.2
def Multiplier(a,b):
	from decimal import Decimal
	return Decimal(a)*Decimal(b)

a = input('Enter the first number: ')
b = input('Enter the second number: ')
result = Multiplier(a,b)
print('The product is:', end = ' '); print(result)

#5.3
def Grading(grade):
	if 90 <= int(grade) <= 100:
		return('A')
	elif 80 <= int(grade) <= 89:
		return('B')
	elif 70 <= int(grade) <= 79:
		return('C')
	elif 60 <= int(grade) <= 69:
		return('D')
	else:
		return('F')

grade = input('Enter the number grade: ')
print('The letter grade is: %s' % Grading(grade))

#5.4
def LeapYear(year):
	year = int(year)
	if (year % 4 == 0 and year % 100 != 0) or year % 400 ==0:
		return('%d is a Leap Year.' % year)
	else:
		return('%d is not a Leap Year.' % year)

a = input('Enter a year: ')
print(LeapYear(a))

#5.5
def ChangeCoins(money):
	money = float(money)*100
	quarter = money // 25; money = money % 25
	dime = money // 10; money = money % 10
	cent = money // 1
	return (quarter, dime, cent)

money = input('The amount of the money(less than 1 dollar): ')
a = ChangeCoins(money)
print('There are %d quarters, %d dimes and %d cents' %(a[0], a[1], a[2]))

#5.6
def Calculator(s):
	if s.find('+') != -1:
		ls = s.split('+')
		return(float(ls[0]) + float(ls[1]))
	if s.find('-') != -1:
		ls = s.split('-')
		return(float(ls[0]) - float(ls[1]))
	if s.find('*') != -1:
		ls = s.split('*')
		return(float(ls[0]) * float(ls[1]))
	if s.find('/') != -1:
		ls = s.split('/')
		return(float(ls[0]) / float(ls[1]))
	if s.find('%') != -1:
		ls = s.split('%')
		return(float(ls[0]) % float(ls[1]))
	if s.find('^') != -1:
		ls = s.split('^')
		return(float(ls[0]) ** float(ls[1]))

a = input('Enter an expression: ')
print(Calculator(a))

#5.8
def square(length):
	area = length ** 2
	volume = length ** 3
	return [area, volume]
def circle(radius):
	import math
	area = math.pi * (radius**2)
	volume = (4/3) * math.pi * (radius**3)
	return [area, volume]

l = float(input('Enter the length: '))
s = square(l)
print('The area of the square is %f and the volume of the cubic is %f' %(s[0], s[1]))
r = float(input('Enter the radius: '))
c = circle(r)
print('The area of the circle is %f and the volume of the ball is %f' %(c[0], c[1]))

#5.10
def temperature(F):
	C = (F - 32) *(5/9)
	return C

f = float(input('Enter the Fahrenheit degree: '))
c = temperature(f)
print('The Celsius degree is: %f' % c)

#5.11
print('All the even numbers in 0~20 are: ', end  = '')
for eachNum in range(21):
	if (eachNum % 2 == 0):
		print(eachNum, end = ' ')
print()

print('All the odd numbers in 0~20 are: ', end  = '')
for eachNum in range(21):
	if (eachNum % 2):
		print(eachNum, end = ' ')
print()

e = []; o = []
for i in range(21):
	if i % 2:
		o.append(i)
	else:
		e.append(i)
print('even numbers:',e, '\n', 'odd numbers:',o)

def devide(a,b):
	if (a % b == 0):
		print('%d can be devided by %d' %(a,b))
	else:
		print('%d cannot be devided by %d' %(a,b))

s = input('Enter two numbers(a,b): ')
n = s.split(',')
devide(int(n[0]),int(n[1]))

#5.13
def time(hour, minute):
	return hour * 60 + minute

t = input('Enter the time (in form of hour:minute): ')
t = t.split(':')
m = time(int(t[0]), int(t[1]))
print('It is %d minutes.' % m)

#5.14
def InterestRate(DRate):
	return (1+DRate)**365 - 1

a = float(input('The daily interest rate is __ %: ')) / 100
b = InterestRate(a)
print('The yearly interest rate is: %f %%.' % (b*100)) # %%很重要

#5.15
def gcdNlcm(a,b):
	t = a*b
	while b != 0:
		a,b = b,a%b   #最大公约数算法
	return (a, t/a)   #最小公倍数算法

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
s = gcdNlcm(a,b)
print('gcd is %d and lcm is %d' %(s[0], s[1]))

#5.16
def Payment():
	r = float(input('Enter opening balance: '))
	s = float(input('Enter monthly payment: '))
	print('           Amount   Remaining')
	print('Pymt#   Paid        Balance')
	print('-----   ------   ----------')
	n = 0
	print(n, '      $0.00\t\t$%.2f' % r)
	while r >= s:
		n += 1
		r -= s
		#print(n, '      $%.2f        $%.2f' % (s, r))
		print(n, '      $%.2f\t\t$%.2f' % (s, r))
	#print(n+1, '      $%.2f         $0.00' % r)
	print(n+1, '      $%.2f\t\t$0.00' % r)

Payment()

#5.17
import random
S1 = []
N1 = random.randint(2, 100)
i = 0
while i < N1:
	n = random.randint(0, 2**31 - 1)
	S1.append(n)
	i += 1

N2 = random.randint(1,N1)
S2 = []
i = 0
while i < N2:
	n = random.choice(S1)
	S2.append(n)
	S1.remove(n)
	i += 1

for x in range(len(S2)):
	for y in range(len(S2)):
		if S2[x] < S2[y]:
			S2[x], S2[y] = S2[y], S2[x]

print('The random list is: ', S2)