'''                             Longest Increasing subsequence in O(nlogn)                                                      '''  
# Steps
#1 if A[i] is smallest in all the elements selected then start a new active list of length 1
#2 if A[i] is largest among all end candidates of active lists, we will clone the largest active list, and extedn it by A[i]
#3 if A[i] is in between, we will find a list with largest end element that is smaller than A[i], clone and extend the list by A[i]
#     and discard all other lists of same length

import math
def LIS(S):
    n=len(S)
    # P[k] will have the index of the predecessor of S[k], where S[k] is the last number in the longest increasing sequence.
    # M[j] will have the index k of S[k] such that there is an increasing subsequence of length j having last number S[k] 
    P=[0]*n
    M=[0]*(n+1)
    L=0
    for i in range(n):
        low=1
        high=L
        while low<=high:
            mid=int(math.ceil((low+high)/2.0))
            if S[M[mid]]<S[i]:
                low=mid+1
            else:
                high=mid-1
        # new length of the subsequence
        newL=low
        P[i]=M[newL-1]
        M[newL]=i

        if newL>L:
            L=newL
    alist=[0 for i  in range(L)]
    k=M[L]
    for i in range(L-1,-1,-1):
        alist[i]=S[k]
        k=P[k]
    return alist


S=[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print LIS(S)