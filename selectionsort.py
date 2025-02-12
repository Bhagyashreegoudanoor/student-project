import time
import random
def selectionsort (a):
    n=len(a)
    for i in range(n-1):
        min=i
        for j in range(i+1,n-1):
            if a[j]<a[min]:
                min=j
                a[i],a[j+i]=a[j+1],a[i]
start=time.time()
n=int(input("enter the number of element in the array"))
x=[]
for i in range(n):
    ele=(random.randint(1,100))
    x.append(ele)
print("befor sorting:",x)
selectionsort(x)
print("after sorting",x)
end=time.time()
print("running time",end-start)
    