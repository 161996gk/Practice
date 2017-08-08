def allDivisor(a):
    for i in range(1,a+1):
        if a%i==0:
            print "%d, "%(i),
a=int(raw_input("enter no: "))
allDivisor(a)