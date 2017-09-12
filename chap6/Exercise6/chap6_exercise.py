# 6_3(a)
def order(nlist):
	newlist = []
	for x in nlist:
		newlist.append(int(x))
	return sorted(newlist, reverse=True)

nlist = []
nums = input('Enter a sequence of numbers(seperate by comma): ')  #键盘输入一个数字列表

for i in nums.split(', '):   #以', '隔开的数字序列
	nlist.append(int(i))
newlist = order(nlist)

print('The decreasing order of the sequence is:', newlist)

# 6_3(b)
def order(nlist):
	newlist = []
	for x in nlist:
		newlist.append(str(x))  #以字典序进行排序
	return sorted(newlist, reverse=True)

nlist = []
nums = input('Enter a sequence of numbers(seperate by comma): ')
for i in nums.split(', '):   #以', '隔开的数字序列
	nlist.append(int(i))
newlist = order(nlist)

print('The decreasing order of the sequence is:', newlist)

# 6_4
def Average():
	Totalscore = []
	while True:
		Input = input('Input the score(if no more scores press ENTER directly to quit): ')
		try:
			Totalscore.append(float(Input))
		except:
			break

	if len(Totalscore):
		return sum(Totalscore)/len(Totalscore)
	else:
		print('False')

print('The average score is: %f' % Average())

# 6_5(a)
def showstr():
	string = input('Input a string: ')
	if len(string) == 0:
		print('False!')
		return False
	elif len(string) == 1:
		print(string)
		return True
	else:
		for i, ch in enumerate(string):
			if i == 0:
				print(string[0:2])
			elif i == len(string)-1:
				print(string[i-1:])
			else:
				print(string[i-1:i+2])
		return True
		
showstr()

# 6_5(b)
def compare():
	FirstString = input('Input the first string: ').upper()  
	#去掉upper()可以区分大小写
	SecondString = input('Input the second string: ').upper()
	diff = len(FirstString) - len(SecondString)

	if not diff == 0:
		print('These two strings are different!')
		return False
	else:
		for i, ch in enumerate(FirstString):
			if  not ord(ch) == ord(SecondString[i]):
				print('These two strings are different!')
				return False
				break
		else:  # for-else结构
			print('These two strings are the same!')
			return True

compare()

# 6_5(c)
def isback():
	import string
	# 控制符表示ASCII码中0~31以及127这33个无法输出的字符，再加上空格
	control = [chr(i) for i in range(0,32)] + list(string.whitespace)
	control.append(chr(127))

	String = input('Input a string: ')
	new = []
	for i in String:
		if i in control:
			continue  # continue语句，if条件满足跳过本次循环，进行下一个循环
		else:
			new.append(i)

	length = len(new)
	if length%2:
		print('This string is not a palindromic!')
		return False
	else:
		half = int(length/2)
		if new[0:half] == new[-1:half-1:-1]:
			print('This string is a palindromic!')
			return True
		else:
			print('This string is not a palindromic!')
			return False

isback()

# 6_5(d)
def beback():
	String = input('Input a string: ')
	return String + String[::-1]
  # return String + String[-1:-len(String)-1:-1]

p = beback()
print('The palindromic result is %s.' % p)

# 6_6
def Strip():  
# 在string.strip()中要进行string.lstrip()和string.rstrip()操作
	String = input('Input a string: ')
	# lstrip()
	for i1,ch in enumerate(String):
		if ch != ' ':
			break
	#rstrip()
	for i2, ch in enumerate(String[::-1]):
		if ch != ' ':
			break
			
	if i2 == 0:
		return String[i1:]
	else:
		return String[i1:-i2]

result = Strip()
print('The striped result is: %s' % result)