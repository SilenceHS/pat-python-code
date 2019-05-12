a=list(input().zfill(4))
while True:
    aa=int(''.join(list(reversed(sorted(a)))))
    bb=int(''.join(list(sorted(a))))
    print(str(aa).zfill(4)+' - '+str(bb).zfill(4)+' = '+str(aa-bb).zfill(4))
    if aa-bb==6174 or aa-bb==0:
        break
    a=list(str(aa-bb).zfill(4))