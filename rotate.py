def rotate(string,number):
	do_s=string+string
	s=string
	if number<=len(s):
		return do_s[number:number+len(s)]
	else:
		return do_s[number-len(s):number]
print(rotate("supercalifragilisters",9))