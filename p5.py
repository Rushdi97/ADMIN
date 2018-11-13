import sys
import hashlib
from random import randint


hashType =getattr( hashlib,sys.argv[1])
numDigits = int(sys.argv[2])
string = sys.argv[4]
numZeros=int(sys.argv[3])

print (string)

if numDigits == 1:
	for i in range(00,100):
		count = 0
		count2=0
		x = str(i) + string
		hash_object = hashType(x.encode())
		hex_dig = hash_object.hexdigest()
		for c in hex_dig:
			if c != '0':
				count2 = count2 +1
			elif c == '0' and count2 == 0:
				count= count +1
		
		if count == numZeros :
			print ("   ","{0:01}".format(i)," ",hex_dig)

elif numDigits == 2:
	for i in range(00,100):
		count = 0
		count2=0
		x = str(i) + string
		hash_object = hashType(x.encode())
		hex_dig = hash_object.hexdigest()
		for c in hex_dig:
			if c != '0':
				count2 = count2 +1
			elif c == '0' and count2 == 0:
				count= count +1
		
		if count == numZeros :
			print ("   ","{0:02}".format(i)," ",hex_dig)

elif numDigits == 3:
	for i in range(000,1000):
		count = 0
		count2=0
		x = str(i) + string
		hash_object = hashType(x.encode())
		hex_dig = hash_object.hexdigest()
		for c in hex_dig:
			if c != '0':
				count2 = count2 +1
			elif c == '0' and count2 == 0:
				count= count +1
		
		if count == numZeros :
			print ("   ","{0:03}".format(i)," ",hex_dig)
		
elif numDigits == 4:
	for i in range(0000,10000):
		count = 0
		count2=0
		x = str(i) + string
		hash_object = hashType(x.encode())
		hex_dig = hash_object.hexdigest()
		for c in hex_dig:
			if c != '0':
				count2 = count2 +1
			elif c == '0' and count2 == 0:
				count= count +1
		
		if count == numZeros :
			print ("   ","{0:04}".format(i)," ",hex_dig)
elif numDigits == 5:
	for i in range(00000,100000):
		count = 0
		count2=0
		x = str(i) + string
		hash_object = hashType(x.encode())
		hex_dig = hash_object.hexdigest()
		for c in hex_dig:
			if c != '0':
				count2 = count2 +1
			elif c == '0' and count2 == 0:
				count= count +1
		
		if count == numZeros :
			print ("   ","{0:05}".format(i)," ",hex_dig)
			
elif numDigits == 6:
	for i in range(0000,1000000):
		count = 0
		count2=0
		x = str(i) + string
		hash_object = hashType(x.encode())
		hex_dig = hash_object.hexdigest()
		for c in hex_dig:
			if c != '0':
				count2 = count2 +1
			elif c == '0' and count2 == 0:
				count= count +1
		
		if count == numZeros :
			print ("   ","{0:06}".format(i)," ",hex_dig)
elif numDigits == 7:
	for i in range(0000,10000000):
		count = 0
		count2=0
		x = str(i) + string
		hash_object = hashType(x.encode())
		hex_dig = hash_object.hexdigest()
		for c in hex_dig:
			if c != '0':
				count2 = count2 +1
			elif c == '0' and count2 == 0:
				count= count +1
		
		if count == numZeros :
			print ("   ","{0:07}".format(i)," ",hex_dig)
			
elif numDigits == 8:
	for i in range(0000,100000000):
		count = 0
		count2=0
		x = str(i) + string
		hash_object = hashType(x.encode())
		hex_dig = hash_object.hexdigest()
		for c in hex_dig:
			if c != '0':
				count2 = count2 +1
			elif c == '0' and count2 == 0:
				count= count +1
		
		if count == numZeros :
			print ("   ","{0:08}".format(i)," ",hex_dig)

elif numDigits == 9:
	for i in range(0000,1000000000):
		count = 0
		count2=0
		x = str(i) + string
		hash_object = hashType(x.encode())
		hex_dig = hash_object.hexdigest()
		for c in hex_dig: