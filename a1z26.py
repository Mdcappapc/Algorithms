def encrypt(plain,key):
	return [ord(elm)-key for elm in plain]
def decrypt(code,key):
	return "".join(chr(elm+key) for elm in code)
print(encrypt("maziar",3))
print(decrypt([106, 94, 119, 102, 94, 111],3))
		
	