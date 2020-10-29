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
With the [a-zA-Z0-9]* character count. There are **41** characters for PCL (python 2.7):

```python2
a=s=0
for _ in range(10**5+1):
	c,N=1,_
	while _>1:_=(_/2,_*3+1)[_%2];c+=1
	if c>a:a,s=c,N
s
```

**29** characters with PCL and range [1, 100000] (python 2.7):

```python2
a=s=(""!="")
for _ in range((""==""),(((""=="")+(""=="")+(""=="")+(""=="")+(""=="")+(""=="")+(""=="")+(""=="")+(""=="")+(""==""))**((""=="")+(""=="")+(""=="")+(""=="")+(""==""))+(""==""))):
	c,N=(""==""),_
	while _>(""==""):_=(_/((""=="")+(""=="")),_*((""=="")+(""=="")+(""==""))+(""==""))[_%((""=="")+(""==""))];c+=(""=="")
	if c>a:a,s=c,N
s
```

**17** characters with PCL and range [1, 100000] (python 2.7):

```python2
__=___=(""!="")
for _ in range((""==""),(((""=="")+(""=="")+(""=="")+(""=="")+(""=="")+(""=="")+(""=="")+(""=="")+(""=="")+(""==""))**((""=="")+(""=="")+(""=="")+(""=="")+(""==""))+(""==""))):
	____,_____=(""==""),_
	while _>(""==""):_=(_/((""=="")+(""=="")),_*((""=="")+(""=="")+(""==""))+(""==""))[_%((""=="")+(""==""))];____+=(""=="")
	if ____>__:__,___=____,_____
___
```

**15** characters with PCL and range [1, 100000] (python 2.7):
```python2
__=___=(""!="")
for _ in range((""==""),(((""=="")+(""=="")+(""=="")+(""=="")+(""=="")+(""=="")+(""=="")+(""=="")+(""=="")+(""==""))**((""=="")+(""=="")+(""=="")+(""=="")+(""==""))+(""==""))):
	____,_____=(""==""),_
	while _>(""==""):_=(_/((""=="")+(""=="")),_*((""=="")+(""=="")+(""==""))+(""==""))[_%((""=="")+(""==""))];____+=(""=="")
	__,___=((__,___),(____,_____))[____>__]
___
```

**10** characters writing collatz_underscore_pcl_4.py in PCL and range \[1, 100000\] (python 3.8). Only words for, in and while, added \~- and -\~ operations to avoid n!=1 and c+=1, changed //2 to >>1:

```python3
_=''=='';__=_+_;___=__+_;____=___+_;_____=____+_;______=_____+_;_______=______+_;________=_______+_;_________=________+_;__________=_________+_;______________=~-_
___________ = [ ...avoided, check full file... ]

____________=_____________=______________
for ______________ in ___________:
	_______________,________________=_,______________
	while ~-______________:______________=(______________>>_,______________*___+_)[______________%__];_______________=-~_______________
	____________,_____________=((____________,_____________),(_______________,________________))[_______________>____________]
_____________
```
