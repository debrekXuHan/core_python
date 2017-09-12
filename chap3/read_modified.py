#!/usr/bin/env python

'readTextFile.py -- read and display text file'

import os

# attempt to open file for reading
while True:
	fname = input('Enter a filename: ')
	if not os.path.exists(fname):
		print('ERROR: %s does not exist\n' % fname)
	else:
		break

# display contents to the sceen
fobj = open(fname, 'r')
for eachLine in fobj:
	print(eachLine, end = '')
fobj.close()