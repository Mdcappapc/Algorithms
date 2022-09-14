import random
from random import Random,SystemRandom
class OneTime(Random):
	@staticmethod
	def randint(a,b):
		return SystemRandom().randint(a,b)
	@staticmethod
	def encrypt(text):
		plain=[ord(i) for i in text]
		key=[]
		cipher=[]
		for i in plain:
			k=OneTime.randint(1,500)
			c=(i+k)*k
			cipher.append(c)
			key.append(k)
		return cipher,key
	@staticmethod
	def decrypt(cipher,key):
		plain=[]
		for i in range(len(key)):
			v=int((cipher[i]-key[i]**2)/key[i])
			plain.append(chr(v))
		res="".join(i for i in plain)
		return res
print(OneTime.encrypt("Maziar")[0])