s=b=0
for n in range(1,100001):
    c=1;m=n
    while n!=1:n=(n*3+1,n/2)[n%2];c+=1
    if c>s:s=c;b=m
print(b)
