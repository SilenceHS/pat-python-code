'''
1007 素数对猜想 （20 分)
让我们定义d
​n
​​ 为：d
​n
​​ =p
​n+1
​​ −p
​n
​​ ，其中p
​i
​​ 是第i个素数。显然有d
​1
​​ =1，且对于n>1有d
​n
​​ 是偶数。“素数对猜想”认为“存在无穷多对相邻且差为2的素数”。

现给定任意正整数N(<10
​5
​​ )，请计算不超过N的满足猜想的素数对的个数。

输入格式:

输入在一行给出正整数N。

输出格式:

在一行中输出不超过N的满足猜想的素数对的个数。

输入样例:

20
输出样例:

4
'''
import math
n=input()
n=int(n)
alist=[1 for x in range(0,n+1)]
blist=[]
p=2
while p< alist.__len__():
    while True:
        if p>=len(alist):
            break
        if alist[p]==1:
            blist.append(p)
            for k in range(p+p,len(alist),p):
                alist[k]=0
            p+=1
            break
        else:
            p+=1
count=0
for i in range(len(blist)):
    if blist[i]-blist[i-1]==2:
        count+=1
print(count)
