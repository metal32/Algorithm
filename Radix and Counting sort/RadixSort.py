"""                             Sorting in a linear time                                                         """

## Radix sort
## Assumption: Imagine each integer as base b instead of decimal
## number of digits=d=logk base b
## Sort integers by their least significance digits to sort by their most significance digits
## then sort each of the above step by Counting sort by using digit, it's order of complexitiy is O(n+b)
## since all the digits are between 0 and b-1
## so total time is O((n+b)d) since their are d digits
## so above complexicity will be minimum when b=n so the final complexicity is O(kn)
import unittest
 
class Test( unittest.TestCase ):
 
  def testRadixsort( self ):
      A = [18, 5, 100, 3, 1, 19, 6, 0, 7, 4, 2]
      radixsort( A )
      for i in range( 1, len( A ) ):
          if A[i - 1] > A[i]:
            self.fail( "radixsort method fails." )

def radixsort( aList ):
  RADIX = 10
  maxLength = False
  tmp , placement = -1, 1
 
  while not maxLength:
    maxLength = True
    # declare and initialize buckets
    buckets = [list() for _ in range( RADIX )]
 
    # split aList between lists
    for  i in aList:
      tmp = i / placement
      buckets[tmp % RADIX].append( i )
      if maxLength and tmp > 0:
        maxLength = False
 
    # empty lists into aList array
    a = 0
    for b in range( RADIX ):
      buck = buckets[b]
      for i in buck:
        aList[a] = i
        a += 1
 
    # move to next digit
    placement *= RADIX