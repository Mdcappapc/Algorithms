from string import ascii_letters,digits
alpha=ascii_letters
def encrypt(string,key):
	result=""
	for ch in string:
		if ch not in alpha:
			result+=ch
		else:
			new_key=(alpha.index(ch)+key)%len(alpha)
			result+=alpha[new_key]
	return result
def decrypt(string,key):
	return encrypt(string,key*-1)
def brute(string=""):
	force={}
	key=1
	while key<=len(alpha):
		force[key]=decrypt(string,key)
		key+=1
	return force
print(brute("uiHqiz"))
print(encrypt("MAZIAR",9))