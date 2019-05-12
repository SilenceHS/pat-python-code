s=input()
alist=s.split()
a=''.join([i for i in alist[0] if i==alist[1]])
b=''.join([i for i in alist[2] if i==alist[3]])
if a=='':
    a=0
if b=='':
    b=0
print(int(a)+int(b))