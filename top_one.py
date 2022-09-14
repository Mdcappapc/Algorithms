def top_one(arr):
	values={}
	result=[]
	for i in range(len(arr)):
		if arr[i] in values.keys():
			values[arr[i]]+=1
		else:
			values[arr[i]]=1
	for i in values.keys():
		if values[i]==max(values.values()):
			result.append(i)
	return {result[0]:values[result[0]]}
print(top_one((1,1,2,2,3,3,3,3)))