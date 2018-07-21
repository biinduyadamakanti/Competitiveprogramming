





def me(l):
	a=[]
	for n in range(l+1):
		s=""
		c=0
		while(n!=0):
			i=n%2
			if(i==1):
				c+=1
			s=str(i)+s
			n=n//2
		a.append(c)
	return a

l=[5,15,16,1,25,5,6]
x=[]
m=[[0,1,1,2,1,2],[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4],[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1],[0, 1],[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2,3, 2, 3, 3, 4, 2, 3],[0, 1, 1, 2, 1, 2],[0, 1, 1, 2, 1, 2, 2]]
for i in range(len(l)):
	x=me(l[i])
	c=0
	for j in range(len(m[i])):
		if x[j]==m[i][j]:
			c+=1
	if(c==len(m[i])):
		print("testcase  "+str(i)+"  passed...")
