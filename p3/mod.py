import sys

def find_starts():	
	seq = yield
	try:	
		
		while True:
			seqData=[]
			length=0
			for i in seq:
				codon=seq[length:length+3]
				if codon.upper() == "ATG" or codon.upper() == "GTG":
					seqData.append((codon,length))
				length+=1
			seq = yield (seqData)
	except StopIteration:
		pass		