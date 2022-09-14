def end(arr,elm):
	if elm in arr:
		for i in range(arr.count(elm)):
			arr.remove(elm)
			arr.append(elm)
	return arr
print(end([1,2,2,3,3,3,4,4,4,4],2))