"""                                             Sorting in a linear time                                    """

## Counting sort(It doesn't depend on comparison) it's complexicity is O(n+k)
## Assumptions: N keys sorting are integers and each fits in a word
## We have an array of lot's of integers as a key already stored in an ordered form and when we pass our array it will look at the number 
## then according the key will increase the count in it's memory

def countingsort( aList, k ):  #k is the value range from 0
    counter = [0] * ( k + 1 )
    for i in aList:
      counter[i] += 1
 
    ndx = 0
    for i in range( len( counter ) ):
      while 0 < counter[i]:
        aList[ndx] = i
        ndx += 1
        counter[i] -= 1
    return aList
s=[2,3,5,8,1,5,9,4,7,5,3,9,3,4,8,5,8,7,5,4,3,6,4]
k=10
print countingsort(s,k)