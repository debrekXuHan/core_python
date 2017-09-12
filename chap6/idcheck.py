#!usr/bin/env python

import string

alphas = string.ascii_letters + '_'
nums = string.digits

print('Welcome to Identifier Checker v1.0')
print('Testees must be at least 2 chars long.')
myInput = input('Indentifier to test is: ')

while not(len(myInput) >1):
	myInput = input('''Testees must be at least 2 chars long. 
Please re-enter: ''')

if myInput[0] not in alphas:
	print('invalid: first symbol must be alphabetic!')

else:
	alphanums = alphas + nums
	for otherChar in myInput[1:]:
		if otherChar not in alphanums:
			print('invalid: remaining symbols must be alphanumeric!')
			break
	else:     # for-else结构，有break直接跳过else
		print('Okay as an identifier!')