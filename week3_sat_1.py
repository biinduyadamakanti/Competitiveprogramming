def par(n,m):
	s=""

	while(n!=0):
		i=n%2
		s=str(i)+s
		n=n//2

	d=""
	print(s)

	while(m>0):
		j=m%2
		d=str(j)+d
		m=m//2
	# print(d)

	c=0
	if(len(s)>len(d)):
		u=len(s)-len(d)
		for i in range(u):
			d="0"+d
	else:
		u=len(d)-len(s)
		for i in range(u):
			s="0"+s
	
	i=0
	while(i<len(s)):
		# print("in last")
		if(s[i]!=d[i]):
			c+=1
		i+=1

	return c


print(par(1,30))

