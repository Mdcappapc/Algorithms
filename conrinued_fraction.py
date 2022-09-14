def cont_frac(numbers):
	assert len(numbers)==2,"Syntax: cont_frac((num,den))"
	num,den=numbers
	frac=num/den
	fraclist=[int(frac)]
	while frac != fraclist[-1] and round(frac,9) != fraclist[-1]:
		frac2 = frac-fraclist[-1]
		frac=pow(frac2,-1)
		fraclist.append(int(frac) if frac-int(frac) < 0.9999999 else round(frac))
	return fraclist
print(cont_frac((8,5)))