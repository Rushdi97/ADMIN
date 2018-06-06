#calculate pi via dart throwing algorithm

import random 
import math
import sys

#obtain how many darts to be thrown(cmd line arg)
numDarts = int(sys.argv[1])

#keeps track of what hits the dart board
hits = 0

for x in range(numDarts + 1):
	#obtain x and y coords 
	x=random.random();
	y=random.random();
	#find distance
	dist=math.sqrt(x*x + y*y)
	
	#determine if it hit the board and if so increment hits by 1
	if dist < 1 or dist ==1:
		hits = hits + 1
		
print("pi estimate " + str(4*(hits/numDarts)))
