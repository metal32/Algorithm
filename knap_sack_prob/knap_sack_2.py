# Order O(n*s), pseudopolynomial 
# Guess is to select an item orr not
# there are n.s nodes and n.s edges, so the shortest path will be O(V+E) i.e. O(n*s)
# recursion is max(dp[i+1][j],dp[i+1][j-s[i]]+v[i])

## With bottom-up approach
# topological order is from last item to 0th item

s=[1,5,3,4,5,6,2,3,4]
v=[15,10,9,23,10,4,7,19,10]
S=10
n=len(v)
def knapSack(n,S,s,v):
    dp=[[0]*(S+1) for i in range(n+1)]
    for i in range(n,-1,-1):
        for j in range(S+1): 
            if i==n:
                dp[i][j]=0
            else:
                choices=[]
                choices.append(dp[i+1][j])
                if j>=s[i]:
                    choices.append(dp[i+1][j-s[i]]+v[i])
                dp[i][j]=max(choices)
    return dp[0][S]
 
print knapSack(n,S,s,v)

