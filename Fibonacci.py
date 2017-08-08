def generateFib(a):
    if a<=2:
        if a==1:
            print "0"
        else:
            print "0, 1"
    else:
        b=0
        c=1
        print "0, 1, ",
        for i in range(3,a+1):
            d=b+c
            b = c
            c=d
            print "%d, " %(d),
a=int(raw_input("Enter No: "))
generateFib(a)