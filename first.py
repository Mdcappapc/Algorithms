def first(array,elm):
	low=0
	high=len(array)-1
	while low<=high:
		mid=(high+low)//2
		if high==low:
			break
		if array[mid]<elm:
			low=mid+1
		else:
			high=mid
			
	if array[low]==elm:
		return low
print(first([1,1,2,2,3,3,4,4,5],4))