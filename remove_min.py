def remove_min(stack):
	if not len(stack):
		return stack
		
	min=stack[0]
	for i in stack:
		if i<min:
			min=i
	minimum=stack.index(min)
	stack.pop(minimum)
	return stack
print(remove_min([1,2,5,7,0,-12]))