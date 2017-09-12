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