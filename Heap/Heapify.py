#Create Heap
def max_heapify(alist,length,parent):
    left=2*parent+1
    if left>length:
        return
    if left<length and alist[left]<alist[left+1]:
        left=left+1
    if alist[left]>alist[parent]:
        swap(alist,left,parent)
        parent=left
        left=2*parent+1
        max_heapify(alist,length,parent)
        

def swap(alist,left,parent):
    temp=alist[left]
    alist[left]=alist[parent]
    alist[parent]=temp

def build_Max_heap(alist,length):
    for i in range(length/2-1,-1,-1):
        max_heapify(alist,length,i)
    

def heap_sort(alist,length):
    if length<1:
        return
    max_heapify(alist,length,0) 
    swap(alist,0,length)
    heap_sort(alist,length-1)

A=[16,6,4,8,7,39,3,2,4,1,3,5,2,41,4,7,34,23,45,11,23]
length=len(A)-1
build_Max_heap(A,length)
heap_sort(A,length)
print A


    
   