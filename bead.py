def bead(seq):
	if any(not isinstance(x,int) or x<0 for x in seq):
		raise TypeError("Seq must be a tuple or list of positive numbers.")
	for _ in range(len(seq)):
		for i ,(up,low) in enumerate(zip(seq,seq[1:])):
			if up>low:
				seq[i]-=up-low
				seq[i+1]+=up-low
	return seq
print(bead([4,7,9,2,5,13]))