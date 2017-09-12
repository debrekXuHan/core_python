#6.1.2
s = 'abcde'
for i in range(-1, -len(s), -1):
	print(s[:i])

for i in [None] + list(range(-1, -len(s), -1)):
	print(s[:i])

#6.1.3
s = 'abcde'
for i in enumerate(s):
	print(i)

x = [1,2,3]; y = [4,5,6]
xy = list(zip(x,y))
print(xy)

#6.4.2
print('There are %(howmany)d %(lang)s Quotation Symbols.' %{'lang':'Python', 'howmany':3})

from string import Template
s = Template('There are ${howmany} ${lang} Quotation Symbols.')
print(s.substitute(lang='Python', howmany=3))

#6.4.3
import re
m = re.search(r'\\[rtfvn]', r'Hello World!\n')
if m is not None: 
	print(m.group())

#6.5.2
s = 'foobar'
for i, t in enumerate(s):
	print(i,t)

s, t = 'foa', 'obr'
for i, k in zip(s, t):
	print(i,k)

#6.13.2
a = [6, 4, 5]
from functools import reduce
import operator
r = reduce(operator.add, a)
print('The sum of these numbers is:%d' %r)

#6.14
music_media = ['compact disc', 45, '8-track tape', 'long playing record']
for eachMediaType in (45, '8-track tape', 'cassette'):
	if eachMediaType in music_media:
		print(music_media.index(eachMediaType))