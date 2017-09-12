#!/usr/bin/env python

'make choice to read text files or write text files or quit'

import os 

def write():
	
	'write() -- create a text file'

	while True:
		fname = input('Enter a filename: ')
		if os.path.exists(fname):
			print('ERROR: %s already exists\n' % fname)
		else:
			break
		# get file content (text) lines
	all = []
	print("\nEnter lines('.' by itself to quit).\n")

	# loop until user terminate input
	while True:
		entry = input('>>')
		if entry == '.':
			break
		else:
			all.append(entry)
			
	# write lines to file with proper line-ending
	fobj = open(fname, 'w')
	fobj.writelines(['%s\n' %(x) for x in all])
	fobj.close()
	print('DONE!')


def read():

	'read() -- read and display a text file'

	# get filename
	fname = input('Enter filename: ')
	print()

	# attempt to open file for reading
	try:
		fobj = open(fname, 'r+')
	except IOError as e:
		print('*** file open error:',e)
	else:
		# display contents to the sceen
		for eachLine in fobj:
			print(eachLine.strip())
			# print(eachLine, end = '')
		fobj.close()

def modify(): # This function is not good enough

	'modify() -- modify a existed text file'

	# get filename
	fname = input('Enter filename: ')

	# attempt to open file and modify every single line
	try:
		fobj = open(fname, 'r')
	except IOError as e:
		print('*** file open error:',e)
	else:
		lines = fobj.readlines()
		for i in range(len(lines)):
			temp = lines[i].strip()
			print('Line %d is: %s' %(i+1, lines[i]), end = '')
			lines[i] = input('Modify it to: ')
			j = input('[s] save [c] cancel: ')
			if j == 'c':
				lines[i] = temp

		# overwrite the file
		fobj = open(fname, 'w+')
		fobj.writelines(['%s\n' %(x) for x in lines])
		fobj.close()


print('Welcome! please make a choice:')
while True:
	choice = input("""[W] write a text file    [R] read a text file 
[M] modify the text file [Q] quit 
Your choice is: """)
	if choice == 'Q':
		break
	elif choice == 'W':
		write()
	elif choice == 'M':
		modify()
	else:
		read()
print('Thanks for using!')