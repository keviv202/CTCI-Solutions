class ch1q1:
	def unique(self,str):
		l = [0]*128
		for i in str:
			if l[ord(i)]:
				return False
			else :
				l[ord(i)] = 1
		return True
	
u = ch1q1()
print(u.unique("Helo"))