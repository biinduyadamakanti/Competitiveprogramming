def count(n):
	s=""
	c=0
	while(n>0):
		i=n%2
		s=str(i)+s
		n=n//2
	for i in range(len(s)):
		if(i+1<len(s)):
			if s[i]==str(1) and s[i+1]==str(1):
				c+=1
	return c

print(count(256))