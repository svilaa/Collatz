a=s=0
for _ in range(10**5+1):
	c,_=1,_
	while _>1:_=(_/2,_*3+1)[_%2];c+=1
	if c>a:a,s=c,_
print s
