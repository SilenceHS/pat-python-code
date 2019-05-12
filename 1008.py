a,b=input().split()
alist=[]
s=input()
slist=s.split()
for i in slist:
    alist.append(i)
blist=alist[int(a)-int(b):]+alist[:int(a)-int(b)]
for i in range(len(blist)):
    if i==0:
        print(blist[i],end='')
    else:
        print(' '+blist[i],end='')