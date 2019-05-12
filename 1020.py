Sum=0
n=[float(x) for x in input().split()]
a=[float(x) for x in input().split()]
b=[float(x) for x in input().split()]
c=[b[i]/a[i] for i in range(len(a))]
x=c
alist=[x.index(i) for i in reversed(sorted(x))]
for i in alist:
    if a[i]<n[1]:
        Sum+=b[i]
        n[1]=n[1]-a[i]
    elif a[i]>=n[1]:
        Sum+=n[1]*c[i]
        break
print('%.2f'%Sum)