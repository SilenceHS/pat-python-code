adict1={'A':'MON','B':'TUE','C':'WED','D':'THU','E':'FRI','F':'SAT','G':'SUN'}
alist=[]
for i in range(4):
    alist.append(input())
if len(alist[0])>len(alist[1]):
    alist[0]=alist[0][:len(alist[1]):]
if len(alist[2])>len(alist[3]):
    alist[2]=alist[2][:len(alist[3]):]
if len(alist[0])<len(alist[1]):
    alist[1]=alist[1][:len(alist[0]):]
if len(alist[2])<len(alist[3]):
    alist[3]=alist[3][:len(alist[2]):]
aposition=0
bposition=0
a=[]
b=[]
flag=0
flag2=0
for i in alist[0]:
    if alist[1][aposition]==i:
        a.append(i)
    aposition+=1
for i in alist[2]:
    if alist[3][bposition]==i and i.isalpha():
        b.append(bposition)
        break
    bposition+=1
# print(a)
# print(b)
p1=0
for i in range(len(a)):
    if a[i].isupper() and a[i]>='A' and a[i]<='G':
        print(adict1[a[i]],end='')
        p1=i
        break
for i in range(p1+1,len(a)):
    if a[i]>='0' and a[i]<='9':
        print(' 0'+a[i]+':',end='')
        break
    elif a[i]>='A' and a[i]<='N':
        print(' '+str(ord(a[i])-ord('A')+10)+':',end='')
        break
print("%02d" %b[0])
