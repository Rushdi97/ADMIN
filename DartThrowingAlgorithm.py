import random 
import math
import sys

numDarts = int(sys.argv[1])#obtain how many darts to be thrown(cmd line arg)

hits = 0

for x in range(numDarts):
	#obtain x and y coords 
	x=random.random();
	y=random.random();
	#find distance
	dist=math.sqrt(x*x + y*y)
	
	if dist < 1 or dist ==1:
		hits = hits + 1
		
		
	
	
print("pi estimate " + str(4*(hits/numDarts)))
