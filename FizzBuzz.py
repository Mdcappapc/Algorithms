y=input("Enter Number : ")
for y in range(int(y if y.isdigit() else ord(y[1]))):
	i="Fizz" if not y%3 else ""
	i+="Buzz" if not y%5 else " "
	print(i)
	