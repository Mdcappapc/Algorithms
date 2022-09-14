def is_isomorph(str1,str2):
	if len(str1)!=len(str2):
		return False
	dict_mor={}
	values=set()
	for i in range(len(str2)):
		if str1[i] not in dict_mor:
			if str2[i] in values:
				return False
			dict_mor[str1[i]]=str2[i]
			values.add(str2[i])
		else:
			if dict_mor[str1[i]]!=str2[i]:
				return False
	return True
print(is_isomorph("paper","title"))				
		