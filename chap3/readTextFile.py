#!/usr/bin/env python

'readTextFile.py -- read and display text file'

# get filename
fname = input('Enter filename: ')
print('The content in this text file is:')

# attempt to open file for reading
try:
	fobj = open(fname, 'r')
except IOError as e:
	print('*** file open error:',e)
else:
	# display contents to the sceen
	for eachLine in fobj:
		print(eachLine.strip())
		# print(eachLine, end = '')
	fobj.close()