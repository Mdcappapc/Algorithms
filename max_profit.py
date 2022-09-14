def max_profit(arr):
	cur_max=0
	max_so_far=0
	for i in range(1,len(arr)):
		cur_max=max(0,cur_max+arr[i]-arr[i-1])
		max_so_far=max(max_so_far,cur_max)
	return max_so_far
print(max_profit([5,2,7,8,2,6,9,1,6]))