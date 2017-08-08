def binarySearch(a,b):
    beg=0
    end=len(a)-1
    while beg<=end:
        mid = (beg + end) / 2
        if a[mid]==b:
            return True
        if(b<a[mid]):
            end=mid-1
        else:
            beg=mid+1
    return False
a=[]
n=int(raw_input("Enter size of an array: "))
for i in range(n):
    a.append(int(raw_input("Enter List element")))
a.sort()
b=int(raw_input("Enter element to be searched"))
print binarySearch(a,b)
