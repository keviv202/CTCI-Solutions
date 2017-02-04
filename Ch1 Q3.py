class ch1q3:
	def URify(self,str):
		l = list(str)
		for i in range(0,len(l)):
			if l[i] ==(' '):
				l[i] = '%20'	
		print(''.join(l))
c = ch1q3()
c.URify("Mr John Smith")			