import time
def binarysearch(a,k):
    low=0
    high=len(a)-1
    while low<=high:
        mid=(high+low)//2
        if a[mid]==k:
            return mid
        elif k<a[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1
#main code
start=time.time()
a=[13,24,34,46,57,68,79]
print("the array element are:",a)
k=int(input("enter element to be searched"))
Bin=binarysearch(a,k)
if Bin==-1:
    print("search is unsuccessfull")
else:
    print("search is successfull and element is good of location", Bin+1)
end=time.time()
print("recursion=",end-start)