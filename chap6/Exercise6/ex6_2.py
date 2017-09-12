#!usr/bin/env python

import string
import keyword

alphas = string.ascii_letters + '_'
nums = string.digits

print('Welcome to Identifier Checker v1.1')
myInput = input('Indentifier to test is: ')

while len(myInput) == 0:
	myInput = input('''No identifier is entered. 
Please enter an identifier: ''')

if myInput in keyword.kwlist:
	print('Invalid: this is a keyword of Python!')
else:
	if myInput[0] not in alphas:
		print('Invalid: first symbol must be alphabetic!')
	else:
		alphanums = alphas + nums
		for otherChar in myInput[1:]:
			if otherChar not in alphanums:
				print('Invalid: remaining symbols must be alphanumeric!')
				break
		else:
			print('Okay as an identifier!')