## Finding the maximum length of increasing subsequence in a sequence and the index from which it should starts the subsequence
## I have used dynamic programming to compute it.
## let's assume that you are trying to find the maximu increasing subsequence from ith element.
## in any case the choice will start from 1 and it will be equal to the length of the subsequence achieved by selecting the next element. O(n**2)
 
arr=map(int,raw_input().split())
n=len(arr)
dp={}
# Pointer to keep the index of the elements to be added in the Longest increasing subsequence
pointer={}
for i in range(n-1,-1,-1):
    choices=[1]
    pointer[i]=[arr[i]]
    sub_pointer=[]
    # calculating subsequence length for the ith element.
    for j in range(i+1,n):
        # we have to move from i+1 elements to the last elements only if the jth element is greater than the ith element.
        if arr[j]>arr[i]:
            choices.append(dp[j]+1)
            sub_pointer.append(pointer[j])
    # take the maximum of all the choices
    dp[i]=max(choices)
    if dp[i]!=1:
        pointer[i]=pointer[i]+sub_pointer[choices.index(dp[i])-1]

# take the aximum of all the dp[i] so that we can finally get the true maximum length of the subsequence and also determine 
# starting the index from where it's

list=sorted(dp.items(), key=lambda x:x[1], reverse=True)
print list[0][1]
print pointer[list[0][0]]

