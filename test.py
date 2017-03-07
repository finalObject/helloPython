L=[]
for n in range(10):
    if n <=1:
        L.append(n)
    else:
        L.append(L[n-1]+L[n-2])
print(L)
