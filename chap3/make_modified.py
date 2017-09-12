#!/usr/bin/env python

import os
ls = os.linesep

fname = input('Enter filename: ')
try:
	fobj = open(fname, 'r')
	fobj.close()
	print('%s already exists.' % fname)
except IOError:
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
	fobj.writelines(['%s%s' %(x,ls) for x in all])
	fobj.close()
	print('DONE!') 