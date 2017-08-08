def returnMax(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c
a=int(raw_input("Enter No. 1: "))
b=int(raw_input("Enter No. 2: "))
c=int(raw_input("Enter No. 3: "))
d=returnMax(a,b,c)
print "%d is Largest" % (d)