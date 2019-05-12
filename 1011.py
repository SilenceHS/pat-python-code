n=int(input())
for i in range(n):
    a,b,c=input().split()
    if int(a)+int(b)>int(c):
        print('Case #'+str(i+1)+': true')
    else:
        print('Case #'+str(i+1)+': false')