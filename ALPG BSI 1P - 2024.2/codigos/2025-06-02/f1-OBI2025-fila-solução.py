na=input("")
while True:
    try:
        na=int(na)
        break
    except ValueError:
        na=input("")

aa=input("")
l1=list(aa.split())

nc=na

for i,j in range(l1):
    if l1[0]>l1[i] and i>0:
        nc-=1
    elif l1[0]<l1[j] and l1[i]>0 and i>0 and j>0 and l1[j]>l1[i]:
        nc-=1
        