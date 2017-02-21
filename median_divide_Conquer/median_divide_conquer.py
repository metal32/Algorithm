# Finding median in linear time complexity  O(n) for n>140 and O(1) for n=<140
import math
# Rank of x is the number of elements less than or equal to x,, so it will be in O(n)
def Rank(alist,x):
    rank=0
    for item in alist:
        if item<=x:
            rank+=1
    return rank

# Finding the value that we should use for x
# Dividing the list into a number of colums each of size 5 and then sorting each column of size 5
# Finding the median for each column and then finding the median for thee medians, that value will be our guess of x
def preCompute(S):
    col_array=[]
    medians=[]
    length=len(S)
    division=length//5
    remainder=length%5
    for i in range(division):
        col_array.append(S[5*i:5*(i+1)])
    if remainder!=0:
        col_array.append(S[(division*5):])
    for list in col_array:
        list.sort()
        if len(list)==5:
            medians.append(list[2])  # all list are of size 5 except last one 
        else:                        # and when they are sorted the median will be at index 2 if the indexes are starting at 0
            medians.append(list[len(list)/2])
    medians.sort()
    median=medians[(division+int(math.ceil(remainder/5.0)))/2]
    return median

def Select(S,i):
    x=preCompute(S)
    k=Rank(S,x)
    B=[item for item in S if item<x]
    C=[item for item in S if item>x]
    if k==i:
        return x
    else:
        if k>i:
            return Select(B,i)
        else:
            return Select(C,i-k)

S=[7,10,4,3,20,15,9]
i=4
print Select(S,i)