a=[1,2,3,4,5]
c=[]
for i in range(0,len(a)+1):
    for j in range(0,len(a)+1):
        c.append(a[i:j])

c.sort()
while [] in c:
    c.remove([])
c.insert(0,[])
print(c,"\n Length= ",len(c))