mn=input("")
while True:
    try:
        mn=float(mn)
        break
    except ValueError:
        mn=input("")

mx=input("")
while True:
    try:
        mx=float(mx)
        break
    except ValueError:
        mx=input("")


vl=input("")
while True:
    try:
        vl=float(vl)
        break
    except  ValueError:
        vl=input("")

vc=input("")
while True:
    try:
        vc=float(vc)
        break
    except ValueError:
        vc=input("")
if vl<0:
    vl=vl*(-1)
if vc<0:
    vc=vc*(-1)
if mn<0:
    mn=mn*(-1)
if mx<0:
    mx=mx*(-1)

if vl-vc>=mn and vl-vc<=mx:
    print("S")

else:
    print("N")