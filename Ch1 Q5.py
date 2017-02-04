class ch1q5:

	def logic(self,str1,str2):
		c = 0
		i1,i2=0,0

		while(i1<len(str1)) and i2 < len(str2):
			if str1[i1]==str2[i2]:
				i1 = i1 + 1
				i2 = i2 + 1
			elif str1[i1] != str2[i2]:
				if len(str1)> len(str2):
					i1 = i1 + 1
					c = c + 1
				elif len(str2)> len(str1):
					i2 = i2 + 1
					c = c + 1
				elif len(str2)== len(str1):
					i1 = i1 + 1
					i2 = i2 + 1
					c = c + 1
			if c >1:
				return False

		return True

	def one_way(self,str1,str2):

		if len(str1) - len(str2) == 1:
			return (self.logic(str1,str2))
		
		elif len(str1) - len(str2) ==0:
			return (self.logic(str1,str2))



c = ch1q5()
print(c.one_way('aqqer','aaae'))