# QuickSort is practially more used than merge sort as in merge sort auxillary space is of 
import random
def QuickSort(arr,p,r):
    if p<r:
        pivot=random.choice(arr[p:r+1])
        index=arr.index(pivot)
        temp=arr[r]
        arr[r]=pivot
        arr[index]=temp
        q=partition(arr,p,r)
        QuickSort(arr,p,q-1)
        QuickSort(arr,q+1,r)

def partition(arr,p,r):
    #pivot element
    x=arr[r]
    i=p-1
    for j in range(p,r):
        if arr[j]<=x:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1

A=[13,19,9,5,12,8,7,4,21,2,6,11]
n=len(A)-1
QuickSort(A,0,n)
print A