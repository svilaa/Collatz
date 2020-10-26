def a(n):return 1if n==1else 1+a(n*3+1)if n%2else 1+a(n/2);d={a(n):n for n in range(1,100001)};print(d[max(d)])
