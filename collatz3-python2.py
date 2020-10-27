a=_=0
for n in range(1,100001):
	c=1;N=n
	while n>1:n=(n/2,n*3+1)[n%2];c+=1
	if c>a:a=c;_=N
print _
