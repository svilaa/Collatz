def _(n):return 1+_(n*3+1if n%2else n/2)if n>1else 1
d={_(n):n for n in range(100000,0,-1)};print(d[max(d)])
