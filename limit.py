def limit(arr,*,min=None,max=None):
	min_check=lambda val:True if min is None else min<=val
	max_check=lambda val:True if max is None else max>=val
	return [val for val in arr if min_check(val) and max_check(val)]
#Filtering list by minimum and maximum
print(limit([1,2,3,4,5,6,7,8],min=3,max=7))