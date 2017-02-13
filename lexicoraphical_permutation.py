## Agorithm from https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
## Next Lexicographical permutations
#1) Select the non-increasing suffix
#2) Pivot the element prefix to the suffix
#3) Find the smallest element in the suffix
#4) replace pivot with the element
#5) reverse the whole suffix part
#6) Done
def nextPermutation(arr):
    # Find non-increasing suffix
    i=len(arr)-1
    while i>0 and arr[i-1]>=arr[i]:
        i-=1
    print i
    if i<=0:
        return 'no answer'
    # find succesor to pivot, j>i and arr[j]<=arr[i-1]
    j=len(arr)-1
    print j
    while arr[j]<=arr[i-1]:
        j-=1
    # Reverse the suffix
    arr[i-1],arr[j]=arr[j],arr[i-1]
    arr[i:]=arr[len(arr)-1:i-1:-1]
    return ''.join(arr)
test=input()
for i in range(test):
    s=raw_input()
    s=list(s)
    print nextPermutation(s)
    
