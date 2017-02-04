class ch1q2:
	def permu(self,str1,str2):
		l1,l2 = [0]*128,[0]*128
		
		if len(str1) != len(str2):
			return False

		for i in str1:
			l1[ord(i)] = l1[ord(i)]+1
		for i in str2:
			l2[ord(i)] = l2[ord(i)]+1
		if l1 == l2:
			return True
		return False

c = ch1q2()
print(c.permu("abcs","scba"))