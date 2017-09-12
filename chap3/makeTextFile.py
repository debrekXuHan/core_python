#!/usr/bin/env python

'makeTextFile.py -- create text file'

import os
ls = os.linesep #os.linesep字符串给出当前平台使用的行终止符
                #win32平台中ls = '\r\n'

# get filename
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
fobj.writelines(['%s%s' %(x,ls) for x in all])
fobj.close()
print('DONE!')
