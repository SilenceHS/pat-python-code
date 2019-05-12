s=input()
alist=s.split()
alist.reverse()
for i in range(len(alist)):
    if i==0:
        print(alist[i],end='')
    else:
        print(' '+alist[i],end='')