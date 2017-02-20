""" BUBBLE SORT"""
def bubblesort(s):
    temp=0
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i]>s[j]:
                temp=s[j]
                s[j]=s[i]
                s[i]=temp
        print s
    print "The list is sorted"
    return s
a=[1,5,3,9,20,35,67,3,5,7]
#print bubblesort(a)

"""SHORT BUBBLE SORT"""
def shortbubblesort(s):
    swaped=True
    length=len(s)-1
    while length>0 and swaped:
        swapped= False
        for i in range(len(s)-1):
            if s[i]>s[i+1]:
                temp=s[i+1]
                s[i+1]=s[i]
                s[i]=temp
                swapped=True
        length-=1
        print s
#b=[1,2,3,4,6,7,9,10]
#shortbubblesort(b)


"""SELECTION SORT"""
def selectionSort(s):
    position=0
    for i in range(len(s)):
        min=i
        for j in range(i+1,len(s)):
            if s[min]>s[j]:
                min=j
        temp=s[i]
        s[i]=s[min]
        s[min]=temp
        print s
    print "The list is sorted"
    return s
#print selectionSort(a)


""" MERGE SORT""" 

## FIRST WE NEED TO WRITE A FUNCTION IN WHICH HOW CAN TWO LIST BE MERGE
## LEFT AND RIGHT ARE ALREADY SORTED LIST
""" BUBBLE SORT"""
def bubblesort(s):
    temp=0
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i]>s[j]:
                temp=s[j]
                s[j]=s[i]
                s[i]=temp
        print s
    print "The list is sorted"
    return s
a=[1,5,3,9,20,35,67,3,5,7]
#print bubblesort(a)

"""SHORT BUBBLE SORT"""
def shortbubblesort(s):
    swaped=True
    length=len(s)-1
    while length>0 and swaped:
        swapped= False
        for i in range(len(s)-1):
            if s[i]>s[i+1]:
                temp=s[i+1]
                s[i+1]=s[i]
                s[i]=temp
                swapped=True
        length-=1
        print s
#b=[1,2,3,4,6,7,9,10]
#shortbubblesort(b)


"""SELECTION SORT"""
def selectionSort(s):
    position=0
    for i in range(len(s)):
        min=i
        for j in range(i+1,len(s)):
            if s[min]>s[j]:
                min=j
        temp=s[i]
        s[i]=s[min]
        s[min]=temp
        print s
    print "The list is sorted"
    return s
#print selectionSort(a)


""" MERGE SORT""" 

## FIRST WE NEED TO WRITE A FUNCTION IN WHICH HOW CAN TWO LIST BE MERGE
## LEFT AND RIGHT ARE ALREADY SORTED LIST
def merge(left,right):
    global count
    l=len(left)
    r=len(right)
    i=0
    j=0
    result=[]
    while i<l and j<r:
        if left[i]<=right[j]:
            result.append(left[i])
            i=i+1
        else:
            result.append(right[j])
            j=j+1
            count=count+l-i
    while i<l:
        result.append(left[i])
        i=i+1
    while j<r:
        result.append(right[j])
        j=j+1
    return result

def mergesort(alist):
    length=len(alist)
    if length<2:
        return alist
    else:
        mid=length/2
        left=mergesort(alist[:mid])
        right=mergesort(alist[mid:])
        together=merge(left,right)
        return together
count=0
alist=[3,5,2,7,9,1,0,5,7,3,7,4,68,23,12,4,7,9,100]
print mergesort(alist)
# Count calculates the inversion that is the shift taken place in merge sorting
print count