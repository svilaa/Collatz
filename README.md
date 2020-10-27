# Collatz

Source file | Python version | Characters with line endings | Characters without line endings  | Comments
---|---|---|---|---
collatz.py | 3.8 | 103 | 98 |
collatz2.py | 3.8 | 108 | 107 |
collatz-python2.py | 2.7 | 102 | 97 |
collatz2-python2.py | 2.7 | 107 | 106 |
collatz3-python2.py | 2.7 | 99 | 94 |
collatz4-python2.py | 2.7 | 97 | :top::raised_hands: **92** :raised_hands::top: | Range [0, 100001]

If collatz4-python2.py program is written in the Python Command Line, the print command can be avoided, writting only _. Obtaining **86** characters without line endings:

```python2
a=_=0
for n in range(100001):
	c,N=1,n
	while n>1:n=(n/2,n*3+1)[n%2];c+=1
	if c>a:a,_=c,N
_
```
