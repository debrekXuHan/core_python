#2.1
myString = 'Hello World!'
print(myString)

print('%s is number %d' %('Python',1))

logfile = open('E:/mylog.txt','a') #'a':以添加模式打开文件
print('Fatal Error', file = logfile) #将内容输出到指定的文件
logfile.close()

#2.2
user = input('Enter login name: ')
print('Your login is: ', user)

num = input("Enter the number: ")
print ("Doubling number %d" %(int(num)*2))

#2.5
miles = 1000.0
kilometers = 1.609 * miles
print('%f miles is same as %f km' %(miles,kilometers))

#2.9
aDict = {'host':'earth'}
aDict['port'] = 80
for key in aDict:
	print(key,aDict[key]) #在交互窗口中print前需要缩进

#2.12
counter = 0
while counter < 3:
	print('loop #%d' %(counter))
	counter += 1

#2.13
print('I like to use the Internet for:')
for item in ['email','net-surfing','homework','chat']:
	print(item,end=' ')
print()

who = 'knights'
what = 'Ni!'
print('We are the',who,'who say',what,what,what,what)
print('We are the %s who say %s' %(who,(what + ' ')*4))

for eachNum in [0,1,2]:
	print (eachNum)
for eachNum in range(3):
	print (eachNum)

foo = 'abc'
for i in range(len(foo)):
	print(foo[i], '(%d)' % i)
for i, ch in enumerate(foo):
	print(ch, '(%d)' % i)

#2.14
squared = [x**2 for x in range(4)]
for i in squared:
	print (i)
squared = [x**2 for x in range(8) if not x%2]
for i in squared:
	print (i)

#2.15
filename = input('Enter file name: ') #文件名为E:/mylog.txt
fobj = open(filename, 'r')
for eachLine in fobj:
	print (eachLine, end = '')
fobj.close()

#2.16 处理错误和异常
try:
	filename = input('Enter file name: ')
	fobj = open(filename, 'r')
	for eachLine in fobj:
		print(eachLine, end = '')
	fobj.close()
except IOError as e:
	print('Oops! Something is wrong. \nFile open error:',e)

#2.17.3 定义一个函数（参数具有默认值）
def foo(debug = True):
	'Determine if in debug mode with default argument'
	if debug:
		print('in debug mode')
	print('done')

#2.18 创建一个类
class FooClass(object):
	"""My very first class: FooClass"""
	version = 0.1    # class (data) attribute
	def __init__(self, nm = 'John Doe'):
		"""constructor"""
		self.name = nm   # class instance (data)  attribute
		print('Created a class instance for',nm)
	def showname(self):
		"""display instance attribute and class name"""
		print('Your name is',self.name)
		print('My name is',self.__class__.__name__)
	def showver(self):
		"""display class (static) attribute"""
		print(self.version)   # reference FooClass.version
	def addMe2Me(self,x):
		"""apply + operation to argument"""
		return x+x

#2.19
import sys
sys.stdout.write('Hello World!\n')  # 导入模块的方式进行输出