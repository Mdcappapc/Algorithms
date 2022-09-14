def move(seq):
	result=[]
	zeros=0
	for i in seq:
		if i==0 and i.__class__!=bool:
			zeros+=1
		else:
			result.append(i)
	result.extend([0]*zeros)
	return result
print(move([False,2,"Black",0,2,4,0,9]))