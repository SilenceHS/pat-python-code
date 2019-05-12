s=input()
a=s.split()
xishu=a[0::2]
zhishu=a[1::2]
sum=[]
flag=0
for i in range(len(xishu)):
    a=int(xishu[i])*int(zhishu[i])
    if (a==0):
        continue
    sum.append(a)
    sum.append(int(zhishu[i])-1)
    flag=1
for i in range(len(sum)):
    if i==0:
        print(sum[i],end='')
    else:
        print(' '+str(sum[i]),end='')
if flag==0:
    print('0 0',end='')