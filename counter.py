def counter(arr,elm):
	count=1
	for i in arr:
		if i==elm:
			count+=1
	return count-1
print(counter([1,2,2,3,3,3,4,4,4,4],4))