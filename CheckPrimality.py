a=int(raw_input("Enter no.1: "))
b=0
for i in range(1,a+1):
    if a%i==0:
        b+=1
if b==2:
    print "%d is a Prime Number" %(a)
else:
    print "%d is not a Prime Number" %(a)
