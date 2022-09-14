def last(array,elm):
	low=0
	high=len(array)-1
	while low<=high:
		mid=(high+low)//2
		if array[mid]==elm and (mid+1==len(array) or array[mid+1]!=elm):
			return mid
		elif array[mid]<=elm:
			low=mid+1
		else:
			high=mid-1
			
print(last([1,2,2,3,3,3,4,4,4,4],3)) 