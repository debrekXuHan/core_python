#!/usr/bin/env python
'''
An example of reading and writing Unicode string: Writes
a Unicode string to a file in utf-8 and read it back in.
'''
CODEC = 'utf-8'
FILE = 'E:/unicode.txt'

hello_out = u'Hello world\n'
bytes_out = hello_out.encode(CODEC)
f = open(FILE, 'wb')  #以bytes形式写
f.write(bytes_out)
f.close()

f = open(FILE, 'rb')  #以bytes形式读
bytes_in = f.read()
f.close()
hello_in = bytes_in.decode(CODEC)
print(hello_in, end='')