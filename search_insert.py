def  search(array,val):
	low=0
	high=len(array)-1
	mid=high//2
	while low<=high:
		if val>array[mid]:
			mid+=1
			low=mid
		else:
			mid-=1
			high=mid
	return low
print(search([1,3,5,6],4))