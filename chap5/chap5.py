# 5.6.2
import math
for eachNum in range(10):
	print(round(math.pi, eachNum))

import math
for eachNum in (.2, .7, 1.2, 1.7, -.2, -.7, -1.2, -1.7):
	print('int(%.1f)\t%+.1f' %(eachNum, int(eachNum))) 
	# \t代表tab键，%+.1f表示显示正负号保留一位小数的浮点数
	print('floor(%.1f)\t%+.1f' %(eachNum, math.floor(eachNum)))
	print('round(%.1f)\t%+.1f' %(eachNum,round(eachNum)))
	print('-'*20)

# 5.7.2
x = 0.0
for i in range(10):
	x+= 0.1
	print(x)

from decimal import Decimal
dec1 = Decimal(.1)
dec2 = Decimal('.1')
print(dec1); print(dec2)