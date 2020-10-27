def a(n):return 1if n==1else 1+a(n*3+1if n%2else n/2)
d={a(n):n for n in range(100000,0,-1)};print(d[max(d)])
