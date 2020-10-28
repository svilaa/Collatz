# Collatz

Source file | Python version | Characters with line endings | Characters without line endings  | Comments
---|---|---|---|---
collatz.py | 3.8 | 103 | 98 | Range [1, 100000]
collatz2.py | 3.8 | 108 | 107 | Range [1, 100000]
collatz-python2.py | 2.7 | 102 | 97 | Range [1, 100000]
collatz2-python2.py | 2.7 | 107 | 106 | Range [1, 100000]
collatz3-python2.py | 2.7 | 99 | 94 | Range [1, 100000]
collatz4-python2.py | 2.7 | 97 | :top::raised_hands: **92** :raised_hands::top: | Range [0, 100000]

If collatz4-python2.py program is written in the Python Command Line, the print command can be avoided, writting only _. Obtaining **86** characters without line endings:

```python2
a=_=0
for n in range(100001):
	c,N=1,n
	while n>1:n=(n/2,n*3+1)[n%2];c+=1
	if c>a:a,_=c,N
_
```

**Update**
With the [a-zA-Z0-9]* character count. There are **41** characters for PCL:

```python2
a=s=0
for _ in range(10**5+1):
	c,N=1,_
	while _>1:_=(_/2,_*3+1)[_%2];c+=1
	if c>a:a,s=c,N
s
```

**29** characters with PCL and range [1, 100000]:

```python2
a=s=(""!="")
for _ in range((""==""),(((""=="")+(""=="")+(""=="")+(""=="")+(""=="")+(""=="")+(""=="")+(""=="")+(""=="")+(""==""))**((""=="")+(""=="")+(""=="")+(""=="")+(""==""))+(""==""))):
	c,N=(""==""),_
	while _>(""==""):_=(_/((""=="")+(""=="")),_*((""=="")+(""=="")+(""==""))+(""==""))[_%((""=="")+(""==""))];c+=(""=="")
	if c>a:a,s=c,N
s
```
