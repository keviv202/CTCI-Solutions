class ch1q6:
	def comp(self,str1):
		d={}
		l = []
		c = 1
		for i in range(1,len(str1)):
			if str1[i] == str1[i-1]:
				c = c + 1
			elif str1[i] != str1[i-1]:
				l.append(str1[i-1])
				l.append(c)
				c = 1
			if i == len(str1)-1 and str1[i] != str1[i-1]:
				l.append(str1[i])
				l.append(c)
			if i == len(str1)-1 and str1[i] == str1[i-1]:
				l.append(str1[i-1])
				l.append(c)
		print(l)

c = ch1q6()
c.comp('aaaabbbddddddaaaa')