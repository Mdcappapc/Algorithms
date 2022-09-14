def ACHA(string , **kwargs):
	types=kwargs["types"]
	main=[str(abs((ord(i)*len(i))+hash(string)+hash(i))) for i in string]
	joint=ascii(str(types((int(r"".join(main)))*int(main[-1])))[2:].encode())
	return joint[:445]+"'" if not joint[:445].endswith("'") else joint[:445]
print(ACHA("Maziar",types=oct))