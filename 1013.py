a,n=input().split()
a=int(a)
n=int(n)
alist=[] 
def prime(n,a):
    flag = [1]*(n+2)
    p = 2
    count=0
    while(p <= n):
        alist.append(p)
        count+=1
        if count-1>a:
            return
        for i in range(2*p, n+1, p):
            flag[i] = 0
        while 1:
            p += 1
            if(flag[p] == 1):
                break
prime(105000,n)
c=0
for i in range(a-1,n-1):
    if (i-(a-1))%10==0:
        print(alist[i],end='')
        continue
    elif (i+1-(a-1))%10==0:
        print(' '+str(alist[i]))
        continue
    else:
        print(' '+str(alist[i]),end='')
        continue
if (n-a)%10==0:
    print(str(alist[n-1]))
else:
    print(' '+str(alist[n-1]))