class ch1q4:
	def palinpermu(self,s):
		l = list(s)	
		d={}
		for i in l:
			if i not in d:
				d[i]=1
			elif i in d:
				d[i] = d[i]+1
		c=0
		for i in d:
			if d[i]%2==0:
				continue
			elif d[i]%2!=0:
				c=c + 1
			if c >1:
				return False	
		return True

c = ch1q4()
print(c.palinpermu('taco cat'))