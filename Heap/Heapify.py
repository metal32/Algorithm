def max_heap(A,parent,length):
    
        left=parent*2+1
        if left>length:
            return
        if left<length and A[left]<A[left+1]:
            left=left+1
        if A[left]>A[parent]:
            swap(A,left,parent)
            parent=left
            left=2*parent+1
            max_heap(A,parent,length)


def swap(A,L,P):
    temp=0
    temp=A[L]
    A[L]=A[P]
    A[P]=temp


def build_max_heap(A,length):
    for i in xrange(length/2,-1,-1):
        max_heap(A,i,length)

def HeapSort(A,length):
    if length<1:
        return
    build_max_heap(A,length)
    swap(A,0,length)
    HeapSort(A,length-1)

A=[16,6,14,8,7,9,3,2,4,1,3,5,2,6,4,7,34,23,45,11,23]
length=len(A)-1
HeapSort(A,length)
print A