import random;lst=[];flag=1
item=" "
while flag and item !="!":
	lst.append(item)
	item=input("Item:")
pop=lst.pop(0)
while flag and pop:
	randommaker=random.SystemRandom()
	print(randommaker.choice(lst))
	pop=int(input("0.Exit 1.Again"))
print(lst)
	